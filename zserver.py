import zerorpc
import func

c = zerorpc.Server(func)
c.bind("tcp://0.0.0.0:4244")
c.run()
