import os;
import random;
import platform;

if "Windows" in platform.platform():
	clear_command = "cls";
else:
	clear_command = "clear";

language = input("Your Language (en , tr) : ").lower();
while language != "en" and language != "tr":
	language = input("Your Language (EN , TR) : ").lower();

with open(f"words_{language}.txt",mode="r") as isimler:
	word_list = isimler.read().split("\n");
	isimler.close();

word = word_list[random.randint(0,2445)].upper();
knowing_letter = [];
hp = 10;
isWinner = False;

while hp > 0:
	os.system(clear_command);
	if len(set(word)) == len(set(knowing_letter)):
		isWinner = True;
		break;
	for n in word:
		if n in knowing_letter:
			print(n);
		else:
			print("-");
	print(f"Your HP : {hp}");
	guess = input("Your Guess : ");
	if guess == "answer":
		print(word);
		break;
	if guess == "i":
		guess = "İ"
	else:
		guess = guess.upper();

	if guess in word:
		knowing_letter.append(guess);
	else:
		hp -= 1;

if isWinner == False:
	os.system(clear_command);
	print(f"Word : {word}");
	print("--------------- ---------------");
	print("You Lost :(");
	print("--------------- ---------------");
else:
	os.system(clear_command);
	print(f"Word : {word}");
	print("--------------- ---------------");
	print("You Won :)");
	print("--------------- ---------------");
