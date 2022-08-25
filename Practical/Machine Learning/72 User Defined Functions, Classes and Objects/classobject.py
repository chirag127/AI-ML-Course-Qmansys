# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:07:20 2020

@author: Bijoy Pal
"""

# Python program to 
# demonstrate instantiating 
# a class 


class Dog: 
	
	# A simple class 
	# attribute 
	attr1 = "mamal"
	attr2 = "dog"

	# A sample method 
	def fun(self): 
		print("I'm a", self.attr1) 
		print("I'm a", self.attr2) 

# Driver code 
# Object instantiation 
Rodger = Dog() 

# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
print(Rodger.attr2) 
Rodger.fun() 
