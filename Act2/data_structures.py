def dif_ele_in_eq_arr(inp_list):
	dict_ele = {}
	for i in inp_list:
		if not(i in dict_ele.keys()):
			dict_ele[i] = 1
		else:
			dict_ele[i] += 1
	for i in dict_ele.keys():
		if dict_ele[i] == 1:
			return i
	
def find_ele_close_mean(inp_list):
	list_mean = sum(inp_list) / len(inp_list)
	diff_ele_mean = abs(inp_list[0] - list_mean)
	close_to_mean = inp_list[0]
	for i in range(1, len(inp_list)):
		temp_ele_mean = (abs(inp_list[i] - list_mean))
		if temp_ele_mean < diff_ele_mean:
			diff_ele_mean = temp_ele_mean
			close_to_mean = inp_list[i]

	return close_to_mean


def avg_speed_bus(dist_list):
	return (sum(dist_list) / len(dist_list))

def noof_peep_bus(bus_peep_list):
	return (sum(bus_peep_list))


def diff_two_mins(inp_list):
	min1 = inp_list[0]
	min2 = inp_list[1]
	for i in range(2, len(inp_list)):
		if inp_list[i] < min1:
			min2 = min1
			min1 = inp_list[i]
		elif inp_list[i] < min2:
			min2 = inp_list[i]
	
	print(min1, min2)


def count_ele_less_mean(inp_list):
	list_mean = sum(inp_list) / len(inp_list)
	count = 0
	for i in range(0, len(inp_list)):
		if inp_list[i] < list_mean:
			count += 1

	return count


print(diff_two_mins([8.6, 9, 15, 20, 1, 5]))