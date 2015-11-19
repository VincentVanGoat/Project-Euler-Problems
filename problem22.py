names = open('names.txt', 'r+')
name_list_bad = names.readline().split(',')
name_list = [name_list_bad[i].split('"')[1] for i in range(0, len(name_list_bad))]

current_pos = 1
intermediate_score = 0
score = 0
for name in sorted(name_list):
	score += sum([ord(n) - 64 for n in name])*current_pos
	current_pos += 1 
print score