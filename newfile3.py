#create a function multiplecation table of a number
def mtable(n):
	for i in range(1,11):
		print('{}*{}={}'.format(n,i,n*i))
#let us call the function
mtable(101)