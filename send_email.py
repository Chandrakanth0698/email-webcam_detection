import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Your credentials
gmail_user = 'de.chandra226@gmail.com'
gmail_password = 'gmail_password'


def send_email(filename):
    # Create the container email message.
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = gmail_user
    msg['Subject'] = 'Object detected using python script'

    # Body of the email
    body = 'The object which is detected is attached to this email as an attachment'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image file
    # Path to your image file
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(gmail_user, 'de.chandra226@gmail.com', text)
    server.quit()
