import random as r
def hang(a):
    if a==0:
        print('''
             +------+ 
             O      |
                    |
                    |
                    |
                +=======+
''')
    if a==1:
        print('''
             +------+ 
             O      |
             |      |
                    |
                    |
                +=======+
''')
    if a==2:
        print('''
             +------+ 
             O      |
            /|      |
                    |
                    |
                +=======+
''')
    if a==3:
        print('''
             +------+ 
             O      |
            /|\     |
                    |
                    |
                +=======+
''')
    if a==4:
        print('''
             …
[11:57 pm, 29/04/2023] Ronak Gla: import random as r
l=[]
while 1:
    n=r.randint(1,6)
    if n==1:
        print('''
    * * * * * * * * *
    *               *
    *               *
    *       O       *
    *               *
    *               *
    * * * * * * * * *
''')
    elif n==2:
        print('''
    * * * * * * * * *
    *               *
    *               *
    *    O     O    *
    *               *
    *               *
    * * * * * * * * *
''')
    elif n==3:
        print('''
    * * * * * * * * *
    *               *
    *          O    *
    *       O       *
    *    O          *
    *               *
    * * * * * * * * *
''')
    elif n==4:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *               *
    *    O     O    *
    *               *
    * * * * * * * * *
''')
    elif n==5:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *       O       *
    *    O     O    *
    *               *
    * * * * * * * * *
''')
    elif n==6:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *    O     O    *
    *    O     O    *
    *               *
    * * * * * * * * *
''')
    
    if len(l)<6:
        l.append(n)
    else:
        v=l.pop(0)
        l.append(n)
    ch=input('Do you want to play Again ( Yes or No ) : ').capitalize()
    if ch=='Yes':
        continue
    elif ch =='No':
        break
    else:
        print("Enter a valid choice")