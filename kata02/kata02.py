# -*- coding: utf-8  -*-

from helpers import time_me


# 1. classic iterative approach
@time_me
def binary_chop(int_target, int_list):
	""" does a binary search on a list and 
		returns index of the targeted element 
		from the list or -1 if not found

	:rtype: int"""
	
	not_found_value = -1
	if type(int_list) != list:
		raise TypeError
	if len(int_list) == 0:
		return not_found_value

	while int_list != []:
		list_middle_value = int_list[len(int_list) / 2]  # O(1)
		if list_middle_value == int_target:
			return list_middle_value - 1  # O(1)
		elif list_middle_value < int_target:
			int_list = int_list[len(int_list) / 2 + 1 : ]  # O(1)
		elif list_middle_value > int_target:
			int_list = int_list[:len(int_list) / 2]  # O(1)
	return not_found_value	        

# generation without tests:

#print(binary_chop(55, 'a_list'))
#print(binary_chop(55, []))
print(binary_chop(121, [i for i in xrange(1, 1000000)]))

