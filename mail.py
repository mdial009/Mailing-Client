import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#stmp server for gmail would have to change for others email cilents 
server = smtplib.SMTP("smtp.gmail.com", 587)

# function to call server
server.starttls()

name = "Madany Diallo"
myemailadress = "magicturtle1998@gmail.com"
toemailaddress = "madanyx@gmail.com"

with open("password.txt", "r") as f:
    password = f.read()

server.login(myemailadress, password)

msg = MIMEMultipart()
msg["From"] = name
msg["To"] = toemailaddress
msg["Subject"] = "Just A Test"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

# The file name for the file you want to attach and send. make sure its in same diretory
filename = ""
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Dispostion", f"attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail(myemailadress,
                toemailaddress, text)
