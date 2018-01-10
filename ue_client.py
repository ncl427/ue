from bjsonrpc import connect
import pickle
from models.Mdd import Mdd
from models.ueAttachObj import ueAttachObj
import time

def createAttachObj():
   obj = ueAttachObj()
   obj.ip = "192.168.186.51"
   obj.serviceType = 5

   #print "ueAttachObj:"
   #print "\t", obj.ip
   #print "\t", obj.serviceType
   return obj

# connecting to vBBU
print "\n---------------------"
print "...connecting ue-vBBU"
time.sleep(1)
c = connect("192.168.186.61")
print "connected ue-vBBU."
time.sleep(1)

# sending attach request to vBBU with a service-type for video

attachedObj = createAttachObj()
attachedParameter = pickle.dumps(attachedObj)
print "...attaching ue-vBBU-..."
time.sleep(2)
response = c.call.attachvBBU(attachedParameter)
responseUnpickled = pickle.loads(response)

time.sleep(1)
print "attached ue-vBBU-..."
time.sleep(0.5)
print "attaching ue-vBBU-... response: "
print "\tMdd-nesId: ", responseUnpickled.nesId
print "\tMdd-tempId: ", responseUnpickled.tempId
