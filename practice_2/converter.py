month = raw_input('Please, enter month name: ')

name_number = {"january": 1,"february": 2,
	       "march": 3, "april": 4,
	       "may": 5, "june": 6,
	       "july": 7, "august": 8,
	       "september": 9, "october": 10, 
	       "november": 11, "december": 12}

if month in name_number:
	print 'Number of month', month, ':', name_number[month]
else:
	print 'Incorrect month name, try again.'
