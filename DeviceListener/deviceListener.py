from pubnub import Pubnub
class PubNub:
	
	def __init__(self,pubkey,subkey):
		self.pubchannel = "core-ops"
		self.subchannel = "dev-listn"

		self.pubnub = Pubnub(publish_key=pubkey, subscribe_key=subkey)

		pass

	def subCallback(self,message,channel):
		print (message,channel)
		if (channel == self.subchannel):
				self.pub(message,self.pubchannel)

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


if __name__ == '__main__':
	
	pubkey = 'pub-c-b04e36e4-5535-48f1-a969-c0a9fced6655'
	subkey = 'sub-c-0dc10f58-7466-11e8-98cb-067913ebee63'

	pb = PubNub(pubkey,subkey)
	subchannel = "dev-listn"
	pb.sub(subchannel)



	

