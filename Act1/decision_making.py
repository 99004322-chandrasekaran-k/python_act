def biggest_of_3_nos(first_num, sec_num, third_num):
	'''
	Biggest of three numbers

	the inputs has to be int or float else none will be returned

	The logic 
		1) If first is greater than second 
			a) first is greater than third
				first is biggest 
			b) first is less than third
				third is biggest
		2) sec is greater than first 
			a) sec is greater than third
				sec is greater
			b) sec is less than third 
				third is greater
	''' 
	check_int_cond = ((isinstance(first_num, int)) and (isinstance(sec_num, int)) and (isinstance(third_num, int)))
	check_float_cond = ((isinstance(first_num, float)) and (isinstance(sec_num, float)) and (isinstance(third_num, float)))
	if (check_int_cond) or (check_float_cond):
		if (first_num >= sec_num):
			if (first_num >= third_num):
				return first_num
			elif (third_num > first_num):
				return third_num
		elif (sec_num >= first_num) :
			if (sec_num >= third_num):
				return (sec_num)
			elif (third_num > sec_num):
				return (third_num)
	else:
		return (None)


def biggest_of_4_nos(first_num, sec_num, third_num, fourth_num):
	'''
	Biggest of four numbers

	the inputs has to be int or float else none will be returned

	The logic 
		1) first is greater than sec
			a) first is grater than third 
				first is greater than fourth
					first is the greatest
				first is less than fourth
					fourth is greatest
			b) first is less than third
			 	third is greater than fourth
					third is greatest
				third is less than third
					fourth is greatest
		2) first is less than sec
			a) sec is grater than third 
				sec is greater than fourth
					sec is the greatest
				sec is less than fourth
					fourth is greatest
			b) sec is less than third
			 	third is greater than fourth
					third is greatest
				third is less than third
					fourth is greatest


	''' 
	check_int_cond = ((isinstance(first_num, int)) and (isinstance(sec_num, int)) and (isinstance(third_num, int)))
	check_float_cond = ((isinstance(first_num, float)) and (isinstance(sec_num, float)) and (isinstance(third_num, float)))
	if (check_int_cond) or (check_float_cond):
		if (first_num >= sec_num):
			if (first_num >= third_num):
				if (first_num >= fourth_num):
					return (first_num)
				else:
					return (fourth_num)
			else :
				if (third_num >= fourth_num):
					return (third_num)
				else:
					return (fourth_num)
		elif (sec_num >= first_num) :
			if (sec_num >= third_num):
				if (sec_num >= fourth_num):
					return (sec_num)
				else:
					return (fourth_num)
			elif (third_num > sec_num):
				if (third_num > fourth_num):
					return (third_num)
				else:
					return (fourth_num)
	else:
		return (None)

def check_leap_year(year):
	if ((year % 400) == 0):
		# the century year is leap or not
		return (True)
	elif ((year % 4) == 0):
		# the normal year is leap or not
		return (True)
	else:
		return (False)
	

def pythogoras_formula(first_side, second_side, third_side):
	copy_third_side = biggest_of_3_nos(first_side, second_side, third_side)
	copy_sec_side = biggest_of_3_nos(first_side, second_side, 0)
	copy_first_side = (first_side + second_side + third_side) - (copy_sec_side + copy_third_side)
	first_side, second_side, third_side = copy_first_side, copy_sec_side, copy_third_side	
	if ((first_side ** 2) + (second_side ** 2)) == (third_side ** 2):
		return (True)
	else:
		return (False)

def type_of_triangle(first_side, second_side, third_side):
	if (first_side == second_side) and (second_side == third_side):
		return ("Equilateral")
	elif ((first_side == second_side) or (first_side == third_side) or (second_side == third_side)):
		return ("Isosceles")
	elif (pythogoras_formula(first_side, second_side, third_side)):
		return ("Right Triangle")
	else :
		return ("Scalene")


def quadrent_of_point(x, y):
	if (x >= 0) and (y >= 0):
		return (1)
	elif (x <= 0) and (y >= 0):
		return (2)
	elif (x <= 0) and (y <= 0):
		return (3)
	elif (x >= 0) and (y >= 0):
		return (4)
	

	

	
