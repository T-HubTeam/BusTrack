import pymongo
from pymongo import MongoClient

'''
	saiseran_s
	Aaisha!4sai
'''


class mongoDB():
  def __init__(self,):
    self.conn = MongoClient('mongodb://saiseran_s:Aaisha!4sai@ds213229.mlab.com:13229/bus_track')
    self.db = self.conn['bus_track']
    self.db.authenticate('saiseran_s', 'Aaisha!4sai')
    self.coll = self.db['bus_Arv_Ext_Data']
    # self.db = self.db.bus_Arv_Ext_Data
    print self.coll
    self.findWithCondition()

  def findWithCondition(self,):

    # for document in myCollection.find():
    #   print(document) 

    key1   = 'tagID' 
    value1 = '5a4sd65fc32v1a9'
    key2   = 'timeStamp.Date'
    value2 = '2018-06-21'

    # {"$and":[{key1: value1}, {key2:value2}]}

    # result = self.db['bus_Arv_Ext_Data'].find_one()
    # for val in result:
    #   print val
    # for val in self.coll.find():
    #   print val


    post = {"author": "Mike","age":23}
    self.coll.insert_one(post)


# m = mongoDB()

databasename = 'bus_track'
database_user = 'saiseran_s'
database_pass = 'Aaisha!4sai'
collection_name = 'bus_Arv_Ext_Data'

connection = pymongo.MongoClient('mongodb://saiseran_s:Aaisha!4sai@ds213229.mlab.com:13229/bus_track')

# mongodb://saiseran_s:Aaisha!4sai@ds213229.mlab.com:13229/bus_track

db = connection['bus_track']
collection = db['bus_Arv_Ext_Data']


# post = {"author": "Mike","age":23}
# db[collection_name].insert_one(post)
# print "done"

result = collection.find()
for val in result:
    print val



'''
  {
    "tagID":"5a4sd65fc32v1a9",
    "timeStamp":
           {
              "Date":"2018-06-21",
              "Time":"13:42:52"
           }
}
'''

