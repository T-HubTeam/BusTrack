from pubnub import Pubnub
class PubNub:
	def __init__(self,pubkey,subkey):
		self.pubnub = Pubnub(publish_key=pubkey, subscribe_key=subkey)
		self.subchannel = 'core-ops'
	def subCallback(self,message,channel):
		print (message,channel)

		if (channel == self.subchannel):
				return message

	def error(self,message):
		print (message)

	def pubCallback(self,message):
		print (message)


	def pub(self,message,channel):
		try:
			self.pubnub.publish(channel, message, callback=self.pubCallback, error=self.pubCallback)	
		except Exception as e:
			print (e)

	def sub(self,channel):
		try:
			self.pubnub.subscribe(channels=channel, callback=self.subCallback, error=self.error)		
		except Exception as e:
			print (e)


class dataPush():
	''' here we have to decide whether entry insert or update(i.e., bus entering/exiting for the first time of the day or entering/exiting second/third.... time of the day)'''
	def __init__(self):
		pubkey = 'pub-c-b04e36e4-5535-48f1-a969-c0a9fced6655'
		subkey = 'sub-c-0dc10f58-7466-11e8-98cb-067913ebee63'

		self.pb = PubNub(pubkey,subkey)
		subchannel = "core-ops"
		self.verify()
		
	def verify(self,):	
		self.msg = pb.sub(subchannel)


		pass

	def callInsert(self,):
		pass

	def callUpdate(self,):
		pass	





class dataPull():
	'''WE WILL DO IT LATER'''
	pass	




'''

	CORE OPERATONS  - 1) DATA PUSH
							INSERT
							UPDATE

					2) DATA PULL
						2.1) DAY WISE DATA
						2.2) BUS WISE DATA



'''
