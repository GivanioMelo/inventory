import os
import TextColors

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def trim(s:str, size:int)-> str:
    if len(s) <= size: return s
    s2 = s[0:size-1] + '…'
    return s2

def clearScreen():
    os.system("cls")

def drawBox(x, y, w, h, color=TextColors.WHITE):
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
            print(TextColors.RESET,end="")

def drawDoubleBorderBox(x,y,w,h, color=TextColors.WHITE):
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
            print(TextColors.RESET,end="")

def drawBroadBorderBox(x,y,w,h, color=TextColors.WHITE):
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
            print(TextColors.RESET,end="")