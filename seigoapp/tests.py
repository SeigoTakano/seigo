    stu_num = models.CharField(verbose_name= "学生番号" , max_length=100)
    name = models.CharField(verbose_name= "名前" , max_length=100)
    subject = models.CharField(verbose_name= "科目" , max_length=100)
    score = models.CharField(verbose_name= "得点" , max_length=100)
    datetime = models.DateField(verbose_name= "投稿日時" , auto_now_add=True )

    def __str__(self):
        return self.stu_num