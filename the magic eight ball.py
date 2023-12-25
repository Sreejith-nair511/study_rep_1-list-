import random
message=['it is close enough','too far','too close','check your eyes',
         'bingo you got it']
print(message[random.randint(0,len(message)-1)])

name='zoya'
for i in name:#fun way of string printing 
    print('***'+ i+'***')

    #string and list have lot of similarity like indexing,slicing and in and not in operator 
    #but one major difference 
    #string is immuetable(values cant be changed and is fixed )
    #whereas in list,its muteable,the values can be changed and can be updated
    #example
    name='jojo'
    print(name[0:2]+'ho'+name[2:4])
    #the output obtain is just a copy of the,the original string is unchanged 
    
