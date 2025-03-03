import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(report_file):

    sender_email = "snoobetest@gmail.com"
    receiver_email = "shubhampareek838@gmail.com"
    password = "wyai kazk otrr kocd"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Pytest Report"

    body = "Please find the attached pytest report."
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(report_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={report_file}")
    msg.attach(part)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
