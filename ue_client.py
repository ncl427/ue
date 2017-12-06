from bjsonrpc import connect

# connecting to vBBU
c = connect("192.168.186.61")
print "ue-connecting to vBBU"

# sending attach request to vBBU with a service-type for video
response = c.call.attachvBBU("192.168.186.51", 1)
print "vBBU-response: ", response
