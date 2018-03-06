import zerorpc

c = zerorpc.Client()
c.connect("tcp://10.0.3.1:4244")
print c.hello("RPC")
print c.kali(2,3)
print c.bagi(8,4)

#c.cdir("data1")