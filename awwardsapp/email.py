from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #creating sender and the message subject
    sender='mnazwambura@gmail.com'
    subject='welcome to NazAwwards'

    #passing in the context vairables
    html_content=render_to_string('email/awwardsemail.html',{"name":name})
    text_content=render_to_string('email/awwardsemail.txt',{"name":name})
     
    msg=EmailMultiAlternatives(subject,sender,text_content,[receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()




