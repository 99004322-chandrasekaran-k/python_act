'''

Helper functions


'''
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


def sum_of_digits(num):
	'''
	Takes the input as an int
	Then finds the digits inside it
	Then the sum of it
	'''
	digits_tuple = find_digits_using_string(num)
	return (sum(digits_tuple))

'''

Assignment questions

'''
def fibonacci_n_series_print(n):
	'''

	Takes the n as a input
	Generates n fibonacci numbers
	'''
	num1, num2, temp = 1, 1, 1
	for i in range(n):
		temp = num2 + num1 
		num1, num2 = num2, temp
		print(temp)



def tribonacci_n_series_print(n):
	'''
	Takes the n as a input
	Generates n tribonacci numbers
	'''
	num1, num2, num3, temp = 1, 1, 1, 0
	for i in range(n):
		temp = num3 + num2 + num1 
		num1, num2, num3 = num2, num3, temp
		print(temp)


def fact_of_num(num):
	'''
	Factorial of a given number
	'''
	res = 1
	for i in range(num):
		res = res * num
		num -= 1
	return (res) 


def sum_of_factors(num):
	tuple_factors = find_factors(num)
	return (sum(tuple_factors))

def digital_root(num):
	s1 = 1
	while (s1 <= 9):
		s1 = sum_of_digits(num)
	return (s1)


def sum_of_traingle_num(n):
	s = 0
	for i in range(n):
		for j in range(n - i + 1):
			s += j
	return (s)


def find_big_num_del_digit(num):
	s_num = str(num)
	big_num = 0
	temp_num = " "
	for i in range(len(s_num)):
		temp_num = int(s_num[:i] + s_num[i + 1 : ])
		if temp_num > big_num:
			big_num = temp_num
	print(big_num)


def ncr(n, r):
	res = fact_of_num(n) / fact_of_num(r)
	res /= fact_of_num(n - r)
	return res

print(ncr(10, 6))