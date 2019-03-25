import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def send_email(content, subject, email_setting, filename=None):
    msg = MIMEMultipart("alternative")
    # msg = MIMEText(content,"html")
    msg["Subject"] = subject  
    msg["From"] = email_setting["sender"]
    msg["To"] = email_setting["receiver"]
    msg["Cc"] = email_setting["cc"]
    if filename:
        ctype = "application/octet-stream"  
        maintype, subtype = ctype.split("/", 1)   
        attachment_file = MIMEImage((lambda f: (f.read(), f.close()))(open(filename, "rb"))[0], _subtype = subtype)
        attachment_file.add_header("Content-Disposition", "attachment", filename=filename.replace("\\","/").split("/")[-1])
        msg.attach(attachment_file) 
        msg.attach(MIMEText(content, "html", _charset="utf-8"))    
    smtp = smtplib.SMTP(email_setting["smtp_server"], 25)
    smtp.login(email_setting["sender_username"], email_setting["sender_password"])
    smtp.sendmail(email_setting["sender"], (email_setting["receiver"].split(";")) + (email_setting["cc"].split(";") if email_setting["cc"] is not None else []), msg.as_string())
    smtp.quit()
