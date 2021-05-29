'''
Helper functions
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

def correct_time_string(time_str):
	time_list = time_str.split(":")
	hr, mins, sec = int(time_list[0]) , int(time_list[1]), int(time_list[2])
	if (sec // 60 > 0):
		mins += sec // 60
		sec = sec % 60

	if (mins // 60 > 0):
		hr += (mins // 60)
		mins = mins % 60
	
	ret_s = ""
	ret_s = "{}:{}:{}".format(hr, mins, sec)
	return (ret_s)


def correct_date_string(date_str):
	pass


def convert_ip_to_int(ip_str):
	ip_list = list(map(int , ip_str.split(".")))
	print(ip_list)
	power = len(ip_list) - 1
	ip_int = 0
	for i in range(len(ip_list)):
		ip_int += (ip_list[i] * (256 ** power))
		power -= 1
	print(ip_int)


def check_isogram(s_str):
	'''
	If the input string does not contain repeating characters 
	Then it is isogram
	Having two loops 
	One loop iterates through and points to a character -i th 
	And next loop iterates from i+1 th and checks whether any character 
	it encounter is same as the character in i th position
	'''
	s_str = s_str.lower()
	for i in range(len(s_str)):
		for j in range(i + 1, len(s_str)):
			if s_str[i] == s_str[j]:
				return (False)
	else:
		return (True)
	

def gen_mexian_wave(s_str):
	'''
	Mexian wave is similar to the wave done in cricket
	Where fans try to mimic the waves going up and down
	Here we have to do this in a string
	for example hi
	Then we have to return [Hi, hI]
	Here starting from the left index we try to captilize each character
	The input string is iterated starting from 0 and then a new character is created
	by concatining the characters before the iterator and character converted upper
	and the characters after the iterator
	'''
	s_str = s_str.lower()
	list_wave = []
	temp_str = " "
	for i in range(len(s_str)):
		temp_str = s_str[:i] + str.upper(s_str[i]) + s_str[i + 1:]
		list_wave.append(temp_str)

	return list_wave



def find_big_num_del_digit(num):
	s_num = str(num)
	big_num = 0
	temp_num = " "
	for i in range(len(s_num)):
		temp_num = int(s_num[:i] + s_num[i + 1 : ])
		if temp_num > big_num:
			big_num = temp_num
	print(big_num)

def find_big_num_shuffle(num):
	str_num = str(num)
	list_num = []
	for i in range(len(str_num)):
		list_num.append((str_num[i]))
	list_num.sort(reverse= True)
	return ("".join(list_num))


def check_word_frequency(message, word):
	word_list = message.split(" ")
	count = 0
	for s in word_list:
		if s == word:
			count += 1
	return (count)

def RGB_to_HEX(rgb_tuple): 
	r, g, b = rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]
	if ((r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255)):
		hexvalue = "#";
		hexvalue = hexvalue + str(hex(r))[2:]
		hexvalue = hexvalue + str(hex(g))[2:]
		hexvalue = hexvalue + str(hex(b))[2:]
		return str(hexvalue)
	# The hex color code doesn't exist
	else:
		return None


def build_accumlated_str(inp_str):
	out_str = ""
	for i in range(len(inp_str)):
		out_str += inp_str[i].upper()
		for j in range(i):
			out_str += inp_str[i]
		if not(i == len(inp_str) - 1): 
			out_str += "-"
	return out_str


