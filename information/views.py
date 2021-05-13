#
# File: views.py
# Project: MomentumX
# Application: information
# Author: Christian Rustoeen <christian34@protonmail.com>
#
# All files are under git version control
#

from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    """ Landing page for project """
    return render(request, 'information/index.html')


def about(request):
    """ Short information about the project """
    return render(request, 'information/about.html')


def help(request):
    """ Everything the user needs to know about the project """
    return render(request, 'information/help.html')


def contact(request):
    """ Provides contact information for help, support and other requests """

    success = False
    subject = "MomentumX request"
    to_address = "exceed26@gmail.com"
    request_categories = {
                            1: "Help/Support",
                            2: "Advertising",
                            3: "Other business requests",
                        }

    # SMTP settings are configured in settings.py
    # to use google' smtp server and a gmail account to send mail

    # TODO: Mail is not being sent through gmail. Needs to configure
    # gmail properly. Gmail is refusing email as long as you dont 
    # have your own account where you explicitly says that gmail 
    # can use this account to send email. This needs to be an account 
    # that is only used for sending email from one application as this 
    # makes the account less secure. There should not be any email kept 
    # inside this account.
    # 

    if request.POST:
        from_address = request.POST['email']
        message = request.POST['message']

        print("=================")
        print("Sending email...")
        print("==================")
        # Send mail from user
        send_mail(subject,
                  message,
                  from_address,
                  [to_address],
                  fail_silently=False,
        )
        success = True

    return render(request, 'information/contact.html',
                  {'success': success})


def learn_to_invest(request):
    return render(request, 'information/learn_to_invest.html')
