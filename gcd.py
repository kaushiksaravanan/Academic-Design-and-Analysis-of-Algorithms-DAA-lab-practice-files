n1=int(input("Enter n1 "))
n2=int(input("Enter n2 "))

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

print(gcd(n1,n2))

#SC o(1)