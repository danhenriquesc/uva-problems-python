primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

while 1:
	N = int(input())

	if(N == 0):
		break
	
	primesN = []
	for p in range(0,len(primes)):
		primesN.append(0)

	upperIndex = 0

	for n in range(2,N+1):
		index = 0

		M = n

		while M > 1:
			if M%primes[index] == 0:
				M/=primes[index]
				primesN[index]+=1
			else:
				index+=1

		if index > upperIndex:
			upperIndex = index
	
	result = '{:3d}'.format(N) + "! ="
	for p in range(0,len(primesN)+1):
		if p <= upperIndex:
			if p>0 and p%15 == 0:
				result += '\n      ';
			
			result += '{:3d}'.format(primesN[p])


	print(result)

