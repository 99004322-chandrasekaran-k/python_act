from Act1.decision_making import biggest_of_3_nos, check_armstong
from Act1.decision_making import biggest_of_4_nos
from Act1.decision_making import check_armstong
from Act1.decision_making import reverse_num_creating_new_list
from Act1.decision_making import sum_of_digits
from Act1.decision_making import gcd
from Act1.decision_making import lcm
from Act1.decision_making import check_leap_year
from Act1.decision_making import type_of_triangle
from Act1.decision_making import roots_of_quad_eqn
from Act1.decision_making import quadrent_of_point
from Act1.decision_making import choice_based_arithmetic
from Act1.decision_making import check_vowel_or_consonant

def test_big_3_nos1():
	assert biggest_of_3_nos(1, 2, 3) == 3

def test_big_3_nos2():
	assert biggest_of_3_nos(1, 3, 2) == 3

def test_big_3_nos3():
	assert biggest_of_3_nos(3, 2, 1) == 3



def test_big_4_nos1():
	assert biggest_of_4_nos(1, 2, 3, 4) == 4

def test_big_4_nos2():
	assert biggest_of_4_nos(1, 3, 4, 2) == 4

def test_big_4_nos3():
	assert biggest_of_4_nos(3, 4, 2, 1) == 4

def test_big_4_nos4():
	assert biggest_of_4_nos(4, 2, 3, 1) == 4


def test_check_armstrong1():
	assert check_armstong(153) == True

def test_check_armstrong2():
	assert check_armstong(144) == False

def test_check_armstrong3():
	assert check_armstong(1472) == False

def test_reverse_num1():
	assert reverse_num_creating_new_list(102) == 201

def test_reverse_num2():
	assert reverse_num_creating_new_list(1234) == 4321

def test_sum_of_digits1():
	assert sum_of_digits(1234) == 10

def test_sum_of_digits2():
	assert sum_of_digits(104) == 5

def test_gcd1():
	assert gcd(10, 20) == 5

def test_gcd2():
	assert gcd(3, 20) == 1

def test_lcm1():
	assert lcm(72, 120) == 360


def test_check_leap_year1():
	assert check_leap_year(2016) == True

def test_check_leap_year2():
	assert check_leap_year(2017) == False

def test_check_leap_year():
	assert check_leap_year(2000) == True

def test_check_triangle1():
	assert type_of_triangle(1, 1, 1) == "Equilateral"

def test_check_triangle2():
	assert type_of_triangle(1, 1, 5) == "Isosceles"

def test_check_triangle3():
	assert type_of_triangle(3, 4, 5) == "Right Triangle"

def test_check_triangle4():
	assert type_of_triangle(3, 8, 4) == "Scalene"

# Both real roots
def test_quadratic_eqn1():
	assert roots_of_quad_eqn(1, -8, 12) == (6, 2)

# Both equal and real roots
def test_quadratic_eqn2():
	assert roots_of_quad_eqn(3, -6, 3) == (1, 1)

# Both imaginary roots
def test_quadratic_eqn3():
	assert roots_of_quad_eqn(1, 6, 11) == None


def test_quad_point():
	assert quadrent_of_point(1, 1) == 1

def test_quad_point():
	assert quadrent_of_point(-1, 1) == 2

def test_quad_point():
	assert quadrent_of_point(-1, -1) == 3

def test_quad_point():
	assert quadrent_of_point(1, -1) == 4


def test_choice_arithmetic1():
	assert choice_based_arithmetic(1, 2, 1) == 3


def test_choice_arithmetic2():
	assert choice_based_arithmetic(1, 2, 2) == -1


def test_choice_arithmetic3():
	assert choice_based_arithmetic(1, 2, 3) == 2


def test_choice_arithmetic4():
	assert choice_based_arithmetic(4, 2, 4) == 2


def test_check_vowel_or_const1():
	assert check_vowel_or_consonant("a") == "Vowel"

def test_check_vowel_or_const2():
	assert check_vowel_or_consonant("v") == "Consonant"



