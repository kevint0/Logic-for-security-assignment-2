import pandas as pd
from User import User

class String_(str):
     def label(self, l):
         l = self.l
         return l

class Interger_(int):
     def label(self, l):
         l = self.l
         return l


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
            accountData = pd.read_csv(loginDetails)
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
                        else:
                            print("Booking test appointment for " + str(currentUser.username))

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
                        else:
                            print("Booking vaccination appointment for " + str(currentUser.username))
            return
        elif response == 3:
            with open('Appointments.csv') as Appointments:
                if currentUser != None:
                    appInfo = pd.read_csv(Appointments)
                    usernames_ = appInfo.username
                    for i in usernames_:
                        if i == str(currentUser.username):
                            a_booked = appInfo.loc[appInfo['username'] == currentUser.username]
                            print("The following information is stored for " + str(currentUser.username) + ": \n" +
                            "")
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

elif response == 2:
    print("NOT IMPLEMENTED")
