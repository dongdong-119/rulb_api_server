import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

smtpName = 'smtp.naver.com'
smtpPort = 587
sendEmail = 'b3199@naver.com'
password = 'Rhehdgml12#'


def send_mail(title, content, email_to, image) -> None:

    server = smtplib.SMTP(smtpName, smtpPort)
    server.starttls()
    server.login(sendEmail, password)

    msg = MIMEBase('multipart', 'mixed')

    content = MIMEText(content)

    msg['Subject'] = title
    msg['From'] = sendEmail
    msg['To'] = email_to

    msg.attach(content)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(image)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="첨부파일')
    msg.attach(part)

    server.sendmail(
        from_addr=sendEmail,
        to_addrs='kodong119@gmail.com',
        msg=msg.as_string()
    )
    server.close()