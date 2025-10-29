import sys
import time

def slow_typing(text, speed=0.05):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)
	print()
		
name = input ("Enter your name:").strip().capitalize()

slow_typing(f"Hello, {name}")
slow_typing("How are you?,Good/Bad", speed=0.1)

choice = input(">").strip().capitalize()

if choice == "Good":
	slow_typing("You feel happy, that means its your best day!")
	
elif choice == "Bad":
	slow_typing("oh sorry,i feel bad for you maybe someone needs a cheer up")
	
else:
	slow_typing("Error:This wasn't in my choice code sorry...")
	
slow_typing("what weather is today?, Hot/Cold/Normal")

choice = input (">").strip().capitalize()

if choice == "Hot":
	slow_typing("Whoa i think,you need some ice water or ice cream!")
	
elif choice == "Cold":
	slow_typing("Whoa so cold,i think you need a tea or coffee or something!")
	
elif choice == "Normal":
	slow_typing("ok you have a best weather today except for school.")
	
else:
	slow_typing("Error:This wasn't in my choice code sorry...")

slow_typing("how old are you?")

age = input ("age:").strip()

if age.isdigit():
	slow_typing(f"Oh your age is {age},and also nice to meet you {name}")
else:
	slow_typing("Error:This wasn't a age this is a word or letter!")
	
slow_typing("Is it AM/PM")

choice = input(">").strip().upper()

if choice == "AM":
	slow_typing("maybe our time is too early.")
	
elif choice == "PM":
	slow_typing("Oh,its Afternoon maybe you need some break.")
	
else:
	slow_typing("Error:This wasn't in my choice code sorry...")
	
slow_typing("What is your gender? Male/Female")

choice = input("gender:").strip().capitalize()

if choice == "Male":
	slow_typing("oh you are a boy")
	
elif choice == "Female":
	slow_typing("oh you are a girl")
	
else:
	slow_typing("Error:that wasn't in my code and also not a gender!")
	
slow_typing("Are you top in class?Yes/No")

choice = input(">").strip().capitalize()

if choice == "Yes":
	slow_typing("you got a lot friends there,huh")
	
elif choice == "No":
	slow_typing("oh,so you are just normal or bad")
	
else:
	slow_typing("Error:that wasn't in my choice code sorry...")
	
slow_typing("Did you do your homework today?Yes/No/Nohomework")

choice = input(">").strip().capitalize()

if choice == "Yes":
	slow_typing("oh,that's why you have time to play.")

elif choice == "No":
	slow_typing("Um,you should do your homework or your mom will kill you!")
	
elif choice == "Nohomework":
	slow_typing("oh that's great you have time to do something like play outside or... wait i forgot kids now always play in they're cellphone,those old days kids is always playing outside.....")
	
else:
	slow_typing("Error:That wasn't in my choice code sorry...")
	
slow_typing("do you have a pet?Yes/No")

choice = input(">").strip().capitalize()

if choice == "Yes":
	slow_typing("ok you have a pet.")
	slow_typing("What animal is your pet?")
	choice = input("Animal:").strip().title()

	slow_typing(f"oh that's your pet,{choice}")

	dangerous_animals = ['Crocodile', 'Alligator', 		'Wolf', 'Stray dog', 'Snake', 'Tiger', 'Lion']
	
	if choice in dangerous_animals:
		slow_typing("Whoa,that is dangerous 			animals!,well ok its your pet.")

elif choice == "No":
	slow_typing("oh you have no pet.")
	slow_typing("maybe,someday you'll get one!")
	
else:
	slow_typing("Error:That wasn't in my choice code sorry...")
	
#Game name:MyGame
slow_typing("do you want to play a game?")

choice = input(">").strip().capitalize()

if choice == "Yes":
	slow_typing("Great,now lets continue the game...")
	time.sleep(10)
	slow_typing("1+1=")
	choice = input(">").strip()
	if choice == "2":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("3+2=")
	choice = input(">").strip()
	if choice == "5":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error")
	slow_typing("53-6=")
	choice = input(">").strip()
	if choice == "47":
		slow_typing("Correct")
	elif choice.isdigit():
		slow_typing("Wrong")
	elif choice.isalpha():
		slow_typing("Error")
	slow_typing("9×9=")
	choice = input(">").strip()
	if choice == "81":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("56÷8=")
	choice = input(">").strip()
	if choice == "7":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("87278*@^×>+92718+×&<8×8×927×<^÷_÷72_&×÷82<÷÷^&#*@<=")
	choice = input(">").strip()
	if choice == "2014":
		slow_typing("Correct!,how did you do that?")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("Well thats for now goodbye.")
	
