from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')
def Contact(request):
    return render(request, 'Contact.html')
def Projects(request):
    return render(request, 'Projects.html')
def sent(request):
    import smtplib
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('yashpythonemail@gmail.com', 'y@shgurukul')
    Name = request.GET.get('Name', 'default')
    Name = Name.rstrip()
    Name = Name.lstrip()
    User_Message = request.GET.get('Message', 'default')
    User_Message = User_Message.rstrip()
    User_Message = User_Message.lstrip()
    howDidYouGetHere = request.GET.get('howGethere', 'default')
    howDidYouGetHere  = howDidYouGetHere.rstrip()
    howDidYouGetHere  = howDidYouGetHere.lstrip()

    mail.sendmail('yashpythonemail@gmail.com', 'yash.gurukul12@gmail.com', f'Subject: Mail from {Name} [Yash\'s Django Website]\n\nHi Yash, This is a Website mail bot from Python AnyWhere.com\n\n(Message From User is) - \n{User_Message}\n\n(How did You Get Here) - \n{howDidYouGetHere}\n\nThanks\n\tNote-This is a mail sent with Python Automation. If got this by mistake, please ignore.')
    mail.quit()
    return HttpResponse('Sent')