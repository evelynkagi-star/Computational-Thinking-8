print("Hello! And welcome to the which Harry potter character are you?")
Ron_Weasley_points = 0
Hermione_Granger_points = 0
Harry_Potter_points = 0
input()
answer1 = input("If you were to pick a pet which one would you want A Rat B Cat C Owl")
if answer1 == "A" or answer1 == "a":
       Ron_Weasley_points += 1
elif answer1 == "B":
       Hermione_Granger_points += 1
elif answer1 == "C":
       Harry_Potter_points += 1
input()
answer2 = input("If you had free time what would you do A Eat B Study or C Play Quidditch")
if answer2 == "A":
       Ron_Weasley_points += 1
elif answer2 == "B":
       Hermione_Granger_points += 1
elif answer2 == "C":
       Harry_Potter_points += 1
input()
answer3 = input("What color would you chose A Red B Yellow or C Green")
if answer3 == "A":
       Ron_Weasley_points += 1
elif answer3 == "B":
       Hermione_Granger_points += 1
elif answer3 == "C":
       Harry_Potter_points += 1
input()
answer4 = input("Pick a class A Care of magical creatures B Potions C Defense against the dark arts ")
if answer4 == "A":
       Ron_Weasley_points += 1
elif answer4 == "B":
       Hermione_Granger_points += 1
elif answer4 == "C":
       Harry_Potter_points += 1
input()
answer5 = input("Pick a teacher A Lupin B Harid or C Dumbledore ")
if answer5 == "A":
       Ron_Weasley_points += 1
elif answer5 == "B":
       Hermione_Granger_points += 1
elif answer5== "C":
       Harry_Potter_points += 1
input()
if Ron_Weasley_points > Hermione_Granger_points and Ron_Weasley_points > Harry_Potter_points:
    print("You are most like Ron Weasley!")
if Hermione_Granger_points > Ron_Weasley_points and Hermione_Granger_points > Harry_Potter_points:
    print("You are most like Hermione Granger!")


    