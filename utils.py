import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(data, fromaddr, toaddr_list):
    body = data
    msg = MIMEMultipart()
    msg['From'] = f"WebScraping Workshop <{fromaddr}>"
    msg['To'] = ", ".join(toaddr_list)
    msg['Subject'] = "Pyscho x.x"
    message = msg.as_string()

def main():
    data = "Hello, this is a test email from the WebScraping Workshop"
    to = ['']
    sendMail(data, "example@gmail.com", to)
    
    
if __name__ == "__main__":
    main()
