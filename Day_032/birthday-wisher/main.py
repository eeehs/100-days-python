import csv
import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText

# create csv list 
csv_list = []

with open('./Day_032/birthday-wisher/birthdays.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    csv_list = list(reader)

# 오늘 날짜 설정

now = dt.datetime.now() 
month = now.month
day = now.day

# 생일자 찾기 
birth_name = ""
recvEmail = ""
for i in [1,2]:
    if csv_list[i][3] == str(month) and csv_list[i][4] == str(day):
        birth_name += csv_list[i][0]
        recvEmail += csv_list[i][1]

# letter 설정
text = ""
number = [1,2,3]
letter_number = random.choice(number)
letter_path = f'./Day_032/birthday-wisher/letter_templates/letter_{letter_number}.txt'

with open(letter_path) as f:
    lines = f.readlines()
    for i in lines:
        text += i 
text = text.replace("[NAME]" , birth_name)

# Email 설정

sendEmail = ""
password = ""

smtpName = "smtp.naver.com" #smtp 서버  주소
smtpPort = 587 #smtp 포트 번호

msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg['Subject'] ="생일축하합니다."
msg['From'] = sendEmail
msg['To'] = recvEmail

if len(birth_name) > 0:
    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( sendEmail , password ) #로그인
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.close() #smtp 서버 연결을 종료합니다.