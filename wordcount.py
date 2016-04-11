def count_words_in_poem(file_name):
	count_words = 1
	poem_file = open(file_name)

	poem_dictionary = {}

	for line in poem_file:
		poem_bank = line.split(" ")
		for word in poem_bank:
			if word in poem_bank:
				count_words = poem_dictionary.get(word, 0)
				poem_dictionary[word] = count_words + 1	
	return poem_dictionary	

	# for each_word in poem_dictionary:				
	# 	if each_word == word:
	# 		poem_dictionary[each_word] = count_words + 1
	# 	else:
	# 		count_words = 0

	# file_name.close()
	# return poem_dictionary

print count_words_in_poem("test.txt")



						






