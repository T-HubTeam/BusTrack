from pubnub import Pubnub
class PubNub:
	def __init__(self,pubkey,subkey):
		self.pubnub = Pubnub(publish_key=pubkey, subscribe_key=subkey)

		pass

	def subCallback(self,message,channel):
		print (message,channel)

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