# Final project

import random

def level(difficult):
  counter=0
  if difficult=="easy":
    counter=10
  elif difficult=="hard":
    counter=5
  return counter

def guesses(counter):

  print(f"You have {counter} attemps left")
  while True:
    counter-=1
    yourno=int(input("Make a guess"))
    if counter==0:
      print("You lost all your attempts")
      break
    else:  
      if yourno==randomno:
        print("You won")
        break
      elif yourno<randomno:
        print("Too low")
      else:
        print("Too high")

      print(f"You have {counter} attemps left")

randomno=random.randint(1,100)
difficult=input("Choose you level(easy,hard): ")

count=level(difficult)
guesses(count)



