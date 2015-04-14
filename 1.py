multipleSum = 0

for x in range(0,1000):
	three = 0
	five = 0
	fifteen = 0
	if x % 3 == 0:
		three = x
	if x % 5 == 0:
		five = x
	if x % 15 == 0:
		fifteen = -x
	multipleSum = multipleSum + three + five + fifteen

print(multipleSum)
