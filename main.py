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


def eu_data():
    with open('Appointments.csv') as Appointments:
        appInfo = pd.read_csv(Appointments)
        present = datetime.datetime.now()
        a_booked = appInfo.loc[(appInfo['type'] == "test")]

        for i in a_booked.values:
            date_ = datetime.datetime.strptime(i[2], "%d/%m/%y").date()
            date_ = datetime.datetime.combine(date_, datetime.time(0, 0))
            if date_ < present:
                with open('eu_database.csv') as Data_:
                    dataInfo = pd.read_csv(Data_)
                    res_ = random.randint(0,1)
                    df2 = pd.DataFrame({"id":[i[0]], "type":["test"], "result":[res_]})
                    new_ = pd.concat([dataInfo,df2], axis=0)

                    new_.to_csv('eu_database.csv', index=False)

        return


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
            print(usernames)
            j = 0
            for i in usernames:

                print(accountData.iloc[j]["password"])
                if username == i:
                    if accountData.iloc[j]["password"] == password:
                        currentUser = User(username, accountData.iloc[j]["role"])
                        print("you are logged in as " + username)
                        j += 1
                        return currentUser
                    else:
                        print("password does not match")

                elif username != i:

                    j += 1

                #j += 1

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
                    name_list = []
                    for i in usernames_:
                        name_list.append(i)



                    if currentUser.username in name_list:
                        a_booked = appInfo.loc[appInfo['username'] == currentUser.username]
                        if "test" in a_booked.values:
                            print("A test appointment has already been made for " + str(currentUser.username))

                        elif "vacc" in a_booked.values:
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
                    elif currentUser.username not in name_list:
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
                    name_list = []
                    for i in usernames_:
                        name_list.append(i)
                    print(name_list)


                    if currentUser.username in name_list:
    
                        a_booked = appInfo.loc[appInfo['username'] == currentUser.username]

                        if "vacc" in a_booked.values:

                            print("A vaccination appointment has already been made for " + str(currentUser.username))

                        elif "test" in a_booked.values:

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

                    elif currentUser.username not in name_list:
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
                with open('eu_database.csv') as eu:
                    if currentUser != None:
                        appInfo = pd.read_csv(Appointments)
                        eu_data = pd.read_csv(eu)
                        usernames_ = eu_data.id
                        present = datetime.datetime.now()
                        print(usernames_)
                        print("This is the present: " + str(present))
                        #present = datetime.datetime.combine(present, datetime.time(0, 0))

                        if str(currentUser.username) in usernames_.values:


                            user_status = eu_data.loc[eu_data['id'] == currentUser.username]
                            val_ = user_status.values
                            a_booked = appInfo.loc[appInfo['username'] == currentUser.username]

                            date_ = datetime.datetime.strptime(a_booked.iloc[0]["date"], "%d/%m/%y").date()
                            date_ = datetime.datetime.combine(date_, datetime.time(0, 0))

                            isTested = True if (a_booked.iloc[0]["type"] == "test") and (date_ < present) else False
                            isVaccinated = True if (a_booked.iloc[0]["type"] == "vacc") and (date_ < present) else False
                            testResult = "Positive" if val_[0][2] == 1 else "Negative"
                            print("The following information is stored for " + str(currentUser.username) + ": \n" +
                            "Patient has been tested: " + str(isTested) + " The result is: " +  testResult + "\n"
                            "Patient has been vaccinated: " + str(isVaccinated))
                        else:
                            print("This patient has no data")
                            return
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

        #print(len(test_.iloc[:]["date"]))
        list_tested = []
        list_vaccinated = []
        for i in range(len(test_.iloc[:]["date"])):
            #print(i)
            date_ = datetime.datetime.strptime(test_.iloc[i]["date"], "%d/%m/%y").date()
            date_ = datetime.datetime.combine(date_, datetime.time(0, 0))
            list_tested.append(1) if (test_.iloc[i]["type"] == "test") and (date_ < present) else 0
            list_vaccinated.append(1) if (test_.iloc[i]["type"] == "vacc") and (date_ < present) else 0
            #list_tested.append(isTested) if isTested == 1 else None
            #list_vaccinated.append(isVaccinated) if isVaccinated == 1 else None

        print("Currently, this many tests have been made: " + str(sum(list_tested)))
        print("Currently, this many vaccinations have take place: " + str(sum(list_vaccinated)))



        #for i in range(0,2):
        #    print(appInfo.iloc[i]["date"])

elif response == 3:
    eu_data()
