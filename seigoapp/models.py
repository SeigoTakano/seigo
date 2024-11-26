from django.db import models

class SeigoPost(models.Model):
    stu_num = models.CharField(verbose_name= "学生番号" , max_length=100)
    name = models.CharField(verbose_name= "名前" , max_length=100)
    subject = models.CharField(verbose_name= "科目" , max_length=100)
    score = models.CharField(verbose_name= "得点" , max_length=100)
    datetime = models.DateField(verbose_name= "投稿日時" , auto_now_add=True )

    def __str__(self):
        return self.stu_num

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
