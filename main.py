import pymongo

client = pymongo.MongoClient("mongodb+srv://scrat:K5yUw2AWTTlH5ZHX@cluster0.tufcd.mongodb.net/myFirstDatabase"
                             "?retryWrites=true&w=majority")
db = client.pycalc
