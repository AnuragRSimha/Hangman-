'''def KOTIGOBBA():
    b=['_','O','_','I','_','O','_','_','A']
    a=['K','O','T','I','G','O','B','B','A']
    print("Movie : ",' '.join(b))
    print("Health : 6")
    h=6
    for i in range(0,100):
        d=input("Enter letter : ").upper()
        if('K' in d):
            b.pop(0)
            b.insert(0,'K')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('T' in d):
            b.pop(2)
            b.insert(2,'T')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('G' in d):
            b.pop(4)
            b.insert(4,'G')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('B' in d):
            b.pop(6)
            b.insert(6,'B')
            b.pop(7)
            b.insert(7,'B')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('O' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('I' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('A' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        else:
            h=h-1
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        if(b==a):
            print("Game successfully completed")
            break
        if(h==0):
            print("Game over")
            print("Movie was :",' '.join(a))
            break
def KURUKSHETRA():
    b=['_','U','_','U','_','_','_','E','_','_','A']
    a=['K','U','R','U','K','S','H','E','T','R','A']
    print("Movie : ",' '.join(b))
    print("Health : 6")
    h=6
    for i in range(0,100):
        d=input("Enter letter : ").upper()
        if('K' in d):
            b.pop(0)
            b.insert(0,'K')
            b.pop(4)
            b.insert(4,'K')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('R' in d):
            b.pop(2)
            b.insert(2,'R')
            b.pop(9)
            b.insert(9,'R')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('S' in d):
            b.pop(5)
            b.insert(5,'S')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('H' in d):
            b.pop(6)
            b.insert(6,'H')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('T' in d):
            b.pop(8)
            b.insert(8,'T')
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('U' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('E' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        elif('A' in d):
            print("Letter already placed")
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        else:
            h=h-1
            print("Movie : ",' '.join(b))
            print("Health : ",h)
        if(b==a):
            print("Game successfully completed")
            break
        if(h==0):
            print("Game over")
            print("Movie was :",' '.join(a))
            break'''
def MOVIE():
    health={6:'O O O O O O',5:'O O O O O X',4:'O O O O X X',3:'O O O X X X',2:'O O X X X X',1:'O X X X X X',0:'X X X X X X [HANGED]'}
    z=[]
    x=['A','E','I','O','U',' ']
    y=[]
    il=[]
    cl=[]
    A=input("Enter your movie : ").upper()
    hint=input("Give some hint : ")
    language=input("Enter language : ").title()
    for i in range(100):
        print()
    for j in range(0,len(A)):
        z.append(A[j])
        y.append(A[j])
    for i in range(0,len(z)):
        if(z[i] not in x):
            z.pop(i)
            z.insert(i,'_')
    ac=[i for i in range(0,len(z)) if z[i]==' ']
    for i in ac:
        z.pop(i)
        y.pop(i)
        z.insert(i,'/')
        y.insert(i,'/')
    print("Movie : ",' '.join(z))
    print("Language : ",language)
    h=6
    print("Health :",health[h],"["+str(h)+"]")
    loop=0
    while(loop<1):
        d=input("Enter letter : ").upper()
        if(d in y):
            if(d in cl):
                print("Movie : ",' '.join(z))
                print("Health :",health[h],"["+str(h)+"]")
                print("Letter already placed. Used up correct letters : "+', '.join(cl)+"")
            else:
                cl.append(d)
                a=[i for i in range(0,len(y)) if y[i]==d]
                for i in a:
                    z.pop(i)
                    z.insert(i,d)
                print("Movie : ",' '.join(z))
                print("Health :",health[h],"["+str(h)+"]")
        elif(d not in y):
            if(d in il):
                print("Movie : ",' '.join(z))
                print("Health :",health[h],"["+str(h)+"]")
                print("Incorrect letter already used up. Used up incorrect letters : "+', '.join(il)+"")
            elif(d not in x):
                h=h-1
                il.append(d)
                print("Movie : ",' '.join(z))
                print("Health :",health[h],"["+str(h)+"]")
        if(d in x):
            if(d in y):
                print("Letter already placed")
            else:
                print("Vowels already displayed")
        if(h==2):
            print("Movie : ",' '.join(z))
            print("Hint : ",hint+".")
            print("Health :",health[h],"["+str(h)+"]")
        if(h==0):
            print("Game over")
            print("Movie was :",' '.join(y))
            break
        if(y==z):
            print("Game successfully completed")
            break
MOVIE()
            
            
                
    
    
    
            

            
