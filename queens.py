import json

board=[]
size=8
solution=0
flag=0
r=1
print("\n 8-Queens Problem")

with open("input.json") as f:
    data=json.load(f);
c=data["start"]
board.append((r,c))


def danger(row,col):
    for (i,j) in board:
        if(row==i):
            return 1
        if(col==j):
            return 1
        if(abs(row-i)==abs(col-j)):
            return 1
    return 0

def placequeen(row):
    fl=0
    if(row>size):
        print_board()
    
    else:
        for col in range(1,size+1):
            if not danger(row,col):
                board.append((row,col))
                placequeen(row+1)
                board.remove((row,col))

def print_board():
    global flag,solution
    flag=1
    solution+=1
    print "\nSolution-",solution,":\n"
    for (i,j) in board:
        c=1
        while(c<j):
            print "|",
            print "_",
            c+=1
        print "|",
        print "Q",
        print "|",
        while(c<size):
            print "_",
            print "|",
            c+=1
        print "\n-------------------------------------"
    print "\n==========================================="
if(size>0):
    placequeen(2)
    if(flag==0):
        print("Solution does not exists")





