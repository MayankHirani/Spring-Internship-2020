"""
Spring Internship with Prof. Sinha & Shounak Bhogale (Summer part starting July 2020)
Mayank Hirani
mayank.hirani@icloud.com
"""


# All functions used in information_content.py

# Libraries
import random
import numpy as np
import math

# Writes one-hot matrices from sequences in a file
def create_one_hot_matrices(file_name):

	sequences = []
	matrices_dict = {}

	sequences = [ x.strip() for x in open(file_name, 'r+') ]

	matrices = open('matrices.txt', 'w+')

	for sequence in sequences:

		matrices_dict[sequence] = [ ]

		one_hot_matrix = [ ]

		for index, letter in enumerate(sequence):

			# Each letter assigned to a different matrix
			dict1 = {'A':[1,0,0,0], 'C':[0,1,0,0], 'T':[0,0,1,0], 'G':[0,0,0,1]}

			# Add the matrix to the list for writing to the file
			one_hot_matrix.append(dict1[letter])

			# Add to the overall dictionary
			matrices_dict[sequence].append(dict1[letter])

		matrices.write(str(one_hot_matrix) + '\n')

	return matrices_dict


# Takes input of one-hot matrices and turns them into a single profile matrix
def create_profile_matrix(matrices_dict):

	# Profile matrix, rows are each base [A, C, T, G], columns are each index of a pattern
	#                     (Bases, Length of Patterns)
	profile_matrix = np.zeros((4, 10), dtype=int)

	# Iterate through each pattern
	for pattern in matrices_dict.keys():

		# Each base tells whether it is ACTG with code [0,0,0,0], 1 where corresponding base is
		# base[index] == profile_matrix[index]
		for index, base in enumerate(matrices_dict[pattern]):

			# Add a count to the correct position in the profile matrix
			profile_matrix[base.index(1)][index] += 1

	return profile_matrix


# Takes input of the profile matrix and creates a Position Weight Matrix based on it
def create_pwm(profile_matrix):

	# Same format as profile matrix, but using floats instead of ints
	pwm = np.zeros((4, 10), dtype=float)

	# Iterate through each row of the profile matrix
	for base in range( len(profile_matrix) ):

		# Go through each column of the profile matrix
		for position in range( len(profile_matrix[0]) ):

			# Add the position and bases probability of occuring (the value over the total)
			pwm[base][position] = profile_matrix[base][position] / 100

	return pwm


# Takes input of a PWM and calculates the Information Content
def calculate_ic(pwm, qb):

	ic = 0

	# Iterate through each row (A, C, T, and G rows)
	for base in pwm:

		# Iterate through column (position k)
		for wbk in base:

			# Formula for the information content
			ic += wbk * math.log(wbk/qb, 2) 

	return ic


