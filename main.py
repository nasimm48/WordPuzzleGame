#Part1 : To create a csv file
# import csv
# import random
# with open('game.csv', mode='w',newline='') as game_file:
#  word_writer = csv.writer(game_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#  word_writer.writerow(['GuessWord', 'Clue', 'Description'])
#  word_writer.writerow(['tiger', 'a dangerous animal', 'wild'])
#  word_writer.writerow(['cat', 'not a dangerous animal', 'domestic'])
#  word_writer.writerow(['dog', 'a dangerous animal', 'domestic'])
#  word_writer.writerow(['elephant', 'not a dangerous animal', 'wild'])
#  word_writer.writerow(['deer', 'not a dangerous animal', 'wild'])
#  word_writer.writerow(['pecock', 'a colorful big bird', 'forest bird'])

#Part2 : To read a csv file
import csv
import random
from os import system
_= system('clear')
from getpass import getpass
intRandnum =0
totallines=0
RanddRow=[]
def funcTotalLine():
 with open('game.csv', mode ='r') as filecsv:   
  totallines = len(filecsv.readlines())
  filecsv.close()
 return totallines
totallines=funcTotalLine()
totallines=totallines-1
#print("Total lines are: ",totallines)
def funcRandNumGen(totallines):
 intRandnum = random.randint(0, totallines)
 return intRandnum
intRandnum = funcRandNumGen(totallines)
#print("Randomly selected line number : ", intRandnum)
def getrandonline(intRandnum):
 ctr=1
 with open('game.csv') as file_obj:
  reader_obj = csv.DictReader(file_obj)
  for row in reader_obj:
   if (ctr==intRandnum):
    RanddRow=row
   ctr=ctr+1
  file_obj.close()
 return RanddRow
#Main Function
RanddRow = getrandonline(intRandnum)
strGuessWord=RanddRow["GuessWord"]
intlengthOfGuessWord = len(strGuessWord)
strClue=RanddRow["Clue"]
strDescription=RanddRow["Description"]
print("****************************************************")
print("You are going to play 'GUESS A CHARACTER WORD PUZZLE GAME' (*) BEST OF LUCK (*)")
print("")
print("RULE: Maximum 5 wrong guesses are allowed ")
print("****************************************************")
print("Here we go: ")
getUserChoice = input("Do you want to play with a 'f'riend or a 'c'omputer ?. Type small letter 'f' or 'c' : ")
if getUserChoice=="f":
 print("User has selected 'f'")
 #Taking the word from the user in a mask mode
 wordProcessed = getpass(prompt='Please tell your friend to enter a word by hiding you : ')
elif getUserChoice=="c":
 print("You have selected 'c'")
 wordProcessed = strGuessWord
 print("Hint: Computer has typed ",strClue," which is ",strDescription)
else:
 print("Wrong selection, taking 'c' as your default choice: ")
 wordProcessed = strGuessWord
 print("Hint: Computer has typed ",strClue," which is ",strDescription)
#print(wordProcessed)
displayresult=[]
count=0
wordlength = len(wordProcessed)
FixedWordLength = wordlength
FixedWord = wordProcessed
while count<wordlength:
  displayresult.append("*")
  count=count+1
print("and the word which is having " , wordlength , " characters as ", displayresult)
ctrWrongEntries=0
#Run the loop until there are 5 wrong entries
while ctrWrongEntries<=4:
 GuessCharacter = input("Enter the guess character please: ")
 FindCharacter = wordProcessed.find(GuessCharacter)
 # if guessed character is inside the chosen word
 if FindCharacter >= 0:
  wordProcessed=wordProcessed.translate({ord(GuessCharacter): None})
  wordlength = len(wordProcessed)
  #print(wordlength)
  #print("Processed remaining word is : ",wordProcessed)
  #Program for replacing the star mark if found the match
  count=0
  while count<FixedWordLength:
   if FixedWord[count]==GuessCharacter:
    displayresult[count]=GuessCharacter
   count=count+1
  print("Nice Guess : ", displayresult)
 # if guessed character is not inside the chosen word
 else:
  ctrWrongEntries = ctrWrongEntries+1
  print("Sorry you entered a wrong character : ", ctrWrongEntries, " , please Guess again")
 if wordlength==0:
   print(wordlength)
   print("HURREYYY... YOU ARE WON...YOU ARE GREAT")
   break 
 if ctrWrongEntries==5:
   print("Ohh we are SORRY , you are lost, BETTER LUCK NEXT TIME")
   break
