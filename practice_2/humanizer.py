dic = {"one": "chas", "two": "chasa", "many": "chasov"}
num = int(input("Enter number: "))

def humanizer(num, dic):

	if type(num) != int:
		print 'Enter a number'
	elif type(dic) != dict:
		print 'Enter dictionary'
	else:
		if num > 1 and num < 5:
			print num, dic["two"]
		
		elif num == 1:
			print num, dic["one"]

		else:
			print num, dic["many"]

print humanizer(num,dic)
