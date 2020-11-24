from datetime import datetime
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from passwords import email_address, email_password, email_reciever




fileLocation = r'C:\Users\Ashton\PycharmProjects\Calender\birthdays.csv'
datefileLocation = r'C:\Users\Ashton\PycharmProjects\Calender\lastrun.csv'

birthday_Date = {
    'Birthday': [],
    'Person': [],
    'Relation': [],
    'Contact': []
}
birthdays = pd.DataFrame(birthday_Date, columns=['Birthday', 'Person', 'Relation', 'Contact'])


def createCSV():
    birthdays.to_csv(fileLocation, index=False, header=True)
    print('Created CSV')



class birthday:
    def __init__(self, Birthday, Person, Relation, Contact):
        self.Birthday = Birthday
        self.Person = Person
        self.Relation = Relation
        self.Contract = Contact


def dailyCheck():
    today = datetime.today().strftime('%d-%m')
    todayFull = datetime.today().strftime('%d-%m-%Y')
    lastRunDate = pd.read_csv(datefileLocation, parse_dates=["LastRun"])
    lastRunDate = pd.to_datetime(lastRunDate.LastRun.values[0]).strftime('%d-%m')
    currentBirthdays = pd.read_csv(fileLocation)

    todayCsv = {'LastRun': [todayFull]}
    todayCsv = pd.DataFrame(todayCsv, columns=['LastRun'])



    if lastRunDate == today:
        print("Already ran today")
    else:
        print("Running...")
        todayCsv.to_csv(datefileLocation, index=True, header=True)

        for index, row in currentBirthdays.iterrows():
            try:
                datetimeBirthday = datetime.strptime(row['Birthday'], '%d-%m-%Y').strftime('%d-%m')
                if today == datetimeBirthday:
                    birthdayReminder(row['Birthday'], row['Person'], row['Relation'], row['Contact'])
            except ValueError:
                try:
                    datetimeBirthday = datetime.strptime(row['Birthday'], '%d/%m/%Y').strftime('%d-%m')
                    if today == datetimeBirthday:
                        birthdayReminder(row['Birthday'], row['Person'], row['Relation'], row['Contact'])
                except ValueError:
                    print('Birthday format for ', row['Person'], ' not acceptable. Please use DD/MM/YYYY', sep='')



def birthdayReminder(Birthday, Person, Relation, Contact):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email_address, email_password)

    text = ('Hi its '+str(Person)+' birthday today ('+str(Birthday)+'). Your '+str(Relation)+'. Flick them a message to say hi on '+str(Contact))
    
    msg = MIMEText(text, 'html')
    msg['Subject'] = 'Its'+str(Person)+'s birthday!'
    msg['From'] = 'Birthday Reminders <'+email_address+'>'
    msg['To'] = email_reciever

    smtpObj.sendmail(email_address, email_reciever, msg.as_string())
    smtpObj.quit()
    print('Sent')



if __name__ == "__main__":
    dailyCheck()


