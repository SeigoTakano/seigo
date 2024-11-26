from django.db import models

class SeigoPost(models.Model):
    pass

class Student(models.Model):

    student_id = models.CharField(max_length=10, unique=True)  # 学籍番号

    name = models.CharField(max_length=100)  # 名前

    def __str__(self):

        return self.name


class Score(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # 学生

    subject = models.CharField(max_length=100)  # 科目

    score = models.IntegerField()  # 得点

    def __str__(self):

        return f"{self.student.name} - {self.subject}: {self.score}点" 
