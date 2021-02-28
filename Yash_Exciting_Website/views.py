from django.http import HttpResponse
from django.shortcuts import render
import smtplib
import emoji
from email.mime.text import MIMEText
from email.utils import formataddr
import wolframalpha as wf
import re
import wikipedia as wiki

def intro(request):
    return render(request, 'intro.html')

def skills(request):
    return render(request, 'skills.html')

def homepage(request):
    return render(request, 'index.html')

def follow(request):
    return render(request, 'follow.html')

def ans(request):
    message0 = request.GET.get('query', 'default')
    message0 = re.sub(emoji.get_emoji_regexp(), r"", message0)
    message1 = message0.lower()

    try:
        app_id = '8X8K8R-866YJ4X5RE'
        client = wf.Client(app_id)
        result = client.query(message1)
        answer = next(result.results).text
        return render(request, 'answer.html', {'res': answer + '  ', 'mes': message0})
    except Exception:
        try:
            answer = wiki.summary(message1, sentences=3)
            return render(request, 'answer.html', {'res': answer + '  ', 'mes': message0})
        except Exception:
            return render(request, 'answer.html', {'res': 'Sorry, I am unable to understand you. 😢' + '  ', 'mes': message0})

def chat(request):
    return render(request, 'chat.html')


def Contact(request):
    return render(request, 'Contact.html')


def Projects(request):
    return render(request, 'Projects.html')

def SourceCodeNTNN(request):
    return render(request, 'NumberToNumberNames_SourceCode.html')

def SourceCodeYTD(request):
    return render(request, 'YouTubeVideoDownloader.html')

def SourceCodeMD(request):
    return render(request, 'MotionDetector.html')


def sent(request):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo_or_helo_if_needed()
    mail.login('yashpythonemail@gmail.com', 'ijarileucauossqo')

    def strip_emoji(text):
        new_text = re.sub(emoji.get_emoji_regexp(), r"", text)
        return new_text

    Name = request.GET.get('Name', 'default')
    Name = Name.rstrip()
    Name = Name.lstrip()
    Name = strip_emoji(Name)
    User_Message = request.GET.get('Message','default')
    User_Message = User_Message.rstrip()
    User_Message = User_Message.lstrip()
    User_Message = strip_emoji(User_Message)
    howDidYouGetHere = request.GET.get('howGethere', 'default')
    howDidYouGetHere = howDidYouGetHere.rstrip()
    howDidYouGetHere = howDidYouGetHere.lstrip()
    howDidYouGetHere = strip_emoji(howDidYouGetHere)

    params = {'From_': Name, 'Message': User_Message, 'How': howDidYouGetHere}

    msg = MIMEText(r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
      .heading {
      background-color: #0a043c;
    }

    body {
      margin: 0;
      background-color: #1687a7;
    }

    .from {
      background-color: #1687a7;
    }

    .message {
      background-color: #1687a7;
    }

    hr {
      background-color: #0a043c;
      height: 1px;
      width: 75%;
      border-color: #0a043c;
    }

    .special {
      background-color: #19456b;
      height: 1px;
      width: 45%;
      border-color: #19456b;
    }

    .heads1 {
      margin: 0;
      top: 1;
      font-family: Maiandra GD;
      font-size: 175%;
    }

    .heads2 {
      margin: 0;
      font-family: Maiandra GD;
      font-size: 175%;
    }

    .user_message_entry {
      margin: 0;
      font-family: Maiandra GD;
      font-size: 175%;
    }

    </style>
</head>
<body style="background-color: #1687a7;">
<div class="heading">
  <center>
    <img src="https://github.com/Yash-Varshney-Creativities/Yash-Varshney-Creativities/blob/main/Head.jpg?raw=true">
  </center>
</div>
<br>
<div class="from">
  <center>
    <p style="color: #d3e0ea;" class="heads1">Mail From """ + Name + """</p>
    <p></p>
  </center>
  <hr>
</div>
<br>
<div class="message">
  <center>
    <p style="color: #d3e0ea;" class="heads2">Message</p>
    <br>
    <hr noshade class="special">
    <p style="color: #d3e0ea;" class="user_message_entry">""" + User_Message + """</p>
  </center>
</div>
<hr>
<div class="message">
    <center>
      <br>
      <p style="color: #d3e0ea;" class="heads2">How Did You Get Here?</p>
      <br>
      <hr noshade class="special">
      <p style="color: #d3e0ea;" class="user_message_entry">""" + howDidYouGetHere + """</p>
    </center>
  <hr>
  <br><br><br><br><br><br><br><br><br>
</div>
</body>
</html>
""", 'html')

    msg['To'] = formataddr(('YashVarshney', 'yash.gurukul12@gmail.com'))
    msg['From'] = formataddr(('YashPythonEmail', 'yashpythonemail@gmail.com'))
    msg['Subject'] = f'Mail From {Name} [Yash\'s Django Website]'
    mail.sendmail('yashpythonemail@gmail.com', 'yash.gurukul12@gmail.com', msg.as_string())
    mail.quit()

    return render(request, 'sent.html', params)
