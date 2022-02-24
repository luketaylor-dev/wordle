from ast import And
import pyautogui
import time
import keyboard
import random
from PIL import ImageGrab

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def GetPixelColor(point):
    image = ImageGrab.grab()
    color = image.getpixel((point.x, point.y))
    return color

def GetColor(colorCode):
    if colorCode  == (83, 141, 78):
        return  "G"
    elif colorCode  == (181, 159, 59):
        return  "Y"
    elif colorCode  == (58, 58, 60):
        return  "B"
    else:
        return "E"


def GetRowPoint(row, column):
    if row == 1:
        if column == 1:
            return Point(1144, 490)
        elif column == 2:
            return  Point(1232, 490)
        elif column == 3:
            return  Point(1288, 490)
        elif column == 4:
            return  Point(1341, 490)
        elif column == 5:
            return  Point(1412,  490)
    if row == 2:
        if column == 1:
            return Point(1144, 556)
        elif column == 2:
            return  Point(1232, 556)
        elif column == 3:
            return  Point(1288, 556)
        elif column == 4:
            return  Point(1341, 556)
        elif column == 5:
            return  Point(1412,  556)
    if row == 3:
        if column == 1:
            return Point(1144, 624)
        elif column == 2:
            return  Point(1232, 624)
        elif column == 3:
            return  Point(1288, 624)
        elif column == 4:
            return  Point(1341, 624)
        elif column == 5:
            return  Point(1412,  624)
    if row == 4:
        if column == 1:
            return Point(1144, 689)
        elif column == 2:
            return  Point(1232, 689)
        elif column == 3:
            return  Point(1288, 689)
        elif column == 4:
            return  Point(1341, 689)
        elif column == 5:
            return  Point(1412,  689)
    if row == 5:
        if column == 1:
            return Point(1144, 759)
        elif column == 2:
            return  Point(1232, 759)
        elif column == 3:
            return  Point(1288, 759)
        elif column == 4:
            return  Point(1341, 759)
        elif column == 5:
            return   Point(1412,  759)
    if row == 6:
        if column == 1:
            return Point(1144, 827)
        elif column == 2:
            return  Point(1232, 827)
        elif column == 3:
            return  Point(1288, 827)
        elif column == 4:
            return  Point(1341, 827)
        elif column == 5:
            return Point(1412,  827)
        
def CheckRow(row):
    colors = ['?', '?', '?', '?', '?']
    colors[0] = GetColor(GetPixelColor(GetRowPoint(row, 1)))
    colors[1] = GetColor(GetPixelColor(GetRowPoint(row, 2)))
    colors[2] = GetColor(GetPixelColor(GetRowPoint(row, 3)))
    colors[3] = GetColor(GetPixelColor(GetRowPoint(row, 4)))
    colors[4] = GetColor(GetPixelColor(GetRowPoint(row, 5)))
    return colors

def GetLetterPoint(letter):
        if(letter ==  "q"):
            return Point(1060, 1224)
        elif(letter ==  "w"):
            return Point(1106, 1224)
        elif(letter ==  "e"):
            return Point(1156, 1224)
        elif(letter ==  "r"): 
            return Point(1206, 1224)
        elif(letter ==  "t"):
            return Point(1257, 1224)
        elif(letter == "y"):
            return Point(1306, 1224)
        elif(letter ==  "u"):
            return Point(1349, 1224)
        elif(letter == "i"):
            return Point(1401, 1224)
        elif(letter == "o"):
            return Point(1450, 1224)
        elif(letter == "p"):
            return Point(1500, 1224)
        elif(letter == "a"):
            return Point(1080, 1293)
        elif(letter == "s"):
            return Point(1130, 1293)
        elif(letter == "d"):
            return Point(1180, 1293)
        elif(letter == "f"):
            return Point(1230, 1293)
        elif(letter == "g"):
            return Point(1280, 1293)
        elif(letter == "h"):
            return Point(1330, 1293)
        elif(letter == "j"):
            return Point(1380, 1293)
        elif(letter == "k"):
            return Point(1430, 1293)
        elif(letter == "l"):
            return Point(1480, 1293)
        elif(letter == "z"):
            return Point(1130, 1359)
        elif(letter == "x"):
            return Point(1180, 1359)
        elif(letter == "c"):
            return Point(1230, 1359)
        elif(letter == "v"):
            return Point(1280, 1359)
        elif(letter == "b"):
            return Point(1330, 1359)
        elif(letter == "n"):
            return Point(1380, 1359)
        elif(letter == "m"):
            return Point(1430, 1359)
        elif (letter == "enter"):
            return Point(1070, 1359)

def EnterWord(word):
    print(word)
    enterPoint = GetLetterPoint("enter")
    for x in word.lower():
        print(x)
        letterPoint = GetLetterPoint(x)
        pyautogui.click(letterPoint.x, letterPoint.y)
        time.sleep(.5)
    pyautogui.click(enterPoint.x, enterPoint.y)
    time.sleep(2.5)

def CheckColors(colors, startingWord):
    for x in range(5):
        if(colors[x] == 'Y'):
            yellowLetters[x].append(startingWord[x])
        elif(colors[x] == "G"):
            word[x] = startingWord[x]
        elif(colors[x] == "B"):
            blackLetters.append(startingWord[x])
    removing = True
    while removing:
      removing = False
      for b in blackLetters:
        bRemoved = False
        for g in word:
          if (b == g and not bRemoved):
            blackLetters.remove(b)
            bRemoved = True
            removing = True
        for yl in yellowLetters:
          for y in yl:
            if (y == b and not bRemoved):
              blackLetters.remove(b)
              bRemoved = True
              removing = True
                
def GetRemainingWords(lines):
    remains = []
    for line in lines:
        wordOkay = True
        for x in range(5):
            if wordOkay:
                if word[x] != '?':
                    if line[x].lower() != word[x].lower():
                        wordOkay = False
        for yl in  range(5):
            if wordOkay:
                for yellow in yellowLetters[yl]:
                  if line.find(yellow.lower()) == -1:
                    wordOkay = False
                  if line[yl] == yellow.lower():
                    wordOkay = False
        for black in  blackLetters:
            if wordOkay:
                if line.find(black.lower()) != -1:
                    wordOkay = False
        if wordOkay:
            remains.append(line)
    return remains

def CheckWin(wordList):
    win = True
    print(word)
    for x in word:
        if(x == '?'):
            win = False
    if win:
        print("win")
        print(wordList)
        exit()
        
def TakeTurn(turn, wordList):
    if(len(wordList) < 10):
      print(wordList)
    else:
      print(len(wordList))
    startingWord = random.choice(wordList)
    EnterWord(startingWord)
    colors = CheckRow(turn)
    CheckColors(colors, startingWord)
    CheckWin(wordList)
    return GetRemainingWords(wordList)

def main():
  f = open("WORDLE.txt", "r")
  r = f.read()
  remainWords = r.splitlines()
  print(word)
  pyautogui.click(200, 200)
  for x in range(6):
    remainWords = TakeTurn(x + 1, remainWords)
    print(yellowLetters)
    print(blackLetters)

word = ['?','?','?','?','?']
yellowLetters = [[],[],[],[],[]]
blackLetters = []
if __name__ == "__main__":
    main()

