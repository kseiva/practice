import math

const = {"pi": math.pi, "e": math.e, "cos": math.cos(25),
	 "sin": math.sin(25), "exp": math.exp(2), "log": math.log10(2),
	 "sqrt": math.sqrt(4), "tan": math.tan(4)}

name = raw_input("Enter the name of the constant: ")
acc = int(input("Enter the number of decimal places: "))

if name in const:
	print 'Output', name, 'with accuracy', acc, ':', round(const[name], acc)
else:
	print 'Incorrect constant name'

