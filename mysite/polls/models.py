from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Question[%d]=%s' %(self.id, self.question_text);


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "Choice[%d]=%s" %(self.id, self.choice_text)
