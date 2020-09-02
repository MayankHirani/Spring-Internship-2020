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
import time

# Writes one-hot matrices from sequences in a file
def create_one_hot_matrices(file_name):

	matrices_dict = {}

	f = open(file_name)
	sequences = [ x.strip() for x in f.readlines() ]
	f.close()

	matrices = open('matrices.txt', 'w+')

	for index, sequence in enumerate(sequences):

		matrices_dict[sequence + str(index)] = [ ]

		one_hot_matrix = [ ]

		for letter in sequence:

			# Each letter assigned to a different matrix
			dict1 = {'A':[1,0,0,0], 'C':[0,1,0,0], 'T':[0,0,1,0], 'G':[0,0,0,1]}

			# Add the matrix to the list for writing to the file
			one_hot_matrix.append(dict1[letter])

			# Add to the overall dictionary
			matrices_dict[sequence + str(index)].append(dict1[letter])

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

	# Since frequency is dependent on the total number of sequences, we use this 
	# to find the total number of sequences for each iteration
	num = sum([x[0] for x in profile_matrix])

	# Same format as profile matrix, but using floats instead of ints
	pwm = np.zeros((4, 10), dtype=float)

	# Iterate through each row of the profile matrix
	for base in range( len(profile_matrix) ):

		# Go through each column of the profile matrix
		for position in range( len(profile_matrix[0]) ):

			# Add the position and bases probability of occuring (the value over the total)
			pwm[base][position] = profile_matrix[base][position] / num

	return pwm


# Takes input of a PWM and calculates the Information Content
def calculate_ic(pwm, qb):

	ic = 0

	# Iterate through each row (A, C, T, and G rows)
	for base in pwm:

		# Iterate through column (position k)
		for wbk in base:

			# Formula for the information content
			if wbk == 0:
				ic += 0
			else:
				ic += wbk * math.log2(wbk/qb) 

	return ic




# Create the sequences to calculate IC from
def create_sequences():

	f = open('sequences.txt', 'w+')

	# Create the pattern
	pattern = ''
	for x in range(10):

		pattern += random.choice(['T', 'C', 'G', 'A'])

	print("\n\nPattern we are trying to find: >> " +  pattern + " <<\n\n")

	# Create each sequence
	for x in range(100):

		sequence = ""

		for x in range(100):
			sequence += random.choice(['T', 'C', 'G', 'A'])

		# Starting index of the patter
		pat_start = random.randint(0, 89)

		# Number of errors in each pattern
		# (Implement afterwards)
		num_errors = random.randint(0, 3)

		# Chance for error
		e = 0.05

		# With chance e, alter the pattern
		prob = random.random()
		if prob < e:
			# Insert altered pattern because there is error
			sequence = sequence[0:pat_start] + alter_pattern(pattern) + sequence[pat_start+10:]
		
		else:
			# Before pattern + Pattern + Ending part
			sequence = sequence[0:pat_start] + pattern + sequence[pat_start+10:]
			
		

		f.write(sequence + '\n')

	f.close()


# Used to add an error into the pattern
def alter_pattern(pattern):

	altered_pattern = list(pattern)

	index = random.randint(0, 9)

	# Choose a random letter that is not its own
	letter = pattern[index]
	while letter == pattern[index]:
		letter = random.choice(['T', 'C', 'G', 'A'])

	altered_pattern[index] = letter
	altered_pattern = ''.join(altered_pattern)

	return altered_pattern

# Given two segments, calculate the ic of the pair
def calculate_pair_ic(segment1, segment2):

	filename = open('pair.txt', 'w+')

	filename.write(segment1)
	filename.write('\n')
	filename.write(segment2)
	filename.close()

	profilematrix = create_profile_matrix(create_one_hot_matrices('pair.txt'))
	ic = calculate_ic(create_pwm(profilematrix), 0.25)
	
	return ic, profilematrix


# Start with the first two sequences and find the segments with the highest ic,
# iterate through all sequences and keep track of highest IC
def find_pattern(file):

	sequences = [ x.strip() for x in open(file, 'r+') ]

	# Store:         Patterns         IC            Positions   Overall Freq. Matrix
	highest_ic = [ [None, None], -999999999, [0 for x in range(2)], None ]

	# Iterate through segments in sequence 1
	for start1 in range(91):
		end1 = start1 + 10

		segment1 = sequences[0][start1:end1]

		# Iterate through segments in sequence 2
		for start2 in range(91):
			end2 = start2 + 10

			segment2 = sequences[1][start2:end2]

			ic = calculate_pair_ic(segment1, segment2)[0]
			profilematrix = calculate_pair_ic(segment1, segment2)[1]


			if ic >= highest_ic[1]:

				highest_ic[0] = [segment1, segment2]
				highest_ic[1] = ic
				highest_ic[2][0] = start1
				highest_ic[2][1] = start2
				highest_ic[3] = profilematrix

	# Printing it
	print("After the first two sequences: ")
	time.sleep(2)
	print("Predicted Pattern:", evaluate_pattern(highest_ic[3]))
	print("Current Information Content:", highest_ic[1])
	print(highest_ic[3])
	print()


 	# -----------------------------------------------------------------------------
	# Part 2: Iterating through the rest of the sequences

	for sequence in sequences[2:]:

		# For each sequence we have the segment with the highest IC that we want to find
		sequence_highest_ic = 0

		# Related to above, this is the profile matrix for the highest IC segment
		best_profile_matrix = highest_ic[3].copy()
		
		# Iterate through the segments in the sequence
		for start in range(91):
			end = start + 10

			segment = sequence[start:end]

			# Profile matrix that we update to see if IC increases/decreases
			profilematrix = highest_ic[3].copy()

			f = open('pair.txt', 'w+')
			f.write(segment)
			f.close()

			# We want a matrix dictionary of the segment to update the profile matrix
			matrices_dict = create_one_hot_matrices('pair.txt')[segment + '0']

			# Update the profile matrix using the matrix dictionary
			for index, base in enumerate(matrices_dict):
				# Add a count to the correct position in the profile matrix
				profilematrix[base.index(1)][index] += 1

			# Compare if the IC was the highest for this sequence
			if calculate_ic(create_pwm(profilematrix), 0.25) >= sequence_highest_ic:

				# If this segment has the highest has the highest IC, save the IC
				# and the profile matrix in this sequence's temporary ones
				sequence_highest_ic = calculate_ic(create_pwm(profilematrix), 0.25)
				best_profile_matrix = profilematrix.copy()

		# With each sequence, after all the segments have been tested, update the one
		# with the largest increase (or smallest decrease) in IC value
		highest_ic[3] = best_profile_matrix
		highest_ic[1] = sequence_highest_ic


	# Printing it
	print("After " + str(sequences.index(sequence)+1) + " Sequences")
	time.sleep(3)
	print("Predicted Pattern:", evaluate_pattern(highest_ic[3]))
	print("Current Information Content:", highest_ic[1])
	print(highest_ic[3])
	print()


# Given a profile matrix, decide what the pattern must be (used at the end)
def evaluate_pattern(profilematrix):

	# Predicted pattern we make
	pattern = '0000000000'
	pattern = list(pattern)
	bases = ['A', 'C', 'T', 'G']

	for index in range(10):
		# Assign the highest occuring value in the column to a base
		column = [profilematrix[base][index] for base in range(len(bases))]
		pattern[index] = bases[column.index(max(column))]

	return ''.join(pattern)



