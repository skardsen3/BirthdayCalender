import pandas as pd

fileLocation = r'C:\Users\Ashton\PycharmProjects\Calender\birthdays.csv'
datefileLocation = r'C:\Users\Ashton\PycharmProjects\Calender\lastrun.csv'

birthday_Date = {
    'Birthday': [],
    'Person': [],
    'Relation': [],
    'Contact': []
}
birthdays = pd.DataFrame(birthday_Date, columns=['Birthday', 'Person', 'Relation', 'Contact'])



def addBirthday(Birthday, Person, Relation, Contact):
    newBirthdayId = Birthday + Person

    currentBirthdays = pd.read_csv(fileLocation)
    currentBirthdays['id'] = currentBirthdays['Birthday'] + currentBirthdays['Person']

    if newBirthdayId in currentBirthdays['id'].to_list():
        print('Someone with the same name and birthday is already saved')
    else:
        newBirthdayList = [[Birthday, Person, Relation, Contact]]
        newBirthday = pd.DataFrame(newBirthdayList, columns=['Birthday', 'Person', 'Relation', 'Contact'])
        newBirthday.to_csv(fileLocation, mode='a', index=False, header=False)


#addBirthday('23/11/2003','Someone','Idk',' ')