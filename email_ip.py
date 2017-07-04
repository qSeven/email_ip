import configparser
import time
from urllib import request

import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailWrapper:
    def __init__(self, config_file):
        config_reader = configparser.ConfigParser()
        config_reader.read(config_file)
        self._sender_email = config_reader.get('email','sender')
        self._send_password = config_reader.get('email','password')
        self._subject = config_reader.get('email','subject')
        self._append_ip_to_subject = config_reader.getboolean('email','AppendIPtoSubject')
        self._recive_list = []
        for key in config_reader['recievers']:
            self._recive_list.append(config_reader.get('recievers',key))
        print(self._recive_list)

    def send(self, ip):

        to = self._recive_list  

        subject =self._subject
        if self._append_ip_to_subject:
            subject = subject + str(ip)

        msg = MIMEMultipart()
        msg['From'] = self._sender_email
        msg['Subject'] = subject
        msg.attach(MIMEText('New IP: ' + str(ip)))


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self._sender_email, self._send_password)
        server.sendmail(self._sender_email, to, msg.as_string())
        server.close()

if __name__ == '__main__':
    ew = EmailWrapper('default.cfg')
    ip = 0
    while True:
        time.sleep(2)
        #get ip
        ip_new = request.urlopen('http://ip.42.pl/raw').read()
        #check ip?
        if ip != ip_new:
            ew.send(ip_new)
            ip = ip_new
            print('new ip')
        else:
            print('no new ip')
