import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
# 요일 설정
now = dt.datetime.now() 
day_of_week = now.weekday()

# 명언 
file_path = "./Day_032/quotes.txt"

with open(file_path) as f:
    lines = f.read().splitlines()
random_line = random.choice(lines)

sendEmail = ""
recvEmail = ""
password = ""

smtpName = "smtp.naver.com" #smtp 서버  주소
smtpPort = 587 #smtp 포트 번호

text = random_line
msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg['Subject'] ="명언을 보내드립니다."
msg['From'] = sendEmail
msg['To'] = recvEmail

if day_of_week == 1:
    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( sendEmail , password ) #로그인
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    s.close() #smtp 서버 연결을 종료합니다.


# 참고
# https://wikidocs.net/book/2965
