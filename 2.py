count = 0
a = 1
b = 1
evenFibSum = 0
while count < 4000001:
	count = a + b
	if count % 2 == 0:
		evenFibSum += count
	a = b
	b = count

print(evenFibSum)

	
