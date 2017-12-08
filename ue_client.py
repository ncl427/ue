from bjsonrpc import connect
import pickle
from models.Mdd import Mdd
from models.ueAttachObj import ueAttachObj

def createAttachObj():
   obj = ueAttachObj()
   obj.ip = "192.168.186.51"
   #obj.serviceType = 4

   #print "ueAttachObj:"
   #print "\t", obj.ip
   #print "\t", obj.serviceType
   return obj

# connecting to vBBU
print "\n---------------------"
print "...connecting ue-vBBU"
c = connect("192.168.186.61")
print "connected ue-vBBU."

# sending attach request to vBBU with a service-type for video

attachedObj = createAttachObj()
attachedParameter = pickle.dumps(attachedObj)
print "...attaching ue-vBBU"
response = c.call.attachvBBU(attachedParameter)

print "attaching ue-vBBU response: "
responseUnpickled = pickle.loads(response)
print "\tMdd-nesId: ", responseUnpickled.nesId
print "\tMdd-tempId: ", responseUnpickled.tempId
