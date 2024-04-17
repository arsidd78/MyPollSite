from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=300,blank=False)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.question
class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choices=models.CharField(max_length=200,blank=False)
    updated=models.DateTimeField(auto_now=True)  
    votes=models.IntegerField(default=0)  
    def __str__(self) -> str:
        return self.choices