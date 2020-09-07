# -*- encoding: utf-8 -*-

from functools import wraps
from time import time


def time_me(func):
    @wraps(func)
    def wrapper_closure(*args, **kwargs):
    	start_time = time()
    	func_res = func(*args, **kwargs)
    	end_time = time()
    	print("{}'s funning time: {:0.4e} s".format(wrapper_closure.__name__, end_time - start_time))
    	return func_res
    return wrapper_closure

