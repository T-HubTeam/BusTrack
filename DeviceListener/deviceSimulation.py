from pb import PubNub
import datetime
import time
tagId = ['a4sd5f7as6d54fe9f4d','e8r7t546e5rt9er4er5','xc5v4b3xc2v1b5xc51c','4f5gvb2n13d52y4u8','8d7fg3s2df432cvb1ds']

pubkey = 'pub-c-b04e36e4-5535-48f1-a969-c0a9fced6655'
subkey = 'sub-c-0dc10f58-7466-11e8-98cb-067913ebee63'

pb = PubNub(pubkey,subkey)
pubchannel = 'dev-listn'

for iD in tagId:
	t = datetime.datetime.now()
	
	mesg = {'tagId':iD,'timeStamp':{"Date":str(datetime.date.today()),"Time":t.strftime("%H:%M:%S")}}
	pb.pub(mesg,pubchannel)
	time.sleep(10)