month = raw_input('Please, enter month name: ')

name_number = {"January": 1, "january": 1,
	       "February": 2, "february": 2,
	       "March": 3, "march": 3,
	       "April": 4, "april": 4,
	       "May": 5, "may": 5,
	       "June": 6, "june": 6,
	       "July": 7, "july": 7,
	       "August": 8, "august": 8,
	       "September": 9, "september": 9,
	       "October": 10, "october": 10, 
	       "November": 11, "november": 11,
	       "December": 12, "december": 12}

if month in name_number:
	print 'Number of month', month, ':', name_number[month]
else:
	print 'Incorrect month name'
