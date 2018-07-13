from django.db import models as m


class Question(m.Model):
    text = m.CharField(max_length=1024)
    answer_type = m.CharField(max_length=1024, default='Other')

    def __str__(self):
        return self.text


class GoldAnswer(m.Model):
    text = m.CharField(max_length=1024)
    question = m.ForeignKey(Question, related_name='gold_answers', on_delete=m.CASCADE)

    def __str__(self):
        return self.text

class AnswerCandidate(m.Model):
    fid = m.CharField(max_length=1024)
    text = m.CharField(max_length=1024)
    question = m.ForeignKey(Question, related_name='candidates', on_delete=m.CASCADE)

    def __str__(self):
        return self.text + '(' +  self.fid + ')'

class AnswerTriple(m.Model):
    fid = m.CharField(max_length=1024)
    text = m.CharField(max_length=1024)
    relation = m.CharField(max_length=1024, default='')
    score = m.FloatField(default=0.0)
    question = m.ForeignKey(Question, related_name='answer_triples', on_delete=m.CASCADE)

    def __str__(self):
        return self.relation + '(' +  self.text + ')'

class PredAnswer(m.Model):
    text = m.CharField(max_length=1024)
    question = m.ForeignKey(Question, related_name='pred_answers', on_delete=m.CASCADE)

    def __str__(self):
        return self.text


class DecomposedQuestion(m.Model):
    question = m.ForeignKey(Question, related_name='decomposed_list', on_delete=m.CASCADE)
    text = m.CharField(max_length=1024)
    pos_tagging = m.CharField(max_length=1024, default='')

    def __str__(self):
        return self.text

class GraphEdge(m.Model):
    question = m.ForeignKey(Question, related_name='graph_edges', on_delete=m.CASCADE)
    entity1 = m.CharField(max_length=1024, default='')
    relation = m.CharField(max_length=1024, default='')
    entity2 = m.CharField(max_length=1024, default='')

    def __str__(self):
        return self.entity1 + self.relation + self.entity2

class Tripple(m.Model):
    question = m.ForeignKey(Question, related_name='tripples', on_delete=m.CASCADE)
    relation = m.CharField(max_length=1024, default='')
    subject_text = m.CharField(max_length=1024, default='')
    subject_id = m.CharField(max_length=1024, default='')

    def __str__(self):
        return self.relation + self.subject_text

class QueryCandidate(m.Model):
    question = m.ForeignKey(Question, related_name='query_candidates', on_delete=m.CASCADE)
    type = m.CharField(max_length=1024, default='')
    e1 = m.CharField(max_length=1024, default='')
    e2 = m.CharField(max_length=1024, default='')
    r1 = m.CharField(max_length=1024, default='')
    r2 = m.CharField(max_length=1024, default='')
    r3 = m.CharField(max_length=1024, default='')
    score = m.FloatField(default=0.0)