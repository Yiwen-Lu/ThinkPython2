# Exercise 2.2.3 optimal version

def convert_time(minutes, seconds):
	#ss = seconds % 60
	mm = minutes + seconds // 60
	hh = minutes // 60
	return int(hh), int(mm)


def back_time(start_time, speeds, miles):
	start_hh, start_mm = str(start_time).split(':')
	total_min, total_sec = 0, 0

	for v,s in zip(speeds, miles):
		minute, second = str(v).split(':')
		min_spent = s * int(minute)
		sec_spent = s * int(second)
		total_min += min_spent
		total_sec += sec_spent

	hh, mm = convert_time(total_min, total_sec)
	back_hh = int(start_hh) + hh
	back_mm = int(start_mm) + mm
	if back_mm >= 60:
		back_hh += 1
		back_mm -= 60

	# check if too late for breakfast:
	if back_hh >= 12:
		raise ValueError('It is too late for breakfast.')	
	
	return str(back_hh) + ":" + str(back_mm)


if __name__ == '__main__':
	speeds = ['8:15', '7:12', '8:15']
	miles = [1, 3, 1]
	start_time = '6:52'
	breakfast_time = back_time(start_time, speeds, miles)
	print("At %s I get home for breakfast." % breakfast_time)
