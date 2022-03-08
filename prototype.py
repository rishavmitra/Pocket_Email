import smtplib
from email.message import EmailMessage


def body():
    text = []
    while True:
        a = input()
        if a == '.':
            break
        else:
            text.append(a)
    actual_message = "\n".join(text)
    return actual_message


def message_input():
    mes = EmailMessage()
    mes['Subject'] = input('Subject\n************************\n')
    print('Body\n************************\n')
    body_message = body()
    mes.set_content(body_message)
    send_message(mes)


def send_message(mes):
    smtp.sendmail(us_em, to_em, mes.as_string())


smtp = smtplib.SMTP(host='smtp.gmail.com', port='587')

smtp.ehlo()
smtp.starttls()

us_em = input("Enter you Email")
us_pss = input("Enter password")

to_em = input("To:")

smtp.login(us_em, us_pss)

message_input()

smtp.quit()
################################## To do##################################################################
############################# Use the email module to construct the subject of the email##################
