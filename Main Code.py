#Jake Eaton

import time
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
elif hnn == 2:
    hn = input("Please enter the number of the child's house. ")
    hs = input("Please enter the street of the child's house. ")
    loc = input("Please enter the town, village or city ")
    pc = input ("Please enter the Postcode of the child. ")
    hpn = input("Please enter the child's Home Number. ")    
    print("Thank you. Storing in your database now...")
    email = name + "." + lname + "@matrixcommand.ne.oh"
    writefile = open("students.csv","a")
    writefile.write(name + "," + lname + "," + dob + "," + gender + "," + hna + "," + hs + "," + loc + "," + pc + "," + email + "," + uid + "," + hpn + "," +"\n")
    writefile.close()
    time.sleep(1)
    print("Saved!")
