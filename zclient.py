import zerorpc

c = zerorpc.Client()
c.connect("tcp://10.0.3.1:4244")
print c.hello("RPC")
#c.cdir("data1")