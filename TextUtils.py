import os

#Colors
RESET           = '\033[0m'

#Foreground colors
BLACK           = '\033[30m'
RED             = '\033[31m'
GREEN           = '\033[32m'
YELLOW          = '\033[33m'
BLUE            = '\033[34m'
MAGENTA         = '\033[35m'
CYAN            = '\033[36m'
LIGHT_GRAY      = '\033[37m'
DARK_GRAY       = '\033[90m'
BRIGHT_RED      = '\033[91m'
BRIGHT_GREEN    = '\033[92m'
BRIGHT_YELLOW   = '\033[93m'
BRIGHT_BLUE     = '\033[94m'
BRIGHT_MAGENTA  = '\033[95m'
BRIGHT_CYAN     = '\033[96m'
WHITE           = '\033[97m'

#Background colors
BG_BLACK    = '\033[40m'
BG_RED      = '\033[41m'
BG_GREEN    = '\033[42m'
BG_YELLOW   = '\033[43m'
BG_BLUE     = '\033[44m'
BG_MAGENTA  = '\033[45m'
BG_CYAN     = '\033[46m'
BG_GRAY     = '\033[47m'

def printColored(s:str, color:str = WHITE, end="\n"): print(color + s + RESET, end=end)
def printBlack(s:str, end="\n"):			printColored(s,BLACK, end=end)
def printRed(s:str, end="\n"):				printColored(s,RED, end=end)
def printGreen(s:str, end="\n"):			printColored(s,GREEN, end=end)
def printYellow(s:str, end="\n"):			printColored(s,YELLOW, end=end)
def printBlue(s:str, end="\n"):				printColored(s,BLUE, end=end)
def printMagenta(s:str, end="\n"):			printColored(s,MAGENTA, end=end)
def printCyan(s:str, end="\n"):				printColored(s,CYAN, end=end)
def printLightGray(s:str, end="\n"):		printColored(s,LIGHT_GRAY, end=end)
def printDarkGray(s:str, end="\n"):			printColored(s,DARK_GRAY, end=end)
def printBrightRed(s:str, end="\n"):		printColored(s,BRIGHT_RED, end=end)
def printBrightGreen(s:str, end="\n"):		printColored(s,BRIGHT_GREEN, end=end)
def printBrightYellow(s:str, end="\n"):		printColored(s,BRIGHT_YELLOW, end=end)
def printBrightBlue(s:str, end="\n"):		printColored(s,BRIGHT_BLUE, end=end)
def printBrightMagenta(s:str, end="\n"):	printColored(s,BRIGHT_MAGENTA, end=end)
def printBrightCyan(s:str, end="\n"):		printColored(s,BRIGHT_CYAN, end=end)

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def trim(s:str, size:int)-> str:
    if len(s) <= size: return s
    s2 = s[0:size-1] + '…'
    return s2

def clearScreen():
    os.system("cls")

def drawBox(x, y, w, h, color=WHITE):
    if (w <= 1) : return
    if (h <=1) : return
    for i in range(x , x + w):
        for j in range(y , y + h):
            gotoxy(i,j)
            print(color,end="")
            if i == x:
                if j == y: print('┌')
                elif j == y+h-1: print('└')
                else: print('│')
            elif i == x+w-1:
                if j == y: print('┐')
                elif j < y+h-1: print('│')
                else: print('┘')
            else:
                if j == y: print('─')
                elif j == y+h-1: print('─')
            print(RESET,end="")

def drawDoubleBorderBox(x,y,w,h, color=WHITE):
    if (w <= 1) : return
    if (h <=1) : return
    for i in range(x , x + w):
        for j in range(y , y + h):
            gotoxy(i,j)
            print(color,end="")
            if i == x:
                if j == y: print('╔')
                elif j == y+h-1: print('╚')
                else: print('║')
            elif i == x+w-1:
                if j == y: print('╗')
                elif j < y+h-1: print('║')
                else: print('╝')
            else:
                if j == y: print('═')
                elif j == y+h-1: print('═')
            print(RESET,end="")

def drawBroadBorderBox(x,y,w,h, color=WHITE):
    if (w <= 1) : return
    if (h <=1) : return
    for i in range(x , x + w):
        for j in range(y , y + h):
            gotoxy(i,j)
            print(color,end="")
            if i == x:
                if j == y: print('▛')
                elif j == y+h-1: print('▙')
                else: print('▌')
            elif i == x+w-1:
                if j == y: print('▜')
                elif j < y+h-1: print('▐')
                else: print('▟')
            else:
                if j == y: print('▀')
                elif j == y+h-1: print('▄')
            print(RESET,end="")

def drawRoundBorderBox(x,y,w,h, color=WHITE):
    if (w <= 1) : return
    if (h <=1) : return
    for i in range(x , x + w):
        for j in range(y , y + h):
            gotoxy(i,j)
            print(color,end="")
            if i == x:
                if j == y: print('╭')
                elif j == y+h-1: print('╰')
                else: print('│')
            elif i == x+w-1:
                if j == y: print('╮')
                elif j < y+h-1: print('│')
                else: print('╯')
            else:
                if j == y: print('─')
                elif j == y+h-1: print('─')
            print(RESET,end="")

def printTitle(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor)
	gotoxy(x,2)
	print(text)

def drawEditField(text:str, line:int, boxColor = WHITE, textColor = WHITE):
	drawBox(1,line,20,3,boxColor)
	drawBox(21,line,100,3,boxColor)
	gotoxy(2,line+1)
	printColored(text,textColor)

def drawInfoBox(text:str = "", textColor = WHITE):
	drawBox(1,27,120,3,DARK_GRAY)
	gotoxy(2,28)
	printColored(text, textColor, end="")

def inputxy(x:int, y:int, message:str) -> str:
    gotoxy(x,y)
    value = input(message)
    return value

def assureInput(message:str) -> str:
    while True:
        value = input(message)
        if value == "": print("Invalid Input, Try Again...")
        else: return value

def assureInputxy(x:int, y:int, message:str) -> str:
    while True:
        gotoxy(x,y)
        value = input(message)
        if value != "": return value

def inputIntxy(x:int, y:int, message:str) -> int:
    while True:
        gotoxy(x,y)
        try: value = int(input(message)); return value
        except: pass

def inputFloatxy(x:int, y:int, message:str) -> float:
    while True:
        gotoxy(x,y)
        try: value = float(input(message)); return value
        except: pass