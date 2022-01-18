from django.shortcuts import render
from .forms import ContactFormEmail
from django.core.mail import  send_mail


def contactsendemail(request):
          if request.method=="GET":
                    form=ContactFormEmail()
          else:
                    form=ContactFormEmail(request.POST)
                    if form.is_valid():
                              fromemail=form.cleaned_data['fromemail']
                              subject=form.cleaned_data['subject']
                              message=form.cleaned_data['message']
                              send_mail(subject, message,fromemail,['dyuldashev278@gmail.com', fromemail])

          return render(request, 'index.html', {'form':form})
