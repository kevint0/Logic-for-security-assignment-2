import pandas as pd
from User import User

print("enter login")
username = input()
print("enter password")
password = input()

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
                    return
            j += 1
        print("username not found")
        return

currentUser = login(username, password)
def patientOptions():
    print("press 1 to book appointment, press 2 to book test, press 3 to book a vaccination, press 4 to access you"
          " information")
    response = int(input())
    if response == 1:
        return
    elif response == 2:
        return
    elif response == 3:
        return
    elif response == 4:
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