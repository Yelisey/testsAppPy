# coding: utf-8

import smtplib
import random
from email.mime.multipart import MIMEMultipart


class EmailSender(object):

    def subject_generator(self):
        """
        Генератор темы письма
        :return:
        """
        words = ['IPA', 'Health Plan', 'ID', 'Claims Address', 'Group', 'Claim', 'Phone',
                 'Fax', 'Contact', 'AdjusterEmail', 'UtilReviewPhone', 'UtilReviewFax',
                 'Doctor', 'NPI', 'DateofInjury', 'BodyParts', 'BodyPartide', 'Gender',
                 'Diagnosis', 'Diagnosis', 'Procedure']

        domains = ["gmail.com", "ya.ru", "mail.ru", "yahoo.com",
                   "openslave.com", "yandex.ru", "hotmail.com",
                   "aol.com", "mail.com", "mail.kz"]

        random_word = words[random.randint(0, len(words) - 1)]
        random_domain = domains[random.randint(0, len(domains) - 1)]
        number = str(random.randint(0, 99999))
        subject = '{0}{1}{2}{3}'.format(random_word, number, '@', random_domain)
        return subject


    def mail_generator(self, count_of_mail, to_address):
        """
        Генератор писем
        :param count_of_mail: количество писем, которое нужно сгенерировать
        :param to_address: адрес, на который нужно отправить письма
        :return:
        """
        for i in range (0,count_of_mail):
            me = 'From: AutoMail'

            server = 'smtp.gmail.com' # Сервер отправитель
            port = 587 # возможные порты: 587, 465
            user_name = 'block.klaviaturenko@gmail.com' # Адрес отправителя
            user_passwd = 'Block1234' # Пароль отправителя

             # Формируем заголовок письма
            msg = MIMEMultipart('mixed')
            msg['Subject'] = self.subject_generator()
            msg['From'] = me
            msg['To'] = to_address

            # Подключение
            s = smtplib.SMTP(server, port)
            s.ehlo()
            s.starttls()
            s.ehlo()
            # Авторизация
            s.login(user_name, user_passwd)
            # Отправка пиьма
            s.sendmail(me, to_address, msg.as_string())
            s.quit()


    def send_emails(self, number_of_emails, to_address):
        """
        Отправка писем
        :param number_of_emails: количество писем, которые нужно сгенерировать
        :param to_address: адрес, на который нужно отправить письма
        :return:
        """
        self.mail_generator(number_of_emails, to_address)