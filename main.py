import pymongo
import random

client = pymongo.MongoClient("mongodb+srv://scrat:K5yUw2AWTTlH5ZHX@cluster0.tufcd.mongodb.net/myFirstDatabase"
                             "?retryWrites=true&w=majority")
db = client.pycalc

print("1 - Log in")
print("2 - Sign up")
print("3 - Use _demo")
i = input("> ")
print(i)

if i == "1":
    uName = input("Enter your username: ")
    uId = input("Enter your uid: ")
    x = db.users.find_one({"name": uName})
    if x["UID"] == uId:
        print("Auth successfull")
    else:
        print("Auth failed")
        quit()
elif i == "2":
    print("Let's create your account :)")
    uName = input("Enter your username: ")
    uId = random.randint(100000,999999)
    db.users.insert_one({"name": uName, "UID": uId})
    print("Account created")
    print("Your username will be: " + uName)
    print("Your uid will be: " str(uId))
elif i == "3":
    uName = "_demo"
    uId = 000000

while true:
    i = input(uName + "@PyCalc $ ")
    