import math

'''

Helper fucntions are below

'''
def find_digits_using_string(num):
	'''
	Takes an int and returns a tuple of digits of the num

	Converts the given num into string
	Then iterates through each individual string (each digit) 
	and converts that to int
	and stores it into a list
	Then that list is converted to a tuple
	'''
	str_num = str(num)
	len_tuple = len(str_num)
	list_num = []
	for i in range(len_tuple):
		list_num.append(int(str_num[i]))
	tuple_num = tuple(list_num)
	return (tuple_num)


def find_num_from_digits_using_string(digits_tuple):
	'''
	Takes the input as a tuple which contains the digits
	Then outputs a num made up of the digits

	First a empty string is created
	Then iterating thorugh the tuple, we add to the string
	Then finally type casted to int and returned
	'''

	str_digits = ""
	for i in digits_tuple:
		str_digits += str(i)
	return (int(str_digits))


def find_factors(num = 10):
	'''
	iterating from num /2 to 1 and then checking if any number divides
	If it is divided then added to the list
	'''
	factors_list = []
	for i in range(num // 2 , 1, -1):
		if (num % i) == 0:
			factors_list.append(i)
	factors_tuple = tuple(factors_list)
	return factors_tuple


def pythogoras_formula(first_side, second_side, third_side):
	copy_third_side = biggest_of_3_nos(first_side, second_side, third_side)
	copy_sec_side = biggest_of_3_nos(first_side, second_side, 0)
	copy_first_side = (first_side + second_side + third_side) - (copy_sec_side + copy_third_side)
	first_side, second_side, third_side = copy_first_side, copy_sec_side, copy_third_side	
	if ((first_side ** 2) + (second_side ** 2)) == (third_side ** 2):
		return (True)
	else:
		return (False)

'''

Assignment questions in order

'''
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


def check_armstong(num):
	'''
	To be a armstrong number,  
	each digit raised to the power of the num of digit and added 
	must be equal to the number itself
	Each digit in the tuple raised to the len of the tuple
	and added
	Then it is checked whether it is equal to the number
	'''
	tuple_digits = find_digits_using_string(num)
	base = len(tuple_digits)
	dig_raise_to_base = 0
	for i in tuple_digits:
		dig_raise_to_base += (i ** base)
	if (dig_raise_to_base == num):
		return (True)
	else:
		return (False)


def reverse_num_creating_new_list(num):
	'''
	Takes the input as a int
	Then converts the int into a tuple of digits
	Then that tuple is converted into list
	iterating the list strting from the end decrementing by 1 
	reaching till 0
	In iterating each thing is added into another list
	And finally that list is converted to num
	'''
	list_digits = list(find_digits_using_string(num))
	rev_list_digits = []
	for i in range(len(list_digits) - 1, -1, -1):
		rev_list_digits.append(list_digits[i])
	return (find_num_from_digits_using_string(tuple(rev_list_digits)))


def sum_of_digits(num):
	'''
	Takes the input as an int
	Then finds the digits inside it
	Then the sum of it
	'''
	digits_tuple = find_digits_using_string(num)
	return (sum(digits_tuple))


def gcd(num1 = 1, num2 = 1):
	'''
	Find the factors of num1 in descending order
	Find the factors of num2 in descending order
	Then the common factor is chosen and returned
	'''
	factors_tuple1 = find_factors(num1)
	factors_tuple2 = find_factors(num2)
	for i in factors_tuple1:
		if i in factors_tuple2:
			return (i)


def lcm(num1, num2):
	'''
	LCM is nothing but the max number that divides both the num1 and num2
	First check if the max_num = max(num1, num2) divides both n1 and n2
	Then increment the max_num and check until it divides both
	As LCM is always > or = n1 and n2
	'''
	max_num = max(num1, num2)
	while (not ((max_num % num1 == 0) and (max_num % num2) == 0)):
		max_num += 1
	return max_num


def check_leap_year(year):
	'''
	Checks the following conditions and returns true if it satisfies
	the century year is leap or not
	the normal year is leap or not
	'''
	if ((year % 400) == 0):
		return (True)
	elif ((year % 4) == 0):
		return (True)
	else:
		return (False)
	
	
def type_of_triangle(first_side, second_side, third_side):
	'''
	Takes the input as the length of the sides of the triangle
	Then equilatral is returned when all the sides are equal
	or if 2 sides are equal then isosceles is returned 
	or if it satisfies the pythogoras formula then right triangle is returned 
	or if is not anything above scalene is returned 
	'''
	if (first_side == second_side) and (second_side == third_side):
		return ("Equilateral")
	elif ((first_side == second_side) or (first_side == third_side) or (second_side == third_side)):
		return ("Isosceles")
	elif (pythogoras_formula(first_side, second_side, third_side)):
		return ("Right Triangle")
	else :
		return ("Scalene")


def roots_of_quad_eqn(a, b, c):
	'''
	takes the value as the coefficients of a quadratic equation
	Based on the quadratic formula
	First the determinant is found
	From which the nature of roots is determined
	After determining the nature of the roots
	If both the roots are real then 2 both r1 , r2 are different
	If both are real and same both r1 and r2 are equal
	If the roots are imaginary returns None
	'''
	det = ((b ** 2) - (4 * a * c))
	if (det > 0):
		r1 = ((-b) + math.sqrt(det)) / (2 * a)
		r2 = ((-b) - math.sqrt(det)) / (2 * a)
	elif (det == 0):
		r1 = r2 = ((-b) + math.sqrt(det)) / (2 * a)
	else: 
		return (None)
	return (r1, r2)	


def quadrent_of_point(x, y):
	'''
	takes the input as 2 points according to the cartesain 
	coordinate
	Then checks and returns the coordinate it lies
	If x has a value 0 or postive as well as y has value 0 or postive
	then it lies in first quad
	If x is negative and y is positive
	Then it is in sec quad
	if x is negative and y is also negative
	Then it is third quad
	if x is negative and y is positive
	Then it is fourth quad
	'''
	if (x >= 0) and (y >= 0):
		return (1)
	elif (x <= 0) and (y >= 0):
		return (2)
	elif (x <= 0) and (y <= 0):
		return (3)
	elif (x >= 0) and (y >= 0):
		return (4)
	


def choice_based_arithmetic(num1, num2, choice = 1):
	'''
	Takes the input as num1, num2 and choice
	The defualt value of choice is 1
	if choice is 1 it wil add the numbers
	if choice is 2 it will subtract
	if choice is 3 it will multiply
	if choice is 4 it will divide
	'''
	if choice == 1:
		return (num2 + num1)
	elif (choice == 2):
		return (num1 - num2)
	elif (choice == 3):
		return (num1 * num2)
	elif (choice == 4):
		return (num1 / num2)


def check_vowel_or_consonant(str_s):
	'''
	Takes the string as input
	Then checks whether it contains alphabet
	If it does not then returns "Not a string"
	Else It checks whether it is vowel or string
	'''

	if not (str.isalpha()):
		return ("Not a string !")
	str_s = str_s.lower()
	if (str_s == 'a') or (str_s == 'e') or (str_s == 'i') or (str_s == 'u'):
		return "Vowel"
	else:
		return "Consonant"
