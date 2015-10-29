def fib():
	x0,x1 = 0,1
	while True:
		x0 , x1 = x1 , x0+x1
		yield x1

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()

