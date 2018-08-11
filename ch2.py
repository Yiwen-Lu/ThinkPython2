# Exercise 2.2

import math

# 2.2.1
def volume(r):
	return 4/3 * math.pie * r**3

# 2.2.2
def wholesale_cost(num_copy):
	assert (num_copy >= 1), 'The copies must be larger than one.'
	return num_copy * (24.95 * (1-0.4) + 3 + (num_copy-1)*0.75)

# 2.2.3
def compute_time(leave_h,leave_m, leave_s):
	#leave_time = leave_h + leave_m/60 + leave_s/60**2
	spent_second = 2*(8*60+15) + 3*(7*60+12)
	current_second =  

