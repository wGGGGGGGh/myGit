Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isPrime(x):
	flag = True
	for n in range(2,x):
		if not flag:
			break
		elif not x % n:
			flag = False
	return flag

>>> for i in range(40):
	if isPrime(i**2+i+41):
		print(i,end = ' ')
	else:
		continue

	
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 
>>> 