import re,random

def isInIt(list,target,print):
	my_RegExp = re.compile(r'\|+[\w\s\"]*{0}[\w\s\"]*\|+'.format(target))
	matches = my_RegExp.finditer(list)
	counter = 0
	list_games = []
	for match in matches:
		if print:
			#print(match.group(0)[1:-1].title())
			list_games.append(match.group(0)[1:-1].title())
		counter += 1
	return list_games

usr_input = input("I'm a chatBoy! Ask me something related to videogames!\n")

splt_str = usr_input.split(" ")
new_format = ''
list_games1 = [" "]
for item in splt_str:
	itemFound = False
	lines = open("data/words.txt",'r')
	for line in lines:
		splt_line = line.split("|")
		if item.lower() == splt_line[0].lower():
			new_format = new_format+splt_line[1].rstrip()
			itemFound = True
	if not itemFound:
		games_data = open("data/games.txt",'r')
		data_string = ""
		for line in games_data:
			data_string = data_string + line.lower()
		list_games1 = isInIt(data_string,item.lower(),True)

	lines.close()

format = open("data/format.txt",'r')

answer = ""

for pattern in format:
	spltPat = pattern.split("|")
	if spltPat[0] == new_format:
		answer = spltPat[1].rstrip()

if answer == "":
	print("I did not get that")
else:
	print(answer+" "+list_games1[0])