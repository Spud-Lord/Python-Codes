#Jake Eaton

import time
username = "J.Leeman"
password = "Mr J.Leeman"
un = input("Please enter your username. ")
if un == "J.Leeman":
    print("Username Accepted")
    pw = input("Please Enter your Password. ")
else:
    print("Incorrect.")
if pw == "Mr J.Leeman":
        print("Mr James Leeman")
        time.sleep(0.5)
        print("Welcome back!")
        print("So pleased to hear from you again.")
elif pw != "Mr J.Leeman":
    print("Password Incorrect")
    print("Shutting Down System... ")
    time.sleep(1.5)
