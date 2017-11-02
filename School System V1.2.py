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
def repeat():
    menu = input("Type 1 to create a student, Type 2 to view a student, Type 3 to Log Out. ")
    if menu == "1":
        name = input("Please enter the child's First Name. ")
        lname = input("Please enter the child's Last Name. ")
        dob = input("Please enter the child's date of birth. ")
        gender = input("Please enter the child's Gender. ")
        uid = input("Please enter the child's Unique ID. ")
        hnn = int(input("Please type 1 to type in a house name or type 2 to type in a house number. "))
        if hnn == 1:
            hna = input ("Please enter the name of the child's house. ")
            hs = input("Please enter the street of the child's house. ")
            loc = input("Please enter the town, village or city. ")
            pc = input ("Please enter the Postcode of the child. ")
            hpn = input("Please enter the child's Home Number. ")
            print("Thank you. Storing in your database now...")
            email = name + "." + lname + "@matrixcommand.ne.oh"
            writefile = open("students.csv","a")
            writefile.write(name + "," + lname + "," + dob + "," + gender + "," + hna + "," + hs + "," + loc + "," + pc + "," + email + "," + uid + "," + hpn + "," +"\n")
            writefile.close()
            time.sleep(1)
            print("Saved!")
            repeat()
        elif hnn == 2:
            hn = input("Please enter the number of the child's house. ")
            hs = input("Please enter the street of the child's house. ")
            loc = input("Please enter the town, village or city ")
            pc = input ("Please enter the Postcode of the child. ")
            hpn = input("Please enter the child's Home Number. ")    
            print("Thank you. Storing in your database now...")
            email = name + "." + lname + "@matrixcommand.ne.oh"
            writefile = open("students.csv","a")
            writefile.write(name + "," + lname + "," + dob + "," + gender + "," + hn + "," + hs + "," + loc + "," + pc + "," + email + "," + uid + "," + hpn + "," +"\n")
            writefile.close()
            time.sleep(1)
            print("Saved!")
            repeat()
    if menu == "2":
        import csv
        import sys
        uid = input('Enter number to find\n')
        csv_file = csv.reader(open('students.csv', "r"), delimiter=",")
        for row in csv_file:
            if uid == row[9]:
                 print(row)
                 repeat()

    if menu == "3":
        logout = input("Would you like to log out? ")
        if logout == ('yes'):
            print("Logging out now.")
            time.sleep(2)
        if logout == ("no"):
            repeat()
repeat()
