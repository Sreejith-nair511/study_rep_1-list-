#this is a simplified code bash for creating a database for student 

s=[]#creating a list(empty)
while True:#condition put forward 
    print('enter name',len(s)+1,'or blank to stop')#len(s)+1 done to actually move the lolp forwrd 
    name=input()
    if name==":" :
        break
    s=s+[name]    
    print('student name are:')
    for name in s:
        print(name)
         