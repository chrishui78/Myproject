from django.shortcuts import render ,redirect
from django.views import View
from store.models.contact import Contact
from store.forms import ContactForm


class Contact(View):
    def get(self,request):
        
        return render(request,'contact.html')
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():

            form.save()

        return render(request,'contact.html')