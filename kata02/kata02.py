# -*- coding: utf-8  -*-

from helpers import time_me

@time_me
# 1. classic iterative approach
def binary_chop(int_target, int_list):
	""" does a binary search on a list and 
		returns index of targeted_element 
		from the list or -1 if not found

	:rtype: int"""
	
	not_found_value = -1
	if type(int_list) != list:
		raise TypeError
	if len(int_list) == 0:
		return not_found_value
	temp_int_list = int_list
	while temp_int_list != []:
		list_middle_value = temp_int_list[len(temp_int_list) / 2]
		if list_middle_value == int_target:
			return int_list.index(list_middle_value)
		elif list_middle_value < int_target:
			temp_int_list = temp_int_list[len(temp_int_list) / 2 + 1 : ]
		elif list_middle_value > int_target:
			temp_int_list = temp_int_list[:len(temp_int_list) / 2]
	return not_found_value	        

# generation without tests:

print(binary_chop(55, [i for i in xrange(1, 1000000000)]))
