import math
def constant():
	const = {"pi": math.pi, "e": math.e, "cos": math.cos(25),
	         "sin": math.sin(25), "exp": math.exp(2), "log": math.log10(2),
	         "sqrt": math.sqrt(4), "tan": math.tan(4)}

	con = raw_input("Enter <const>:<acc>: ")
	x = con.split(":")
	name = x[0]
	acc = int(x[1])
	print name, "=", round(const[name], acc)

constant()
