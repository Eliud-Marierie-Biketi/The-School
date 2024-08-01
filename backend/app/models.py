from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Exam(models.Model):
    title = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date = models.DateField()

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

