from django.test import TestCase

# Create your tests here.


from mysite.polls import models

q = models.Question("dddd")
q.save()