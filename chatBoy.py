import re,random,string
#Method to check if a keyword is in the data base
# @retm list_games which consist in a like|game
# format
def isInIt(list,target,print): 
	my_RegExp = re.compile(r'[y,n]\|+[\w\s\"]*{0}[\w\s\"]*\|+'.format(target))
	matches = my_RegExp.finditer(list)
	counter = 0
	list_games = []
	for match in matches:
		if print:
			list_games.append(match.group(0)[2:-1].title())
			list_games.append(match.group(0)[0:1].title())
		counter += 1
	return list_games
#Method to learn and put it on the data base
def learn():
	usr_input = input("What was the complete name of the game?\n")
	game_genre = input("I don't know about that game, what is its genre? \n").lower()
	file_editor = open("data/games.txt",'a')
	if isInIt(data_string,game_genre,False) == 0: 
		new_taste = input("I don't know that genre, Do you like it?\n").lower()
		new_console = input("For which console?\n")
	else:
		new_taste = input("I know what you talking about!\nIs it a cool game? \n").lower()
		new_console = input("For which console is it?\n")

	if new_taste == "yes":
		file_editor.write("\ny|"+usr_input.title()+"|"+game_genre+"|"+new_console)
	elif new_taste == "no":
		file_editor.write("\nn|"+usr_input.title()+"|"+game_genre+"|"+new_console)
	file_editor.close()
	print("Thanks for the recomendation! :)")
# Random funciotn to pick a random game
# in case it need to access one
def randomGame():
	games_data = open("data/games.txt",'r')
	data_string = ""
	for line in games_data:
		data_string = data_string + line.lower()
	rando = random.choice(data_string)
	random_games = isInIt(data_string,rando,True)
	return random_games[0]

#Program stars
usr_input = input("I'm a chatBoy! Let's talk about videogames!\n")
#Parse input into something the pattern can understand
answer = ""
#To catch if it is a question
if usr_input[-1] == "?":
	usr_input = usr_input.replace('?','')
ranGame = randomGame()
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
	#If the word is not a keyword in data, it may be a keyword in games
	if not itemFound: 
		games_data = open("data/games.txt",'r')
		data_string = ""
		for line in games_data:
			data_string = data_string + line.lower()
		list_games1 = isInIt(data_string,item.lower(),True)
	lines.close()
#Verify if it is a valid pattern
format = open("data/format.txt",'r')
for pattern in format:
	spltPat = pattern.split("|")
	if spltPat[0] == new_format:
		answer = answer+spltPat[1].rstrip()
#Provides an answer depending on the pattern
if answer == "": #In case an answer was not found
	print("I did not get that")
# If more than one game match the one mentioned by the user
elif len(list_games1) > 1:
	while(True):
		try:
			likeCurrent = list_games1.pop()
			currentGame = list_games1.pop()
		except IndexError:
			learn()
			break
		usr_input = input("are you talking about "+currentGame+"\n")	
		if usr_input.lower() == "yes":
			if likeCurrent == "Y":
				print("I really like "+currentGame)
			else:
				print("I did not like "+currentGame)
			break
# If only one game matched the one mentioned by the user
else:
	likeCurrent = ""
	currentGame = ""
	try:
		likeCurrent = list_games1.pop()
		currentGame = list_games1.pop()
	except IndexError:
		print (answer+" "+ranGame)
	if likeCurrent == "Y":
		print("I really like "+currentGame)
	elif likeCurrent == "N":
		print("I did not like "+currentGame)
