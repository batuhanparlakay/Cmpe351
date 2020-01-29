import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Estate"]
mycol = mydb["House"]

mylist = [
  { "name": "Parıs", "address": "Apple st 652","sale":0,"price":30000},
  { "name": "Chiago", "address": "Mountain 21","sale":1,"price":40000},
  { "name": "Frankurt", "address": "Valley 345","sale":0,"price":50000},
  { "name": "Washington", "address": "Ocean blvd 2","sale":1,"price":60000},
  { "name": "Washington", "address": "Green Grass 1","sale":1,"price":70000},
  { "name": "Washington", "address": "Sky st 331","sale":0,"price":80000},
  { "name": "Toronto", "address": "One way 98","sale":1,"price":90000},
  { "name": "Los Angeles", "address": "Yellow Garden 2","sale":0,"price":20000},
  { "name": "Houston", "address": "Park Lane 38","sale":1,"price":35000},
  { "name": "Washington", "address": "Central st 954","sale":0,"price":45000},
  { "name": "Dallas", "address": "Main Road 989","sale":1,"price":85000},
  { "name": "Phoenix", "address": "Sideway 1633","sale":0,"price":42000},
]

x = mycol.insert_many(mylist)


myquery = { "city": "Washington","sale":1 }

mydoc = mycol.find(myquery)

myvalues = []

def sale(num):
    return num*0.9

for y in mydoc:
    new = { "$set": { "price": sale(y["price"]) } }
    y.update_one(myquery,new)
    
    


