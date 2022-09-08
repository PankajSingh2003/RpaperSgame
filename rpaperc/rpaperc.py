import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
uchoose=input("Enter your choice: ")
cchoose=random.randint(0,2)
#0 be rock 1 be paper and 2 be scissors

print("Your choice")
if uchoose=="rock":
  print(rock)
elif uchoose=="paper":
  print(paper)
elif uchoose=="scissors":
  print(scissors)

print("Comupter choose")
if cchoose==0:
  print(rock)
elif cchoose==1:
  print(paper)
elif cchoose==2:
  print(scissors)




if uchoose=="rock":
  uchoose=3
elif uchoose=="paper":
  uchoose=4
else:
  uchoose=5

  #for rock
if uchoose==3 and cchoose==0:
  print("It's a draw")
elif uchoose==3 and cchoose==1:
  print("Computer wins")
elif uchoose==3 and cchoose==2:
  print("You win")

#for paper
if uchoose==4 and cchoose==1:
  print("It's a draw")
elif uchoose==4 and cchoose==0:
  print("You win")
elif uchoose==4 and cchoose==2:
  print("Computer win")
#for scissors
if uchoose==5 and cchoose==2:
  print("It's a draw")
elif uchoose==5 and cchoose==1:
  print("You win")
elif uchoose==5 and cchoose==0:
  print("Computer win")



