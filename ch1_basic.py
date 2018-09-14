# Exercise 1.2

def compute_second(minutes, seconds):
	return 60*minutes + seconds

def compute_miles(kilometers):
	return kilometers / 1.61

def average_pace(kilometers, minutes, seconds):
	'''
	v = S / t
	'''
	miles = compute_miles(kilometers)
	hour = compute_second(minutes, seconds) / 60**2
	return miles / hour

if __name__ == '__main__':
	kilometers = 10
	minutes, seconds = 42, 42
	print('The average speed is {:.4f} miles/hour.'
		.format(average_pace(kilometers, minutes, seconds)))
