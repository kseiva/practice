def gen():
	numbers = {"0": [['','*','*','*','*','*','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','','','','','*',''],
		['','*','*','*','*','*','*','']],
	       "1": [['','','','*','*','','',''],
	        ['','','*','*','*','','',''],
		['','','','*','*','','',''],
		['','','','*','*','','',''],
	        ['','','','*','*','','',''],
		['','','','*','*','','',''],
	        ['','','','*','*','','',''],
 	        ['','','*','*','*','*','','']],
	       "2": [['','','','*','*','*','',''],
	        ['','','*','','','','*',''],
	        ['','*','','','','','*',''],
	        ['','','','','','*','',''],
 	        ['','','','','*','','',''],
	        ['','','','*','','','',''],
	        ['','','*','','','','',''],
        	['','*','*','*','*','*','','']],
	       "3": [['*','*','*','*','*','*','*','*'],
	        ['','','','','','','','*'],
       	        ['','','','','','','','*'],
	        ['','*','*','*','*','*','*','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
		['*','*','*','*','*','*','*','*']],
	       "4": [['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*']],
	       "5": [['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','',''],
	        ['*','','','','','','',''],
	        ['*','*','*','*','*','*','*','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*']],
	       "6": [['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','',''],
	        ['*','','','','','','',''],
	        ['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*']],
	       "7": [['*','*','*','*','*','*','*','*'],
	        ['','','','','','','*',''],
	        ['','','','','','*','',''],
	        ['','','','','*','','',''],
	        ['','','','*','','','',''],
	        ['','','*','','','','',''],
	        ['','*','','','','','',''],
	        ['*','','','','','','','']],
	       "8": [['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','','*'],
  	        ['*','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','','*'],
                ['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*']],
	       "9": [['*','*','*','*','*','*','*','*'],
	        ['*','','','','','','','*'],
	        ['*','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['','','','','','','','*'],
	        ['*','*','*','*','*','*','*','*']]}
	num = raw_input("Please, enter number: ")
	if numbers.has_key(num):
		for sumb in numbers[num]:
			s = ''
			for i in sumb:
				if i == '':
					s += ' '
				else:
					s += i
			print s
	else:
			print 'Incorrect. Enter a number from 0 to 9.'
gen()




































