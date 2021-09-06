
#Look Before You Leap Method (LBYL) where you make sure to have all variables needed


def get_days_alive(person):
    if 'age' in person: 
        days = person['age'] * 365 
        print(f'{person["name"]} has been alive for {days} days')


{'name': 'princess kitty', 'age': 10}

#Easier to Ask Forgiveness than Permission Method (EAFP) where you just go for it and wrap it in a 'try' 

#Using this approach you need to be specific about the ErrorType you are looking for 


def get_days_alive(person):

    try: 
        days = person['age'] * 365 
        print(f'{person["name"]} has been alive for {days} days')
    except KeyError as exc:
        print(f'Missing key: {exc}')
    except TypeError:
        print('Expected person to be a dict')

{'name': 'princess kitty', 'age': 10}



def bounded_avg(nums):
	'''Return avg of nums (make sure nums are 1-100)'''
	for n in nums:
		if n < 1 or n > 100:
			raise ValueError ('Outside bounds of 1-100')
	return sum(nums) / len(nums) 

def handle_data():
    ages = [10,40,50,99,103,2,0]

    try:
        avg = bounded_avg(ages)
        print('Average was', avg)
    
    except ValueError as exc:
        print('Invalid age in list of ages')
