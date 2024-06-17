import smtplib
from email.message import EmailMessage
import ssl
import requests


#for email automation system credits to https://www.youtube.com/watch?v=g_j6ILT-X0k


reciever = ''
quote_url = 'https://api.api-ninjas.com/v1/quotes?category=happiness'
sender = 'YOUR GMAIL'
email_pass = 'PASSWORD GIVEN FROM GMAIL 2FA'
subject = 'Weather Data!'


decider = input('Phone or Email? ')


decider = decider.lower()




if decider == 'phone':
   number = input('enter phone number  ')
   carrier = input("TMobile,AT&T, or Verizon? ")
   carrier.lower()
   if carrier == 'tmobile':
       reciever = number+'@tmomail.net'
   elif carrier == 'at&t':
       reciever = number+'@txt.att.net'
   elif carrier == 'verizon':
       reciever == number+'@vtext.com'


if decider == 'email':
   email = input('Enter email address  ')
   reciever = email
          


place = input('Location  ')
quote = requests.get(quote_url, headers={'X-Api-Key': 'YOUR API KEY YOU USE'})
weather = requests.get('http://api.weatherapi.com/v1/current.json?key=YOUR API KEY={}&aqi=no'.format(place))


fin = quote.json()
quote_fin = fin[0]['quote']




current = weather.json()["current"]["temp_f"]
location = weather.json()["location"]["name"]
current = str(current)




body = 'It is currently '+current+' degrees in '+location+' This is an automation program in python for weather by Anish!'+' Here is the quote of the day! '+quote_fin




em = EmailMessage()
em['From'] = sender
em['To'] = reciever
em['Subject'] = subject


em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
   smtp.login(sender,email_pass)
   smtp.sendmail(sender, reciever, em.as_string() )
   print(reciever)

