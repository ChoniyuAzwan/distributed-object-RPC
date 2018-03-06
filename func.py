import os

def hello(name):
	print("client calling...")
	return "Hello, %s" %name

def kali(x,y):
	hasil = x*y
	return "hasil kali = %s" %hasil

def bagi(x,y):
	x = float(x)
	y = float(y)
	hasil = x/y
	return "hasil bagi = %s" %hasil

# def cdir(dirname):
# 	os.mkdir("/tmp/%s" %dirname)
# 	print "Directory %s created" % dirname
 
