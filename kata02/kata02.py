# -*- coding: utf-8  -*-

from __future__ import print_function

from helpers import time_me


# 1. approach:   classic iterative 
@time_me
def binary_chop(int_target, int_list):
	""" does a binary search on a list and 
		returns index of the targeted element 
		from the list or -1 if not found

	:rtype: int"""
	
	not_found_value = -1
	if type(int_list) not in (list, ):
		raise TypeError('{} is not list'.format(type(int_list)))
	if not len(int_list):
		return not_found_value
	start_index = 0
	end_index = len(int_list) - 1

	while start_index != end_index:
		arithmetic_mean = (start_index + end_index) / 2
		list_middle_value = int_list[arithmetic_mean]  # O(1)
		if list_middle_value == int_target:
			return arithmetic_mean  # O(1)
		elif list_middle_value < int_target:
			start_index = arithmetic_mean + 1  # O(1)
		elif list_middle_value > int_target:
			end_index = arithmetic_mean - 1  # O(1)
	#  start_index == end_index True. check for 2-dim lists case
	if int_list[start_index] == int_target:  # O(1)
		return start_index
	return not_found_value	        

# generation without tests:

#print(binary_chop(55, 'a_list'))
#print(binary_chop(55, []))
print(binary_chop(121, [i for i in xrange(1, 2 ** 20)]))
#print(binary_chop(7, [1, 3, 5, 7]))


# 2. approach:    binary_chop - recursive edition
@time_me
def binary_chop_rec(int_target, int_list, depth = 1):
	""" Does a binary search on a list and 
		returns index of the targeted element 
		from the list or -1 if not found
		
		This is a decorated recursive functions, thus, the first
		printed running time is for the last invoked function in the 
		recursive chain

	:rtype: int"""
	
	not_found_value = -1
	if type(int_list) not in (list, ):
		raise TypeError('{} is not list'.format(type(int_list)))
	if not len(int_list):
		return not_found_value
	
	# recursion stop condition
	if len(int_list) == 1: 
		leftover = int_list.pop()
		print('\ndepth: {}\n'.format(depth))
		return leftover - 1 if leftover == int_target else not_found_value
	print('\ndepth: {}'.format(depth))
	depth += 1
	
	list_middle_value = int_list[len(int_list) / 2]
	if list_middle_value == int_target:
		print('result: ', end='')
		return list_middle_value - 1
	elif list_middle_value < int_target:
		return  binary_chop_rec(int_target, int_list[len(int_list) / 2 + 1 :], depth)
	elif list_middle_value > int_target:
		return  binary_chop_rec(int_target, int_list[: len(int_list) / 2 ], depth)
	
#print(binary_chop_rec(55, 'a_list'))
#print(binary_chop_rec(55, []))
#print(binary_chop_rec(2, [1, 2]))
#print(binary_chop_rec(999, [i for i in xrange(1, 2 ** 10)]))
