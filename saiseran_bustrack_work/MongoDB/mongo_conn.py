#Program to receive tag data and push to MongoDB
import pymongo
from file_parser_mongo import *
from pymongo import *
import time
class mongo_db():


	def __init__(self):

		pass

		'''
		Takes "db"=database_name, "collection"=collectio_name 
		as input "args" and connects to database and
		given collection.
		'''
	def mongo_connect(self,db,collection):
		try:
			self.conn = MongoClient(host)
			print(self.conn)
			self.db = self.conn[db]
			self.db = self.db[collection]
						
			print('''

				 connected
			 	   to
		  	   	'Database'


			  		''')
			time.sleep(1)
		except Exception as e:
			print(e)

		'''
		Takes a input as json, dict and inserts
		it into the database
		'''
	def mongo_insert(self,info):
		try:
			print (self.db)
			data=info
			self.insert=self.db.insert_one(data)
			print(self.insert)
		except Exception as e:
			print(e)

	def mongo_insert_many(self,info):
		try:
			print(info)
			self.insert=self.db.insert_many(info)
			print(self.insert)
		except Exception as e:
			print(e)
	def mongo_find_and_replace(self,info):
		data = info
		print(data)
		try:
			self.replace=self.db.findOneAndReplace(data)
			print(self.replace)
		except Exception as e:
			print(e)

		'''
		This functin returns the timw stamp
		'''
	def mongo_find_specific(self,info):
		try:

			data=info
			self.find=self.db.find(data).sort(["_id", pymongo.ASCENDING])
			
			return self.find
		except Exception as e:
			print(e)


	def mongo_find(self):
		try:
			self.find=self.db.find()
			return self.find
			#print(self.find)
		except Exception as e:
			print(e)

	def time(self):
		self.a = time.localtime(time.time())
		self.t =[self.a.tm_hour]
		self.t.append(self.a.tm_min)
		self.t.append(self.a.tm_sec)
		self.v = ':'.join(str(e) for e in self.t)
		return self.v

	# def date(self):
	# 	self.date=self.db.insert_one({"date":new Date()})
		# self.a = time.localtime(time.time())
		# self.t =[self.a.tm_mday]
		# self.t.append(self.a.tm_mon)
		# self.t.append(self.a.tm_year)
		# self.v = '/'.join(str(e) for e in self.t)
		# return self.v

	#def random_put(self):


				# #create connection
				# try:
				# 	client = MongoClient()
				# 	print("Connection successfully!!")
				# except:
				# 	print("Connection failed!!")
				# #connect to ip and port 
				# client = MongoClient(host)
				# #Access database
				# # database
				# try:
				# 	db = client.sai
				# 	print("Connected to database")
				# except:
				# 	print("not connected")
				 
				# # Created or Switched to collection names: seran
				# collection = db.seran
				 
				# emp_rec1 = {
				#         "name":"Mr.Geek",
				#         "eid":24,
				#         "location":"delhi"
				#         }
				# emp_rec2 = {
				#         "name":"Mr.Shaurya",
				#         "eid":14,
				#         "location":"delhi"
				#         }
				 
				# # Insert Data
				# rec_id1 = collection.insert_one(emp_rec1)
				# rec_id2 = collection.insert_one(emp_rec2)
				 
				# print("Data inserted with record ids",rec_id1," ",rec_id2)
				 
				# # Printing the data inserted
				# cursor = collection.find()
				# for record in cursor:
				#     print(record)
