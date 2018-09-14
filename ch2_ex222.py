# Exercise 2.2.2
def wholesale_cost(cover_price, discount, copy_num):
	assert type(copy_num) is int and (copy_num >= 0)
	shipping = 3 + 0.75 * (copy_num - 1) if copy_num >= 1 else 0
	return cover_price*(1 - discount)*copy_num + shipping

if __name__ == '__main__':
	cover_price = 24.95
	discount = 0.40
	copy_num = 60
	cost = wholesale_cost(cover_price, discount, copy_num)
	print("the wholesale cost for {} copies is {:.2f}"
				.format(copy_num, cost))