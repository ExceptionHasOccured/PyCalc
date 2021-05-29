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
    db.users.insert_one({"name": uName, "UID": str(uId)})
    print("Account created")
    print("Your username will be: " + uName)
    print("Your uid will be: " + str(uId))
    quit()
elif i == "3":
    uName = "_demo"
    uId = "000000"

def submit_equation(eid, op, num1, num2, ans):
    db.history.insert_one({"UID":uId,"EID":eid,"num1":num1,"num2":num2,"op":op,"ans":ans})

while True:
    i = input(uName + "@PyCalc $ ")
    args = i.split()
    if args[0] == "calc":
        if len(args) == 4:
            if args[2] == "+" or args[2] == "-add":
                a = int(args[1]) + int(args[3])
                eRand = random.randint(1000000000,9999999999)
                submit_equation(eRand, "add", args[1], args[3], a)
                print("Equation Solved")
                print("Answer: " + str(a))
                print("Equation ID: " + str(eRand))
            elif args[2] == "-" or args[2] == "-sub":
                a = int(args[1]) - int(args[3])
                eRand = random.randint(1000000000,9999999999)
                submit_equation(eRand, "subtract", args[1], args[3], a)
                print("Equation Solved")
                print("Answer: " + str(a))
                print("Equation ID: " + str(eRand))
            elif args[2] == "*" or args[2] == "x" or args[2] == "-mlt":
                a = int(args[1]) * int(args[3])
                eRand = random.randint(1000000000,9999999999)
                submit_equation(eRand, "multiply", args[1], args[3], a)
                print("Equation Solved")
                print("Answer: " + str(a))
                print("Equation ID: " + str(eRand))
            elif args[2] == "/" or args[2] == "-div":
                a = int(args[1]) / int(args[3])
                eRand = random.randint(1000000000,9999999999)
                submit_equation(eRand, "divide", args[1], args[3], a)
                print("Equation Solved")
                print("Answer: " + str(a))
                print("Equation ID: " + str(eRand))
            else:
                print("Invalid syntax")
        else:
            print("Invalid syntax")
    elif args[0] == "get":
        if len(args) == 2:
            if args[1] == "-eq":
                x = db.history.find_one({"EID": int(args[2])})
                print("Equation ID: " + str(x["EID"]))
                print("User ID: " + x["UID"])
                print("First Number: " + str(x["num1"]))
                print("Second Number: " + str(x["num2"]))
                print("Operation: " + x["op"])
                print("Answer: " + str(x["ans"]))
            elif args[1] == "-user":
                # find user by UID
        else:
            print("Invalid syntax")
 