# Exercise 2.2.3
import numpy as np

def pace(min_per_mile):
	minute, second = str(min_per_mile) .split('.')
	v = int(minute) + int(second) / 60
	return v

def convert_time(durantion):
	hh = durantion // 60
	mm = round(durantion % 60)
	return int(hh), int(mm)

def running_time(v, s):
	return np.sum(v * s)

def return_time(start_time, v, s):
	start_hh, start_mm = str(start_time).split(':')
	durantion = running_time(v, s)
	add_hh, add_mm = convert_time(durantion)
	end_hh = int(start_hh) + add_hh
	end_mm = int(start_mm) + add_mm
	if end_mm >= 60:
		end_hh = end_hh + 1
		end_mm = end_mm - 60

	# check if too late for breakfast:
	if end_hh >= 12:
		raise ValueError('It is too late for breakfast.')
	end_time = str(end_hh) + ":" + str(end_mm)
	return end_time


if __name__ == '__main__':
	v = np.array([pace(8.15), pace(7.12), pace(8.15)])
	s = np.array([1.0, 3.0, 1.0])
	start_time = "6:52"
	back_time = return_time(start_time, v, s)
	print("At {} I get home for breakfast.".format(back_time))
