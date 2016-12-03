def parse_file(which_file):
	f = open(which_file)
	lines_in_file = f.readlines()
	words_list = []
	for i in range(len(lines_in_file)):
		words_list.extend(lines_in_file[i].split())

	return words_list
