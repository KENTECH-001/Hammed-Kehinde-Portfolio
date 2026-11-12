from django.shortcuts import render, redirect
from django.contrib import messages
from .models import information
import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# Create your views here.


def send_email(name, email, subject, content):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv('BREVO_API_KEY')

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": "hammednurein017@gmail.com"}],
        sender={
            "name": "Hammed Kehinde",
            "email": "hammedkehinde017@gmail.com"
        },
        reply_to={
            "email": email,
            "name": name
        },
        subject=subject,
        text_content=content
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
        return True

    except ApiException as error:
        print("Brevo email error:", error)
        return False


def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        information.objects.create(name=name, email=email, subject=subject, content=content)
        result = send_email(name, email, subject, content)

        if result:
            messages.success(request, 'Your Message Has Been Sent\n We Will Give You Feedback Soon')
        
        else:
            messages.error(request, 'Message Has not Been Sent Due To Some Issues\n Please Try Again Later')

        return redirect('index')
        
    return render(request, 'index.html')


def project_detail(request):
    return render (request, 'project_detail.html')



