import smtplib

sendermail = 'xxxxxx@gmail.com'
senderpassword= 'xxxxxxx'
receviermail ='x.xx@gmail.com'
subject = "xxxx"

s= smtplib.SMTP("smtp.gmail.com" ,587)
s.starttls()
s.login(sendermail,senderpassword)
s.sendmail(sendermail,receviermail,subject)
s.quit()
