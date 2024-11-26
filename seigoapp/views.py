from django.shortcuts import render , redirect

from .models import SeigoPost , Student , Score

from django.views.generic.base import TemplateView

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import ContactForm , StudentForm ,ScoreForm

from django.contrib import messages

from django.core.mail import EmailMessage

from django.views.generic import ListView, CreateView

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

import json


class IndexView(TemplateView):
    template_name = "index.html"

class MypageView(TemplateView):
    template_name = 'mypage.html'

class Stu_scoreView(TemplateView):
    template_name = 'stu_score.html'

class ScheduleView(TemplateView):
    template_name = 'schedule.html'

class ContactView(FormView):
    template_name = 'contact.html'

    form_class = ContactForm

    success_url = reverse_lazy('seigoapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ :{}'.format(title)

        message = \
        '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'.format(name,email,title,message)
        from_email = 'tdn2430115@stu.o-hara.ac.jp'
        to_list = ['tdn2430115@stu.o-hara.ac.jp']

        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)

        message.send()

        messages.success(self.request,'お問い合わせは正常に送信されました。')

        return super().form_valid(form)



@csrf_exempt

def register_student_with_score(request):

    if request.method == "POST":

        data = json.loads(request.body)

        student_id = data.get('student_id')

        name = data.get('name')

        subject = data.get('subject')

        score = data.get('score')

        if not (student_id and name and subject and score is not None):

            return JsonResponse({'message': 'すべてのフィールドを正しく入力してください。'}, status=400)

        student, created = Student.objects.get_or_create(student_id=student_id, defaults={'name': name})

        if not created and student.name != name:

            return JsonResponse({'message': '異なる名前で同じ学籍番号が既に存在します。'}, status=400)

        Score.objects.create(student=student, subject=subject, score=score)

        return JsonResponse({'message': f'学生 {name} (学籍番号: {student_id}) の {subject} の得点を {score} 点に登録しました。'})

    return JsonResponse({'message': '無効なリクエストです。'}, status=400) 