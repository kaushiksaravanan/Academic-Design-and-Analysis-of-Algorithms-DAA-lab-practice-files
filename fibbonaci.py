fib=[0,1]
n=int(input("Enter n\n"))

def normal():
	for iterable in range(n):
		next=fib[-1]+fib[-2]
		fib.append(next)
	print(*fib)
	print()

def get_last_dig(n):
	return n%10


def bit_efficient_tc():
	fib=[0,1]
	for iterable in range(n):
		next=get_last_dig(get_last_dig(fib[-1])+get_last_dig(fib[-2]))
		fib.append(next)
	print(*fib)
	print()

def bit_efficient_sc():
	fib=[0,1]
	for iterable in range(n):
		next=get_last_dig(get_last_dig(fib[-1])+get_last_dig(fib[-2]))
		# temp=fib[1]
		fib[0]=fib[1]
		# next
		fib[1]=next
	print(fib[1])

#TC O(n)
#SC O(n)
# fails for longer input / overflow
# normal()

#TC O(n)
#SC O(n)
# works for longer input due to using only one digit
# bit_efficient_tc()

#TC O(n)
#SC O(1)
bit_efficient_sc()


