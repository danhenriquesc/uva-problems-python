def doTheWork(n):
	if int(n) <= 17:
		return n
	else:
		ini = n[:-1]
		las = n[len(n)-1:]
		
		return doTheWork(str(int(ini) - 5*int(las)))


while (True):
	n = input()
	if int(n) == 0:
		break
	
	if int(doTheWork(n)) % 17 == 0:
		print ("1")
	else:
		print ("0")

