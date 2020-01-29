import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Market"]
mycol = mydb["Item"]

mylist = [
 {"item_name":"chips","item_brand":"lays","item_type":"snack","item_price":5,"item_quantity":100},
  {"item_name":"cheseeburger","item_brand":"mcdonalds","item_type":"food","item_price":4,"item_quantity":150},
   {"item_name":"cola","item_brand":"pepsi","item_type":"juice","item_price":4,"item_quantity":110},
    {"item_name":"milk","item_brand":"pýnar","item_type":"drink","item_price":2,"item_quantity":100},
     {"item_name":"apple","item_brand":"mcdonalds","item_type":"fruit","item_price":1,"item_quantity":420}]
x=mycol.insert_many(mylist)

def makediscount(fname,a):
    for cities in mycol.find({'item_brand':fname}, {'item_name', 'item_brand', 'item_type','item_price','item_quantity'}):
         where_query = {'_id':cities['_id'], 'item_brand':fname}
         update_query = {'$set':{'item_price':(cities["item_price"]- cities['item_price']*a)}}
         mycol.update_one(where_query, update_query)

class Basket:
      def add_basket(self,item_name,item_quantity):
          for kings in mycol.find({'item_name':item_name}, {'item_name', 'item_brand', 'item_type','item_price','item_quantity'}):
           where_query = {'_id':kings['_id'], 'item_name':item_name}
           update_query = {'$set':{'item_quantity':(kings['item_quantity']-item_quantity)}}
           mycol.update_one(where_query, update_query)
 

b=Basket()
makediscount("burgerking",0.1)
b.add_basket("chips",4)