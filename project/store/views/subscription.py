from django.shortcuts import render,redirect
from store.models.subscribe import Subscribe
from django.views import View
from django.core.mail import send_mail

class Subscription(View):
    def post(self , request):
        email = request.POST.get('email')
        new_email = Subscribe(email=email)
        email_data =Subscribe.objects.all().values()
        email_list =[]
        for oldemail in email_data:
            email_list.append(oldemail['email'])
        if email not in email_list:
            new_email.save()

            send_mail(
                "Thanks for subscripting",
                '''Thanks for subscripting
This is an auto-generated email. 
Please DO NOT reply to this email''',
                "coffeefancynews@gmail.com",
                [new_email],
                fail_silently=False,
            )


        return render(request, 'subscribe.html', {})
