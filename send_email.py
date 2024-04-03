import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "firad.aslanov28@gmail.com"
    password = "madndggwjnstiaxv"
    receiver = "firad.aslanov28@gmail.com"
    context = ssl.create_default_context()
    message = f"""
{message}
    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

