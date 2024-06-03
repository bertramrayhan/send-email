import smtplib
import os

username = input('Username: ')
password = input('Password: ')
print(password)

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()
smtp_server.starttls()
smtp_server.ehlo()

smtp_server.login(username, password)

msg = '''
halo
ini test pertama
bisa gak ya
'''

smtp_server.sendmail(username, 'forminecraft1357@gmail.com', msg)
print('berhasil')

smtp_server.quit()