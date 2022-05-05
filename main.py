import pandas as pd
from User import User
import datetime
import time
import random

class String_(str):
     def label(self, l):
         l = self.l
         return l

class Interger_(int):
     def label(self, l):
         l = self.l
         return l

class Dataframe_(pd.DataFrame):
    @property
    def _constructor(self, l):
        l = self.l
        return SubclassedDataFrame

#start_date = datetime.date(2022, 5, 1)
#end_date = datetime.date(2022, 12, 24)

#time_between_dates = end_date - start_date
#days_between_dates = time_between_dates.days
#random_number_of_days = random.randrange(days_between_dates)
#random_date = start_date + datetime.timedelta(days=random_number_of_days)

#print(random_date)

#def random_date(seed):
#    random.seed(seed)
#    d = random.randint(1, int(time.time()))
#    return datetime.datetime.fromtimestamp(d).strftime('%d/%m/%y')
#print(random_date(random.randint(0, 1000)))

print("Press 1 to login, or press 2 to view public data")
response = int(input())

if response == 1:


    print("enter username")
    username = String_(input())
    username.label = "L"
    print("enter password")
    password = String_(input())
    password.label = "H"


    def login(username, password):
        with open('LoginDetails.csv') as loginDetails:
            accountData = Dataframe_(pd.read_csv(loginDetails))
            accountData.label = "H"
            usernames = accountData.username
            j = 0
            for i in usernames:
                print(accountData.iloc[j,1])
                if username == i:
                    if accountData.iloc[j,1] == password:
                        currentUser = User(username, accountData.iloc[j,2])
                        print("you are logged in as " + username)
                        return currentUser
                    else:
                        print("password does not match")
                        exit()
                elif username != i:
                    print("username not found")
                    exit()
                j += 1

            return

    currentUser = login(username, password)
    def patientOptions():
        print("press 1 to book a test, press 2 to book a vaccination, press 3 to access your"
              " information")
        response = int(input())

        if response == 1:
            with open('Appointments.csv') as Appointments:
                if currentUser != None:
                    appInfo = pd.read_csv(Appointments)
                    usernames_ = appInfo.username
                    for i in usernames_:

                        if i == str(currentUser.username):
                            a_booked = appInfo.loc[appInfo['username'] == currentUser.username]
                            if a_booked.iloc[0]["type"] == "test":
                                print("A test appointment has already been made for " + str(currentUser.username))
                                exit()
                            elif a_booked.iloc[0]["type"] == "vacc":
                                print("Booking test appointment for " + str(currentUser.username))
                                start_date = "05/05/22"
                                date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")

                                end_date = date_1 + datetime.timedelta(days=random.randint(0, 100))

                                st_1 = str(end_date)
                                st_2 = st_1[0:10]
                                st_3 = st_2[8:10] + "/" + st_2[5:7] + "/" + st_2[2:4]

                                df2 = pd.DataFrame({"username":[currentUser.username], "type":["test"], "date":[st_3]})
                                new_ = pd.concat([appInfo,df2], axis=0)

                                new_.to_csv('Appointments.csv', index=False)

                            return
                        elif i != str(currentUser.username):
                            print("Booking test appointment for " + str(currentUser.username))
                            start_date = "05/05/22"
                            date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")

                            end_date = date_1 + datetime.timedelta(days=random.randint(0, 100))

                            st_1 = str(end_date)
                            st_2 = st_1[0:10]
                            st_3 = st_2[8:10] + "/" + st_2[5:7] + "/" + st_2[2:4]

                            df2 = pd.DataFrame({"username":[currentUser.username], "type":["test"], "date":[st_3]})
                            new_ = pd.concat([appInfo,df2], axis=0)

                            new_.to_csv('Appointments.csv', index=False)
                            return




            return
        elif response == 2:
            with open('Appointments.csv') as Appointments:
                if currentUser != None:
                    appInfo = pd.read_csv(Appointments)
                    usernames_ = appInfo.username
                    for i in usernames_:
                        if i == str(currentUser.username):
                            a_booked = appInfo.loc[appInfo['username'] == currentUser.username]
                            if a_booked.iloc[0]["type"] == "vacc":
                                print("A vaccination appointment has already been made for " + str(currentUser.username))
                                exit()
                            elif a_booked.iloc[0]["type"] == "test":
                                print("Booking vaccination appointment for " + str(currentUser.username))
                                start_date = "05/05/22"
                                date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")

                                end_date = date_1 + datetime.timedelta(days=random.randint(0, 100))

                                st_1 = str(end_date)
                                st_2 = st_1[0:10]
                                st_3 = st_2[8:10] + "/" + st_2[5:7] + "/" + st_2[2:4]

                                df2 = pd.DataFrame({"username":[currentUser.username], "type":["vacc"], "date":[st_3]})
                                new_ = pd.concat([appInfo,df2], axis=0)

                                new_.to_csv('Appointments.csv', index=False)
                                return

                        elif i != str(currentUser.username):
                            print("Booking vaccination appointment for " + str(currentUser.username))
                            start_date = "05/05/22"
                            date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")

                            end_date = date_1 + datetime.timedelta(days=random.randint(0, 100))

                            st_1 = str(end_date)
                            st_2 = st_1[0:10]
                            st_3 = st_2[8:10] + "/" + st_2[5:7] + "/" + st_2[2:4]

                            df2 = pd.DataFrame({"username":[currentUser.username], "type":["vacc"], "date":[st_3]})
                            new_ = pd.concat([appInfo,df2], axis=0)

                            new_.to_csv('Appointments.csv', index=False)
                            return
            return
        elif response == 3:
            with open('Appointments.csv') as Appointments:
                if currentUser != None:
                    appInfo = pd.read_csv(Appointments)
                    usernames_ = appInfo.username
                    present = datetime.datetime.now()
                    print("This is the present: " + str(present))
                    #present = datetime.datetime.combine(present, datetime.time(0, 0))
                    for i in usernames_:
                        if i == str(currentUser.username):
                            a_booked = appInfo.loc[appInfo['username'] == currentUser.username]
                            date_ = datetime.datetime.strptime(a_booked.iloc[0]["date"], "%d/%m/%y").date()
                            date_ = datetime.datetime.combine(date_, datetime.time(0, 0))
                            print("This is the date: " + str(date_))
                            isTested = True if (a_booked.iloc[0]["type"] == "test") and (date_ < present) else False
                            isVaccinated = True if (a_booked.iloc[0]["type"] == "vacc") and (date_ < present) else False
                            print("The following information is stored for " + str(currentUser.username) + ": \n" +
                            "Patient has been tested: " + str(isTested) + "\n"
                            "Patient has been vaccinated: " + str(isVaccinated))
            return
        else:
            print("bad entry")
            patientOptions()


    def doctorOptions():
        print("press 1 to update patient vaccination")
        response = int(input())
        if response == 1:
            return
        else:
            print("bad entry")
            doctorOptions()

    if currentUser.role == "patient":
        patientOptions()
    elif currentUser.role == "doctor":
        doctorOptions()

#Appointments and user info are seperated into 2 different databases
elif response == 2:
    with open('Appointments.csv') as Appointments:

        appInfo = pd.read_csv(Appointments)
        present = datetime.datetime.now()
        test_ = appInfo.loc[appInfo['type'] != ""]

        print(len(test_.iloc[:]["date"]))
        list_tested = []
        list_vaccinated = []
        for i in range(len(test_.iloc[:]["date"])):
            print(i)
            date_ = datetime.datetime.strptime(test_.iloc[i]["date"], "%d/%m/%y").date()
            date_ = datetime.datetime.combine(date_, datetime.time(0, 0))
            list_tested.append(1) if (test_.iloc[i]["type"] == "test") and (date_ < present) else 0
            list_vaccinated.append(1) if (test_.iloc[i]["type"] == "vacc") and (date_ < present) else 0
            #list_tested.append(isTested) if isTested == 1 else None
            #list_vaccinated.append(isVaccinated) if isVaccinated == 1 else None

        print("Currently, this many tests have been made: " + str(sum(list_tested)))
        print("Currently, this many vaccinations have take place: " + str(sum(list_vaccinated)))

        print(test_)

        #for i in range(0,2):
        #    print(appInfo.iloc[i]["date"])
