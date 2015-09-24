# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib

__author__ = 'Matthieu Gallet'


def main():
    from_email = 'administrator@test.example.org'
    to_email = from_email
    hostname = 'mail01.test.example.org'
    login = 'administrator'
    password = 'toto'

    smtp = smtplib.SMTP(hostname, 25)
    smtp.set_debuglevel(1)
    smtp.starttls()
    smtp.sendmail(from_email, [to_email], 'test message')

    smtp = smtplib.SMTP(hostname, 587)
    smtp.set_debuglevel(0)
    smtp.starttls()
    smtp.login(login, password)
    smtp.sendmail(from_email, [to_email], 'test message')

    smtp = smtplib.SMTP_SSL(hostname, 465)
    smtp.set_debuglevel(0)
    smtp.login(login, password)
    smtp.sendmail(from_email, [to_email], 'test message')


if __name__ == '__main__':
    main()
