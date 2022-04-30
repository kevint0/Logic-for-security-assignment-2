import pandas as pd

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
                    print("you are logged in as " + username)
                    return username
                else:
                    print("password does not match")
                    return "null"
            j += 1
        print("username not found")
        return "null"

login(username, password)