try:
	y = int(raw_input("Please, enter year: "))
except ValueError:
	print('Year is entered incorrectly')
except NameError:
	print('Year is not set')
else:
	if (y % 4) == 0:
		print('Leap year')
	elif (y % 100) == 0
		print('Not a leap year')
	elif (y % 400) == 0:
		print('Leap year')
	else:
		print('Not a leap year')

