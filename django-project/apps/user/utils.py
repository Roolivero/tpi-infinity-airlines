import random 
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings


def generateOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1, 9))

    return otp

def send_code_to_user(email):
    Subject = "Codigo de verificacion infinity airlines"
    otp_code = generateOtp()

    print(otp_code)

    user=User.objects.get(email=email)
    current_size = "myAuth.com"
    email_body = f"Hola {user.first_name} gracias por registrarte en {current_size} por favor verifica tu mail con el \n codigo de verificacion {otp_code} "
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    d_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    d_email.send(fail_silently=True)