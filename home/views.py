from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail 
from django.core.mail import settings


# Create your views here.


def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        subject  = request.POST.get('subject')
        message  = request.POST.get('message')

        send_mail(
                email ,
                subject +message,
                settings.EMAIL_HOST_USER,
                ['thisissachinr@gmail.com'],
                fail_silently=False,
            )
    return render(request, "index.html", {name:'name'})
#I had actually done this from Django a while back. Open up a legitimate GMail account & enter the credentials here. Here's my code -




# from email import encoders
# from email.MIMEBase import MIMEBase
# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart
# def sendmail(to, subject, text, attach=[], mtype='html'):
#     ok = True
#     gmail_user = settings.EMAIL_HOST_USER
#     gmail_pwd  = settings.EMAIL_HOST_PASSWORD

#     msg = MIMEMultipart('alternative')

#     msg['From']    = gmail_user
#     msg['To']      = to
#     msg['Cc']      = 'you@gmail.com'
#     msg['Subject'] = subject

#     msg.attach(MIMEText(text, mtype))

#     for a in attach:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(open(attach, 'rb').read())
#         Encoders.encode_base64(part)
#         part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(a))
#         msg.attach(part)

#     try:
#         mailServer = smtplib.SMTP("smtp.gmail.com", 687)
#         mailServer.ehlo()
#         mailServer.starttls()
#         mailServer.ehlo()
#         mailServer.login(gmail_user, gmail_pwd)
#         mailServer.sendmail(gmail_user, [to,msg['Cc']], msg.as_string())
#         mailServer.close()
#     except:
#         ok = False
#     return ok
    
