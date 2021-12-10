word = "metallica";
knowing_letter = [];
hp = 10;
isWinner = False;

while hp > 0:
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

	if guess in word:
		knowing_letter.append(guess);
	else:
		hp -= 1;

if isWinner == False:
	print("You Lost :(");
else:
	print("You Won :)");
