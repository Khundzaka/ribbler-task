import datetime
from pymongo import MongoClient

conn = MongoClient()

# tests
# print list(conn["challenge"]["events"].find())
# print time.strftime("%B %d %Y", "1452376800000")

csvdata = open("csvs/persons.csv", "r")

k = csvdata.read().split("\n")
dt = k[0]
print dt
k = k[1:-1]
print k

#parsing CSV file
dictlist = []
for i in k:
    print i
    d = i.split(",")
    print d
    dateformat = "%d/%m/%Y"

    di = {"pid": d[0], "fname": d[1], "lname": d[2], "bdate": datetime.datetime.strptime(d[3], dateformat)}
    # di = {"pid":d[0], "catid":d[1]}
    dictlist.append(di)
print dictlist

# insert in database
# for i in dictlist:
#     conn["challenge"]["persons"].insert(i)