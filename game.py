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
show_tried_letter = False;
show_tried_letter_input = input("Do i show the tried letter ? (yes , no) : ");
if show_tried_letter_input in ["yes","y","evet","e"]:
	show_tried_letter = True;

with open(f"words_{language}.txt",mode="r") as isimler:
	word_list = isimler.read().split("\n");
	isimler.close();

word = word_list[random.randint(0,2445)].upper();
knowing_letter = [];
tried_letter = [];
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
	if show_tried_letter == True:
		print("Tried letter : "+",".join(tried_letter));
	guess = input("Your Guess : ");
	if guess == "i":
		guess = "İ"
	else:
		guess = guess.upper();

	if guess in word:
		knowing_letter.append(guess);
	else:
		tried_letter.append(guess);
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
