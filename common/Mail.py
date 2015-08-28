#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

SMTP_QQ = "smtp.qq.com"
SMTP_163 = "smtp.163.com"
SMTP_gmail = "smtp.gmail.com"
SMTP_126 = "smtp.126.com"

def getSMTP(userName):
    if "qq" in userName:
        return SMTP_QQ
    if "163" in userName:
        return SMTP_163
    if "gmail" in userName:
        return SMTP_gmail
    if "126" in userName:
        return SMTP_126

class Email_Test_Sender:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def sendMsg(self, to, subject, text):
        # 组织邮件主体
        msg = MIMEText(text, _subtype='html', _charset='UTF-8')
        msg["Subject"] = subject
        msg["From"] = self.userName
        msg["To"] = to

        print u"开始发送邮件"
        print self.userName, " >>>> " + to
        print u"邮件主题：", subject
        print u"邮件内容：", text

        # 获取邮箱对应的SMTP
        smtp = getSMTP(self.userName)

        # 发送邮件
        s = smtplib.SMTP(smtp, timeout=30, port=25)
        s.login(self.userName, self.password)
        s.sendmail(self.userName, to, msg.as_string())
        s.close()


def test_send_text():
    userName = "lcw2004@163.com"
    pwd = "2g1JLXI6lQ"
    toQQ = "292232611@qq.com"
    text = """邮件内容"""

    sender = Email_Test_Sender(userName, pwd)
    sender.sendMsg(toQQ, "呵呵", text)

# test_send_text()