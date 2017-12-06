from bjsonrpc import connect

# connecting to vBBU
print "\n---------------------"
print "...connecting ue-vBBU"
c = connect("192.168.186.61")
print "connected ue-vBBU."

# sending attach request to vBBU with a service-type for video
print "...attaching ue-vBBU"
response = c.call.attachvBBU("192.168.186.51", 1)
print "attaching ue-vBBU response: ", response