elif choice == "No":
	slow_typing("Well,maybe next time!")
	sys.exit()

else:
	slow_typing(f"Error:invalid Unexpected error no {choice} in the code!")
slow_typing("Round 2:")
time.sleep(2)
slow_typing("Do you want your Dream to come true?")

choice = input(">").strip().capitalize()

if choice == "Yes":
	slow_typing("Well you need pray to make it come true")
	
elif choice == "No":
	slow_typing("oh, ok")
	#MyDev a easter egg Game!
elif choice == "Thomas2014":
	slow_typing("you just unlock a secret game")
	time.sleep(2)
	slow_typing("What is @&^@!*!&+918179÷]×[×*&@*=")
	choice = input(">").strip().capitalize()
	if choice == "Dev_question":
		slow_typing("Correct!")
	elif choice.isalnum():
		slow_typing("Wrong!")
		sys.exit()
	slow_typing("What is the solution for _____")
	choice = input(">").strip().capitalize()
	if choice == "Dev_say_nothing":
		slow_typing("you got that one right!")
	elif choice.isalnum():
		slow_typing("you got that one wrong!")
		sys.exit()
	slow_typing("What is a Code thats never finished by a programmer?")
	choice = input(">").strip().capitalize()
	if choice == "Lazy_dev":
		slow_typing("You win!")
	elif choice.isalnum():
		slow_typing("You lose")
		sys.exit()

slow_typing("Which game do you want?Mymath/Myquiz")

choice = input(">").strip().capitalize()
#MyMath
if choice == "Mymath":
	slow_typing("3+2=")
	choice = input(">").strip()
	if choice == "5":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("9×9=")
	choice = input(">").strip()
	if choice == "81":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("47÷8")
	choice = input(">").strip()
	if choice == "5.875":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("8172718+(187÷3)×176=")
	choice = input(">").strip().capitalize()
	if choice == "8183688.6666667":
		slow_typing("Correct!")
	elif choice.isdigit():
		slow_typing("Wrong!")
	elif choice.isalpha():
		slow_typing("Error!")
	slow_typing("You win!")
	sys.exit()
#MyQuiz
elif choice == "Myquiz":
	slow_typing("When the dog bark what is it barking to?Someone/Something")
	choice = input(">").strip().capitalize()
	if choice == "Something":
		slow_typing("Correct!")
	elif choice == "Someone":
		slow_typing("Wrong!")
	else:
		slow_typing("Error!")
	slow_typing("What's it called when living things and non-living things are interacting?")
	choice = input(">").strip().capitalize()
	if choice == "Ecosystem":
		slow_typing("Correct!")
	elif choice.isalpha():
		slow_typing("Wrong!")
	else:
		slow_typing("Error!")
	slow_typing("Do you wanna learn Python?")
	choice = input(">").strip().capitalize()
	if choice == "Yes":
		slow_typing("Then go and ask chatgpt he might go and teach you!")
	elif choice == "No":
		slow_typing("oh, ok")
	else:
		slow_typing("Error!")
	slow_typing("Last question:Who created God?")
	choice = input(">").strip().capitalize()
	if choice == "No one":
		slow_typing("Correct!")
	elif choice.isalpha():
		slow_typing("Wrong!")
	else:
		slow_typing("Error!")
	time.sleep(5)
	slow_typing("do you know who created this game?Yes/No")
	choice = input(">")
	if choice == "Yes":
		slow_typing("oh,ok")
		sys.exit()
	elif choice == "No":
		slow_typing("Well the one that created this game is 'Thomas'.")
		slow_typing("The End.")
		time.sleep(5)
		slow_typing("Created by Thomas")
		slow_typing("Coded by Thomas")
		slow_typing("Uploaded by Thomas")
		slow_typing("MyCode")
		sys.exit()