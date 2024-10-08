'''Python Tutorials'''

'''1 Print Statement'''
# print("Hello World",7,"Shubh")
# print("2"*2)
# print(17-5)
# print(5)
# print("Shubh\nPathak")
# print("\"Shubh Pathak\"")
# print("Shubh", "Pathak", sep="~")
# print("Shubh", "Pathak", "Hello", sep="~", end="-\n")



'''2 Variables and Data Types'''
# a=1
# b="Shubh"
# c=True
# d=None
# e=1.0
# f=complex(1,2)
# print(a,b,c,d,e,f)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# Type Casting
# a=1 
# b=2.5
# c=a+b
# d=complex(1,2)
# print()   #throws error
# print(type(a+d))
# e=1.0
# print(int(a+b))
# print(type(c),c)  #Implicit Type casting

# print(float(a))  #Explicit Type casting
# print(int(e))



'''3 Operators'''
# print(10+2)
# print(10-2)
# print(10*2)
# print(10/3)
# print(20//3) #Floor division
# print(10%3)  #Modulo
# print(10**3) #Exponent



'''4 Type Casting'''
# a="2"
# b=int(a) #Explicit Type casting
# c="2"
# d=2.0
# e=2
# print(a)
# print(type(b))
# print(a+c)
# print(type(e+d)) #Implicit Type casting



'''5 User Input'''
# a=input("Enter Value")
# print(a)
# b=int(input("Enter Value"))
# print(b)



'''6 Strings (immutable)'''
# a='Shubh'
# print(a)
# a="Shubh"
# print(a)
# print(a[0],a[1],sep=".")
# a='"Shubh"'
# print(a)
# a="\"Shubh\""
# print(a)
# a='''Shubh
#     Pathak'''   #Multiline String
# print(a)



'''7 String Slicing'''
# name="Shubh,Pathak"
# print(len(name))
# print(name[0:5]) #0 included, 5 excluded
# print(name[:5])
# print(name[0:]) #same as name[0:len(name)]
# print(name[:])   #Same as name[0:len(name)]
# print(name[0:-3])  #this is same as print(name[0:len(name)-3])
# print(name[-3:-1])
# name="Shubh"
# print(len(name))
# print(name[-4:-2]) #this is same as print(name[1:3]) 
# print(type(name[-2:-4])) #this will give empty string



'''8 String Methods and Operations'''
''' Strings are immutable inplace'''
# a="Shubh"  
# print(len(a)) #this is a function
# print(a.upper())   #this is a new string #Converts to uppercase  #this is a method
# print(a.lower())   #Converts to lowercase
# a="!!!!!Shubh!!!!!$!!"
# print(a.rstrip("!")) #Returns new string after removing trailing characters (all occurence)
# print(a.strip("!")) #Returns new string after removing starting and trailing characters (all occurence)
# print(a.replace("Shubh","Pathak")) #replace one character with another
# print(a.replace("Pathak","Shubh"))
# a="Shubh Pathak"
# print(a.split(" ")) #Returns a list after splitting the string on the basis of entered parameter(Output:['Shubh', 'Pathak'])
# a=["shubh","pathak"]
# print(" ".join(a))  #this returns a list
# b="shubH"
# print(b.capitalize())   #Capitalize the 1st character and lower the other characters.

# c="Hello World in python"
# print(len(c))
# print(c.center(50,','))#aligns the string to center as per the parameter (Output:,,,,,,,,,,,,,,Hello World in python,,,,,,,,,,,,,,,)
# print(len(c.center(50)))            

# d="Shubh Shubh Shubh 01"
# print(d.count("Shubh")) #Counts number of occurence of given character or string (Output:3)

# print(d.endswith("bh"))  #Returns true if the string ends with the given parameter else false (Output:False)
# print(d.startswith("bh"))  #Returns true if the string starts with the given parameter else false (Output:False)

# print(d.endswith("ub",1,4)) #Returns true if the string ends with the given parameter in the given range else false; 1 include, 4 excluded;

# print(d.find("ub")) #Gives index of first occurence of give value else -1 (Output:2)
# print(d.find("P")) #Gives index of first occurence of give value else -1  (Output:-1)

# print(d.index("ub")) #It is similar to find but it raises exception if value is not present in the string  (Output:2)
# print(d.index("P")) #It is similar to find but it raises exception if value is not present in the string  (Output:ValueError: substring not found)

# d="ShubhShubhShubh01"
# print(d.isalnum()) #returns true if string is alpha numeric ellse false it does not considers space as aplha or numeric(Output:True)
# print(d.isalpha()) #returns true if string is alphabet ellse false it does not considers space as aplha or numeric(Output:False)

# e="Shubh"
# print(e.isprintable()) #returns true if all characters of given string is printable else false(Output:True)
# e="Shubh\n"
# print(e.isprintable()) #returns true if all characters of given string is printable else false(Output:False since \n is not printable)

# e="     "#using space
# print(e.isspace()) #returns true if whitespace is present either using space bar or tab (Output: True)
# e="        "#using tab
# print(e.isspace())   #(Output: True)

# e="Shubh pathak is a boy"
# print(e.istitle()) #returns true is each first character of each word of the string is capital else false (Output:False) 
# print(e.title()) #Converts given string into title case
# e="Shubh Pathak Is A Boy"
# print(e.istitle()) #returns true is each first character of each word of the string is capital else false (Output:True) 

# e="shubh"
# print(e.isupper()) #returns true if all characters are in upper case (Output:False)
# print(e.islower()) #returns true if all characters are in lower case (Output:True)
# print(e.swapcase()) #Converts lower to upper and vice versa



'''9 If Else'''
#Conditional Operators: >,<,==,!=,>=,<=
# a=int(input("Enter your age: "))
# if(a>=18):
#     print("You can drive")
# else:
#     print("You cant drive")



'''10 Nested if else'''
# n=int(input("Enter a  number: "))
# if(n>0):
#     print("+ive")
#     if (n%2==0):
#         print("Even +ive")
#     else:
#         print("Odd +ive")
# elif(n==0):
#     print("Zero")
# else:
#     print("-ive")
#     if (n%2==0):
#         print("Even -ive")
#     else:
#         print("Odd -ive")



'''Exercise 1'''
'''Greeting Application'''
# import time
# t=time.strftime("%H:%M:%S")
# h=int(time.strftime("%H"))
# m=int(time.strftime("%M"))
# s=int(time.strftime("%S"))
# if(h>0 and h<12):
#     print("Good Morning")
# elif(h>12 and h<16):
#     print("Good Afternoon")
# elif(h>16 and h<20):
#     print("Good Evening")
# else:
#     print("Good Night")
# print(t)



'''11 MatchCase Statements'''
# Same as switch case of Java and C++ 
# a=int(input("Enter a number: "))
# if(a%2==0):
#     f=1
# else:
#     f=2

# match f:
#     case 1:
#         print("Even")
#     case 2:
#         print("Odd")
#     case _:                       #Default case
#         print("Invalid")
# break statement is not required in MatchCase



'''12 For Loop'''
# n="Shubh"
# for i in n:
#     print(i)

# for i in range(1,11,2):    #(start,end-1,step)
#     if i%2==0:
#         print(i, " Even")
#     else:
#         print(i," Odd")

# c=["Red","Green","Blue"]
# for i in c:
#     print(i)
#     for z in i:
#         print(z)

# for i in range(-1,-20,-2):           #works with neg index aswell
#     print(i)


'''13 While Loop'''
# n=int(input("Enter a number: "))
# i=1
# while (i<=n):
#     print(i)
#     i=i+1

# i=5
# while(i>=0):
#     print(i)
#     i=i-1
#     exit()
# else:
#     print("Outside of while and inside else")



'''14 Break and Continue'''
# for i in range(1,12):
#     if (i==11):
#         break    #Exit the loop
#     print("5 x ",i ,"=", 5*i)

# for i in range(1,12):
#     if (i==11):
#         continue  #Skip the iteration
#     print("5 x ",i ,"=", 5*i)  



'''15 Emulating Do While Loop'''
# n=int(input("Enter a Number: "))
# i=1
# while True:
#     print(n,"x",i,"=",n*i)
#     i=i+1
#     if(i==11):
#         continue   #this iteration will be skipped
#     if(i==15):
#         break      #loop will be exited



'''16 Functions'''
''' Function :can have many parameters ; exists on its own; called as: function() and #we create methods not functions in our program.
    Eg: length(len) function to get the length
    Method: the object is one of its parameters; belongs to a certain claass; called as: object.method().
    Eg: append in a list is the usecase of method where object is passed a.append()'''
# def sum(l):
#     c=0
#     for i in l:
#         c=c+i
#     return c

# def average(l):
#     c=sum(l)
#     avg=c/len(l)
#     return avg

# l={1,2,3,4,5,6}
# print(average(l))


# def multiply(a,b):
#     pass                #used to just define the function body

# a=10
# b=2

# def multiply(a,b):
#     return a*b

# print(multiply(a,b))



'''17 Function Arguments and Return Statement'''
'''Types of Arguments:
    1 Default Arguments; 2 Keyword Arguments; 3 Variable Length Arguments; 4 Required Arguments
'''
# # Required Arguments
# def average(a,b=1):
#     c=a+b
#     avg=c/2
#     return avg
# print(average(1)) #value of a is required, b is user choice

# def average(a=1,b):    #a default parameter can't follow a non default parameter
#     c=a+b
#     avg=c/2
#     return avg
# print(average(1,2)) #throws SyntaxError: non-default argument follows default argument

# # Default Arguments
# def average(a=9,b=1):
#     c=a+b
#     avg=c/2
#     return avg
# print(average(1))  #a will be assigned 1 and b will take the deafault argument 1

# # Keyword Arguments
# print(average(b=1,a=9))   #order of parameter is not necessary

# # Variable Length Arguments
# def average(*n):   # *n is taken as tuple and **n is taken as dictionary
#     print(type(n))   #Output: <class 'tuple'>
#     c=0
#     for i in n:
#         c=c+i
#     avg=c/len(n)
#     return avg
# print(average(1,2,3,4))   #we can pass any number of arguments


# def name(**l):   #**l is taken as dictionary
#     print(type(l))
# name(n1="Shubh",n2="Ananya")

# def s(a,b):
#     print(a)
# l=[1,2,3,4]
# s(l,2)
# *args and **kwargs


'''18 List: Ordered Collection of Homogeneous Data Items stored in [] and are mutable
alphabets =["a",     "b",    "c",     "d",     "e"]
            [0]      [1]     [2]      [3]      [4]
alphabets =["a",     "b",    "c",     "d",     "e"]
            [-5]    [-4]    [-3]     [-2]      [-1]   '''
# l=[1,2,3]
# print(type(l))  #Output:<class 'list'>
# print(l[0],l[1],l[2],sep="-")  #Indexing starts from 0

# l=[1,"2",True,4.0,None]        #Can store different data types
# print(l[0],l[1],l[2],l[3],sep="-")
# print(len(l))
# print(l[-2])     #Same as l[len(l)-2]
# print(l[len(l)-2])
# print(l[3])

# print(1 in l) #Used to find an element in list returns true or false same thing applies for Strings

# #List Slicing listName[start : end : jumpIndex] 
# l=[1,2,3]
# print(l[0:3]) #Start from 0 and 3 is excluded same as string
# print(l[0:-2]) #Same as l[0:len(l)-2]
# print(l[0:len(l):2]) #Jump 2
# print(l[0:]) #Same as l[0:len(l)]
# print(l[:2])  #Same as l[0:2]
# print(l[:])  #Same as l[0:len(l)]

# #List Comprehension : List = [Expression(item) for item in iterable if Condition]   
# l=[i for i in range(10)]
# print(l)
# l=[i*i for i in range(10)]
# print(l)
# l=[i for i in range(10) if i%2==0]
# print(l)

# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[i**2 for i in l if i%2==0]
# print(l1)

# l=['1','2','3','4']
# s="".join(l)                               #used to convert list to string
# print(s)
# print(list(s))                             #used to convert string to list 




'''19 List Methods'''
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)
# l.append(11) #used to add elements
# print(l)
# l.sort() #used to sort list in ascending order; original list is updated
# print(l)
# l.reverse() #reverse list; original list is updated
# print(l)
# l.sort(reverse=True) #used to sort list in descending order; original list is updated
# print(l)

# print(l.index(7)) #returns index of first occurence of given element
# print(l.index(7,2,7)) #This will give index 6 since python will search 7 in between index 2(included) and 7(excluded)
# print(l.index(7,2,5)) #This will give error since python will search 7 in between index 2(included) and 5(excluded)

# print(l.count(1)) #returns num of times an element is present in the list
# l=[1,2,3,4,5,6,7,8,9,10]
# m=l #m is a reference of l any change in m will change l  #shallow copy
# m[0]=0 #0th index of l will be changed
# print(l)

# l=[1,2,3,4,5,6,7,8,9,10]
# m=l.copy() #used to create copy of list  #deep copy
# m[0]=0 #0th index of l will be changed
# print(m)
# print(l)


# l.insert(2,100) #insert an element at specified index .insert(index,element)
# print(l)

# m=[100,200,300]
# l.extend(m)  # join second list to first list i.e l is changed
# print(l) 
# print(m)

# k=l+m #this will not edit l but create a new list k
# print(l)
# print(m)
# print(k)



'''20 Tuples: Ordered Collection of Heterogeneous Data Items stored in () and are immutable'''
# t=(1,2,3,4,5)
# print(type(t), t)
# t=(1)
# print(type(t), t) #this will return type as int so we need to add , after 1 element to make sure its tuple
# t=(1,)
# print(type(t), t) #this will return type as tup so we need to add , after 1 element to make sure its tuple

# t[0]=11
# print(t) #This will give error as tuple is immutable

# print(t[0:len(t)])
# print(t[0:-2]) #Same as t[0:len(t)-2]
# print(t[0:len(t)-2]) 
# print(t[0:len(t):2]) #Jump 1 elements

#Tuple unpacking
# t=(1,2,3,4,5)
# (a,b,c,d,e)=t          #tuple unpacking
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# def add(*args):
#     a=args[0]
#     print(a)
#     (a,b,c)=args        #tuple unpacking
#     print(a)
#     print(b)
#     print(c)
# add(1,2,3)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits            #last three will be added in red as list
# print(green)
# print(yellow)
# print(red)

#Tupple Zipping
# t1=(1,2,3)
# t2=(4,5,6)
# t3=zip(t1,t2)
# print(type(zip(t1,t2)),zip(t1,t2))
# l=set(t3)
# print(l)

# for i in l:
#     print(i)

#Tupple Unzipping
# t1=(1,2,3)
# t2=(4,5,6)
# t3=zip(t1,t2)   
# c1,c2=zip(*t3)
# print(c1)
# print(c2)



'''21 Tuple Methods'''
# t=(1,2,3,4,5,6,7,8)
# print(t)

# l=list(t)       #To edit a tuple convert it to list and then performs functions on it and then convert it back to tuple
# l.append(9)
# l.pop(2)        #this will remove element at inex 2
# t=tuple(l)
# print(t)

# t2=(9,10,11)
# t3=t+t2          #Creating a new tuple
# print(t3)

# print(t.count(7)) #Count number of occurence of given element in tuple
# print(t.index(7)) #returns index of first occurence of given element
# print(t.index(7,2,7)) #This will give index 6 since python will search 7 in between index 2(included) and 7(excluded)
# print(t.index(7,2,5)) #This will give error since python will search 7 in between index 2(included) and 5(excluded)


'''Exercise 2'''
'''Create a Quiz'''
# import random
# Ques=["What country has the highest life expectancy?","Where would you be if you were standing on the Spanish Steps?","Which language has the more native speakers: English or Spanish?","What is the most common surname in the United States?","What disease commonly spread on pirate ships? ","Who was the Ancient Greek God of the Sun? ","What was the name of the crime boss who was head of the feared Chicago Outfit?","What year was the United Nations established? ","Who has won the most total Academy Awards?","What artist has the most streams on Spotify?"]
# Ans=["Hong Kong","Rome","Spanish","Smith","Scurvy","Apollo","Al Capone","1945","Walt Disney","Drake",]
# l=[] #List to store ques numbers
# p=0
# while(True):
#     n=input("Enter y to play game else enter n: ")
#     if n=='n':
#         break
#     else:
#         q=random.randint(0,len(Ques)-1) #generates random number between the given range both included
#         l.append(q)
#         print(Ques[q])
#         a=input("Enter Answer: ")
#         if a==Ans[q]:
#             print("Correct answer.Bravo!")
#             p=p+100
#             print("Current Points: ",p)
#         if a!=Ans[q]:
#             print("Wrong answer.Try again!")
#             p=p-100
#             print("Current Points: ",p)
    
# if p<0:
#     p=0
# print("Final Points: ",p)



'''22 f Strings'''
# s="My name is {} and I am {} years old."
# n="Shubh"
# a="22"
# print(s.format(n,a))   #String formatting old way

# print(f'My name is {n} and I am {a} years old..')   #f strings new way
# print(f'My name is {{n}} and I am {{a}} years old..')   #f strings new way

# a=2.333333
# print(a)
# print("{:.2f}".format(a))
# print(f"{a:.2f}")


'''23 DocStrings and Pep-8'''
# def sum(l):
#     '''Returns sum of all elements of list'''     #written right below function name and right above function body
#     c=0
#     for i in l:
#         c=c+i
#     return c
# def average(l):
#     '''Returns average of the list passed'''
#     c=sum(l)
#     a=c/len(l)
#     return a
# l=[1,2]
# average(l)
# print(average.__doc__) 
# print(sum.__doc__)


#PEP- 8: Python Enhancement Proposals
# import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!



'''24 Recursions'''
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# a=int(input("Enter number: "))
# print(factorial(a))

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# a=int(input("Enter number: "))
# print(fibonacci(a))



'''25 Sets are unordered collection of data items, enclosed within curly brackets {}. 
        Sets are unchangeable, and do not contain duplicate items.'''
# s={2,4,5,3,1}
# print(s)
# i={1,"2",False,3.9,3.9} 
# print(i) #only single 3.9 will be printed

# a={}           #this is dictionary not an empty set
# print(type(a)) #this will give <class 'dict'> 
# a=set()        #this is how we create empty set
# print(type(a)) #this will give <class 'set'>   



'''26 Set Methods'''
# s1={10,17,22,34}
# s2={5,13,34,49}

# print(s1.union(s2))        #this will give union of both the set , this will create new set
# print(s1.intersection(s2)) #this will give intersection of both the set, this will create new set

# s1.update(s2)              #this will add elements of s2 in s1    same as list extend method
# print(s1)
# # print(s2)
# s1.intersection_update(s2)   #this will update s1 with elements that are common in both sets
# print(s1)
# print(s2)

# print(s1.symmetric_difference(s2))  #this will return  (s1 union s2)-(s1 intersection s2)
# s1.symmetric_difference_update(s2)   #this will update s1 with  (s1 union s2)-(s1 intersection s2)
# print(s1)

# print(s1.difference(s2))  #this will return s1-s2
# s1.difference_update(s2)  #this will update s1 with s1-s2
# print(s1)

# s1={1,2,3,4}
# s2={2,3}  
# s3={5}
# print(s1.isdisjoint(s3))  #checks if items of given set are present in another set
# print(s1.issuperset(s2))  #checks if all the items of a particular set are present in the original set
# print(s2.issubset(s1))    #checks if all the items of the original set are present in the particular set

# s1={1,2,3,4}
# s2={6}
# s1.add(5)          #this will add only single element in set
# print(s1)
# s1.update(s2)      #this will add s2 to s1
# print(s1)
# s1.remove(6)       #this will remove an element from set. If element is not present in set and error will be thrown.
# print(s1)
# print(s1)
# s1.discard(5)      #this will also remove an element from set. If element is not present in set and no error will be thrown.
# print(s1)
# p=s1.pop()         #this removes the last item of the set but we don’t know which item gets popped as sets are unordered.
# print(s1)
# print(p)
# # del s2           #del keyword deletes the set entirely.
# # print(s2)
# # s2.clear()       #this clears all items in the set and prints an empty set.   
# # print(s2)
# print(6 in s2)     #this check if an item exists in the set or not                



'''27 Dictionary '''
''' They are ordered collection of data items.
    They store multiple items in a single variable. 
    Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}'''
# d={
#     1:"Matt",
#     2:"Rob",
#     3:"Jack",
#     4:"Dolph"
#     }
# print(d)
# print(d[1])     
# print(d.get(1)) 
# print(d[5])     #if key does not exist it will give error (Output: KeyError: 5)
# print(d.get(5)) #if key does not exist it will give none  (Output: None)

# print(d.keys())   #print all the keys in the dictionary
# print(d.values()) #print all the values in the dictionary
# for k in d.keys():
#     print(f"For Key {k} value is {d[k]}")

# print(d.items())  #print all the key-value pairs in the dictionary
# for k,v in d.items():
#     print(f"For Key {k} value is {v}")



'''28 Dictionary Methods'''
# d1={
#     1:"Matt",
#     2:"Rob",
#     3:"Jack",
#     4:"Dolph"
#     }
# d2={
#     5:"Mark",
#     6:"Jey",
#     7:"Jimmy"
# }
# d3={}          #empty dict
# d1.update(d2) #this will add d2 to d1
# print(d1)
# print(d2)

# d2.clear()    #this removes all items from the dict d2
# print(d2)

# d2.pop(6)       #this removes the item with corresponding key passed   
# print(d2)
# d2.popitem()    #this removes the last item from dict
# print(d2)

# del d3          #del keyword deletes the dict entirely.
# print(d3)

# del d1[1]           #this deletes the item with corresponding key passed
# print(d1)



'''29 for and while Loop with else'''
# for i in range(0,4):
#     print(i)
# else:                              #this else will only be executed when the all all the iterations are completed                                 
#     print("Out of loop")


# for i in range(0,4):
#     print(i)
#     if (i==2):
#         break
# else:                              #this time else will not be executed since the loop is terminated in between and all iterations are not completed
#     print("Out of loop")


#Similarly for while loop else will only execute if all iterations are done completely
# i=0
# while(i<5):
#     print(i)
#     i=i+1
# else:                               #this else will only be executed when the all all the iterations are completed  
#     print("Out of loop")

# i=0
# while(i<5):
#     print(i)
#     i=i+1
#     if i==2:
#         break
# else:                               #this time else will not be executed since the loop is terminated in between and all iterations are not completed
#     print("Out of loop")



'''30 Exception Handling'''
# n=input("Enter a number: ")
# print(f"Multiplication table of {n}:")

# try:
#     for i in range(1,11):
#         print(f"{int(n)} x {i} = {int(n)*i}")

# # except Exception as e:
# #     print(e)

# except :
#     print("Invalid input!")        #we can also give custon error msg

# print("Some other piece of code!!")
# print("Some other piece of code!!")

#Handling multiple exceptions
# try:
#     n=int(input("Enter a number: "))   #if error occurs here ValueError will be triggered
#     a=(1,2)
#     print(a[n])                         #if error occurs here IndexError will be triggered

# except ValueError:
#     print("Invalid value entered!")

# except IndexError as i:
#     print("Index out of bound!!")
#     print(i)



'''31 Finally Clause'''
# def func(n):
#     try:
#         a=[1,2,3,4]
#         return(a[int(n)])

#     except ValueError as v:
#         return v

#     except IndexError as i:
#         return i

#     finally:
#         print("Finally is always be executed!!")      #this will always be executed in any situation

#     # print("Finally is always be executed!!")        #but this will not be excuted since it comes after return statetment this is the diff between code written in finally block and code written normally

# n=input("Enter index: ")
# print(func(n))



'''32 Raising custom errors'''
# a=int(input("Enter number between 4 and 6 : "))

# if (a<4 or a>6):
#     raise ValueError("Value should be between 4 and 6")     #raise keyword help us to raise custom errors

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass

# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
        
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")



'''Exercise 3'''
'''Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode'''
# import random
# import string
# def encode(s):
#     e=""
#     l=[]
#     if len(s)<=3:
#         e=s[::-1]
#         return e
#     else:
#         s=s[1:]+s[0]
#         z=""
#         for i in range(0,3):
#             n=random.choice(string.ascii_letters)             #gives random letters
#             z=z+n.lower()
#         s=z+s+z
#         return s

# def decode(s):
#     d=""
#     l=[]
#     if len(s)<=3:
#         e=s[::-1]
#         return e
#     else:
#         s=s[-4]+s[3:-4]
#         return s

# s=input("Enter a string: ")
# print("Encoded Text: ",encode(s))
# print("Decoded Text: ",decode(encode(s)))



'''33 Short Hand if else'''
# a=3
# b=3
# print("B is greater") if b>a else print("A is greater") if a>b else print("A is equal to B")

# c=1 if b>a else -1 if a>b else 0
# print(c)

# above code is similar to below code

# if b>a:
#     c=1
# elif a>b:
#     c=-1
# else:
#     c=0
# print(c)



'''34 Enumerate Function'''
# a=[1,2,3,4,5,6]

# for index,m in enumerate(a):        #this get the index and value of each element in the sequence 
#     print(index,m)
#     if(index==3):
#         print("Index 3")

# for index,m in enumerate(a,start=1):      #By default, the enumerate function starts the index at 0 but we can change this using start parameter
#     print(index,m)
#     if(index==3):
#         print("Index 3")



'''35 Virtual Environment'''
'''A virtual environment is a tool used to isolate specific Python environments on a single machine, 
allowing you to work on multiple projects with different dependencies and packages without conflicts.'''

#For Windows
# for making a new environment (same)->  python -m venv dir_name
# for activation  of that environment->  dir_name\Scripts\activate.bat(for shell)
# for activation  of that environment->  dir_name\Scripts\activate.ps1(for powershell)
# for deactivation  of that environment-> deactivate
# for checking version in windows-> python --version
# for checking version in linux-> python3 --version

#For Mac
# for making a new environment (same)->  python -m venv dir_name
# for activation  of that environment->  source myenv/bin/activate
# for deactivation  of that environment-> deactivate

#Requirement.txt
# pip freeze > requirements.txt    #outputs a list of installed packages and their versions
# pip install -r requirements.txt  #installs the packages listed in the requirements.txt

# To create conda environment use 'conda create -p venv python==3.10 -y'
# To activate conda environment use 'conda activate venv/'  
# To deactivate conda environment use 'conda deactivate '




'''36 Import Keyword'''
# import math
# print(math.floor(4.6))

# from math import sqrt
# print(sqrt(9))
# from math import sqrt as s
# print(s(9))

# from math import *
# print(pi)

# print(dir(math))  #give all the content of module



'''37 if __name__ == "__main__" '''

''' The if __name__ == "__main__" idiom is a common pattern used in Python scripts
    to determine whether the script is being run directly or being imported as a module into another script.'''

''' In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. 
    When a Python script is run directly, the __name__ variable is set to the string __main__ 
    When the script is imported as a module into another script, the __name__ variable is set to the name of the module.'''

# #Shubh.py
# def welcome():
#     print("Hey you are welcome")

# # print(__name__)

# if __name__ == "__main__":
#     welcome()

# #main.py
# import Shubh
# Shubh.welcome()



'''38 OS Module'''
# import os
# os.mkdir("Data")                                            #creates a directory
# for i in range(0,11):
#     os.mkdir(f"folder {i}")
#     os.rename(f"folder {i}",f"Tut {i}")                     #rename a directory

# for i in range(0,11):
#     os.rmdir(f"Tut {i}")                                    #remove an empty directory
    
# os.remove(f"data.txt")                                        #remove a file

# folder=os.listdir("C:/Users/shubh/Desktop/Python tut")
# for f in folder:
#     print(os.listdir(f))                                           #returns list of directories present in the folder      
#     print(os.listdir(f"C:/Users/shubh/Desktop/Python tut/{f}"))

# print(os.getcwd())                                                 #returns current working directory                       
# os.chdir("C:/Users/shubh/Desktop/Python tut/Tut 1")                #changes the working directory
# print(os.getcwd())

# f=os.open("a.txt",os.O_RDONLY)
# print(type(f),f)            #file descriptor an integer that uniquely identifies an open file
# content=os.read(f,1024)
# print(content)
# os.close(f)

# f=os.open("b.txt",os.O_WRONLY)
# os.write(f,b"Hello world")

# f=os.open("b.txt",os.O_RDONLY)
# content=os.read(f,1024)
# print(content)
# os.close(f)

# print(os.system("echo Hello World"))   #Execute the command in a subshell

# f=os.popen("echo Hello World")         #run a command and get the output as a file-like object
# print(type(f),f)                       #<class 'os._wrap_close'> <os._wrap_close object at 0x000001A02AB3A730>
# print(f.read())
# f.close()



'''39 Local vs Global Variables'''
'''A local variable is a variable that is defined within a function and is only accessible within that function. 
It is created when the function is called and is destroyed when the function returns.'''
'''A global variable is a variable that is defined outside of a function and is accessible from within any function in your code. '''
# x=4                                 #Global variable

# def func1():
#     x=5                             #Local variable
#     y=1                             #Local variable
#     print(f"Local x is: {x}")

# def func2():
#     global x                          #used to declare that a variable is a global variable and should be accessed from the global scope.
#     x=10                              #now this x is global x
#     y=1
#     print(f"Local y is: {y}")

# # print(y)                            #this will give error since y is local variable
# print(f"Global x is: {x}")
# func2()
# print(f"Global x is: {x}")



'''40 File IO in Python'''
# f=open("c.txt",'x')                                      #create mode, This mode creates a file and gives an error if the file already exists.
# f.close()                                                #This releases the resources used by the file and allows other programs to access it

# f=open('a.txt','r')                                       #read mode(default mode),This mode opens the file for reading only and gives an error if the file does not exist
# content=f.read()
# print("Content of file a: ",content)
# f.close()               

# f=open('b.txt','w')           #b is empty                 #write mode, This mode opens the file for writing only and creates a new file if the file does not exist.
# f.write("How are you!")
# f.close()               

# f=open('b.txt','r')
# print("Content of file b: ",f.read())
# f.close()               

# f=open('a.txt','a')                                      #append mode, This mode opens the file for appending only and creates a new file if the file does not exist.
# f.write("\nHello world...")
# f.close()               
# f=open('a.txt','rt')                                     #text mode (same as r),  t mode is used to handle text files
# print("Content of file a after appending: ",f.read())
# f.close()               

# f=open("d.pdf",'x')                                        
# f.close()

# f=open('d.pdf','rb')                                       #binary mode, used to handle binary files (images, pdfs, etc)
# print(f.read())
# f.close()

# with open('a.txt', 'r') as f:                               # the with statement to automatically close the file after you are done with it
#     print(f.read())

#readlines() and writelines() functions
# f=open('a.txt','r')
# i=0
# while True:
#     line=f.readline()                                       # readline() method reads a single line from the file
#     if not line:
#         break
#     i=i+1
#     print(line,i)
# print(f.readlines())                                             # readlines() method reads all the lines of the file and returns them as a list of strings.
# f.close()

# f=open('e.txt','w')
# line=["Hello\n","World\n","!\n"]
# f.writelines(line)                                              #writelines() method in Python writes a sequence of strings to a file
# f.close()

# f=open('e.txt','a')
# line=["Hello\n","World\n","!\n"]
# f.writelines(line)
# f.close()

#seek() and tell() function

# with open('f.txt','r') as f:                                      #the file contains:123456789HelloWorld!
#     print(type(f))                                                #Output:<class '_io.TextIOWrapper'>
#     print(f.read(4))                                              #Output:1234

#     f.seek(5)                                                     #The seek() function allows you to move the current position within a file to a specific point
#     print(f.tell())                                               #The tell() function returns the current position within the file, in bytes
#     print(f.read(4))                                              #Output: 6789

#truncate function
# with open('f.txt','w') as f:
#     f.write("123456789")
#     f.truncate(5)                                                   #truncates the file to the given size

# with open('f.txt','r') as f:
#     print(f.read())                                                 #Output: 12345



'''41 Lambda Functions'''
'''a lambda function is a small anonymous function without a name'''
'''Syntax: lambda arguments: expression'''
# def square1(x):
#     return x**2
# print(square1(3))

# square2=lambda x:x**2                                               #does the same job as square1 function
# print(square2(3))

# def cube(sq, n):                                                    #passing function to a function
#     return sq(n)*n

# print(cube(square1,3))                                              #we can also pass function as an argument
# print(cube(lambda x:x**2,3))


# avg= lambda x,y,z:(x+y+z)/3
# print(avg(1,2,3))                                                     #Lambda functions can have multiple arguments

# table= lambda x,n: print([x*i for i in range(1,n+1) ])                       #Lambda functions can also include multiple statements, but they are limited to a single expression.
# table(3,10)
# # print(table(2,10))

# eo= lambda x: "Even " if(x%2==0) else "Odd"                             ##Lambda functions can also include multiple statements, but they are limited to a single expression.
# print(eo(2))

# sc= lambda x,s: [x**2 for x in range(1,11)] if(s=="Square") else [x**3 for x in range(1,11)] if(s=="Cube") else 0             ##Lambda functions can also include multiple statements, but they are limited to a single expression.
# print(sc(2,"Square"))
# print(sc(2,"Cube"))
# print(sc(2,"Zero"))

# table= [lambda x : x*i for i in range(1,11)]
# for a in table:
#     print(a(2))



'''42 Map, Filter, Reduce and Accumulate'''
'''In Python, the map, filter, accumulate and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. 
    These functions are known as higher-order functions, as they take other functions as arguments.'''

#Map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# Synatx: map(function, iterable)

# def square(x):
#     return x**2
# print(square(2))

# l=[1,2,3,4,5,6,7]
# nl=[]
# for i in l:
#     nl.append(square(i))
# print(nl)

# nl=map(square,l)
# nl=map(lambda x:x**2,l)
# print(list(nl))           


#Filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value), 
# and returns a new sequence containing only the elements that meet the predicate.
# Syntax: filter(predicate, iterable)

# l=[1,2,3,4,5,6,7] 
# def filter_func(n):
#     if n%2==0:
#         return 1
#     else:
#         return 0
# nl=filter(filter_func,l)
# print(list(nl))

# nl=filter(lambda n: 1 if(n%2==0) else 0,l)
# print(list(nl))


#Reduce
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
# Syntax: reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value.
# The iterable argument is a sequence of elements, such as a list or tuple
# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on.

# from functools import reduce
# l=[1,2,3,4,5,6]
# nl=reduce(lambda x,y : x*y,l)
# print(nl)


#Accumulate
# This iterator takes two arguments, iterable target and the function which would be followed at each iteration of value in target. 
# If no function is passed, addition takes place by default. 
# If the input iterable is empty, the output iterable will also be empty.

# from itertools import accumulate
# l=[1,2,3,4,5,6]
# nl=accumulate(l,lambda x,y : x*y)
# print(list(nl))


# Reduce vs Accumulate
# reduce() is defined in “functools” module, accumulate() in “itertools” module.
# reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
# reduce(fun, seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.



'''43 'is' vs '==' '''
''' In python, strings and integers are immutable so is and == will always return the same result.
    For mutable objects such as lists and dictionaries, is and == can behave differently.'''

# a=4            #constant
# b=4            #constant
# #both a and b are created at same memory address since both are constant
# print(a is b)  #compare exact location of object in memory
# print(a == b)  #compare value

# a=[1,2,3]      #mutable
# b=[1,2,3]      #mutable
# #both list are created at diffrent memory address since list is mutable
# print(a is b)  #False
# print(a == b)  #True

# a=(1,2,3)      #immutable
# b=(1,2,3)      #immutable
# #both tuple are created at same memory address since tuple is immutable
# print(a is b)  #True
# print(a == b)  #True



'''Exercise 4'''
'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
The gun beats the snake, the water beats the gun, and the snake beats the water. 
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.'''
#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

# import random
# def possibilities(x,y):
#     p=[
#         [0,1,-1],
#         [-1,0,1],
#         [1,-1,0]
#     ]
#     return p[x][y]

# print("*****Snake, Water and Gun Game*****")

# l=[0,1,2]
# points=0

# while True:
#     n=input("Enter your choice: ")
#     n=n.lower()
#     if n=="snake":
#         x=0
#     elif n=="water":
#         x=1
#     elif n=="gun":
#         x=2
#     else:
#         print("Wrong input!")
#         break

#     y=random.choice(l)
#     w="snake" if y==0 else "water" if y==1 else "gun"

#     print(f"Your choice: {n} and Computer's choice: {w}")

#     c=possibilities(x,y)
#     if c==0:
#         points=points
#         print(f"Current Score: {points}")
#     elif c==1:
#         points=points+100
#         print(f"Current Score: {points}")
#     else:
#         points=points-100
#         print(f"Current Score: {points}")

#     q=int(input("Press 1 to continue 0 to exit: "))
#     if q==0:
#         break

# print(f"Final Score is: {points}")    



'''44 OOPS in Python'''
'''The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.'''
'''A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. '''
'''An object is an instance of a class, and it contains its own data and methods.'''
'''Encapsulation, which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. '''
'''Inheritance, which allows new classes to be created that inherit the properties and methods of an existing class.'''
'''Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class.'''
'''Abstraction in OOPS is used to hide unnecessary information and display only necessary information to the users interacting.'''



'''45 Classes and Objects'''
# class Student:                        #Creating a Class
#     id='1'
#     section="A"
#     stream="Science"

#     def info(self):                   #self parameter refers to current instance of the class and is used to access variables of class.It must be provided as the extra parameter inside the method definition.
#         print(f"Student {self.id} studies in section {self.section} and has {self.stream} stream")

# a=Student()                           #Creating an Object a
# a.info()

# b= Student()                          #Creating an Object b
# b.id="2"
# b.section="B"
# b.stream="Commerce"
# b.info()

# c = Student()                         #Creating an Object c
# c.id="3"
# c.section="C"
# c.stream="Arts"
# c.info()



'''46 Constructors'''
'''A constructor is a special method in a class used to create and initialize an object of a class.
    Constructor is invoked automatically when an object of a class is created. It cannot return any value other than None.
    Whenever a class is instantiated __new__ and __init__ methods are called. 
    __new__ method will be called when an object is created and __init__ method will be called to initialize the object.'''

# class Student:                        #Creating a Class
#     id='1'
#     section="A"
#     stream="Science"

#     def __init__(self):                                 #Default Constructor
#         print("Hello World!")
#         print("Inside Default Constructor")

    # def __init__(self,i,sec,str):
    #     print("Hello World!")
    #     print("Inside Parameterized Constructor")     #Parameterized Constructor
    #     self.id=i
    #     self.section=sec
    #     self.stream=str

    # def info(self):
    #     print(f"Student {self.id} studies in section {self.section} and has {self.stream} stream")

# a=Student('2','B','Commerce')                                      #Parameterized constructor is called
# print(f"Student {a.id} studies in section {a.section} and has {a.stream} stream")
# b=Student('3','C','Arts')
# a.info()
# b.info()

# c=Student()                                                       #Default Constructor is called



'''47 Decorators'''
'''Python decorators extend the functionality of a function or method without modifying its source code.
    It is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.'''

''' *args in function definitions in Python is used to pass a variable number of arguments to a function. 
    It is used to pass a non-keyworded, variable-length argument list.

    **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. '''

# def greet(fx):
#     def mfx(*args):                                              
#         print("Table start...")
#         fx(*args)
#         print("Table complete...")
#     return mfx

# @greet
# def table(n,r):
#     for i in range(1,r+1):
#         print(f"{n} x {i} = {n*i}")

# table(5,10)
# greet(table)(5,10)                                #same as @greet



'''48 Getters(Accessors) and Setters(Mutators)'''
''' A setter updates the value of a variable, while a getter reads the value of a variable.
    Getter and setter methods are used in Python to achieve encapsulation.'''

# using @property decorator to achieve getters and setter behavior
# class Student:
#     def __init__(self,id):
#         self.id=id

#     @property
#     def cid(self):                                                      # a getter function 
#         print("Inside getter!")
#         return self.id

#     @cid.setter                                                         
#     def cid(self,id):                                                   # a setter function 
#         self.id=id
#         print("Inside setter!")

# a=Student(5)
# a.cid=2
# print(a.cid)


# Using property function to achieve getters and setter behavior:
# class Student:
#     def __init__(self,id):
#         self.id=id

#     def get_id(self):
#         print("Inside getter!")
#         return self.id
#     def set_id(self,id):
#         self.id=id
#         print("Inside setter!")

#     getter_setter=property(get_id,set_id)

# x=Student(3)
# x.getter_setter=10
# print(x.getter_setter)



'''49 Inheritance'''
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def showDetails(self):
#         print(f"Name of Student is {self.name} and id is {self.id}")

# a=Student("Ron",1)
# a.showDetails()
# b=Student("Jack",2)
# b.showDetails()

# class Standard(Student):
#     def __init__(self,name,id,std):
#         Student.__init__(self,name,id)
#         self.std=std

#     def showfullDetails(self):
#         print(f"Name of Student is {self.name} and id is {self.id} and standard is {self.std}")


# a=Standard("Max",3,'LKG')
# a.showfullDetails()


'''Types of Inheritance'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''1. Single Inheritance
        Single inheritance enables a derived class to inherit properties from a single parent class'''
#Example 1
# class GrandFather:
#     def __init__(self,gname):
#         self.gname=gname
#     def showGName(self):
#         print(f"Grand Father name is: {self.gname} in class GrandFather")

# class Father(GrandFather):
#     def __init__(self,gname,fname):
#         GrandFather.__init__(self,gname)
#         self.fname=fname
#     def showFName(self):
#         print(f"Grand Father name is: {self.gname} and Father name is: {self.fname} in class Father")

# a=GrandFather("Max")
# a.showGName()
# b=Father("Max","Jack")
# b.showGName()
# b.showFName()


#Example 2
# class GrandFather:
#     def __init__(self,gname):
#         self.gname=gname
#     def showName(self):
#         print(f"Grand Father name is: {self.gname} in class GrandFather")

# class Father(GrandFather):
#     def __init__(self,gname,fname):
#         super().__init__(gname)                                                        #same as GrandFather.__init__(self,gname)
#         self.fname=fname
#     def showName(self):                                                                #this will override the function named showName() of GrandFather class 
#         print(f"Grand Father name is: {self.gname} and Father name is: {self.fname} in class Father")

# a=GrandFather("Max")
# a.showName()
# b=Father("Max","Jack")
# b.showName()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2. Multilevel Inheritance
        In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. '''
#Example 1
# class GrandFather:
#     def __init__(self,gname):
#         self.gname=gname
#     def showGName(self):
#         print(f"Grand Father name is: {self.gname} in class GrandFather")

# class Father(GrandFather):
#     def __init__(self,gname,fname):
#         GrandFather.__init__(self,gname)
#         self.fname=fname
#     def showFName(self):
#         print(f"Grand Father name is: {self.gname} and Father name is: {self.fname} in class Father ")

# class Son(Father):
#     def __init__(self,gname,fname,sname):
#         # GrandFather.__init__(self,gname)
#         Father.__init__(self,gname,fname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Grand Father name is: {self.gname} and Father name is: {self.fname} and Son name is: {self.sname} in class Son")

# a=GrandFather("Max")
# a.showGName()
# b=Father("Max","Jack")
# b.showGName()
# b.showFName()
# c=Son("Max","Jack","Ron")
# c.showGName()
# c.showFName()
# c.showSName()

# print(Son.mro())                              #MRO: [<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class 'object'>]

# Example 2
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# a=GoldenRetriever("Tom","Grey")
# a.show_details()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''3. Multiple Inheritance
        When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.'''
#Example 1
# class Father():
#     def __init__(self,fname):
#         self.fname=fname
#     def showFName(self):
#         print(f"Father name is: {self.fname} in class Father ")

# class Mother():
#     def __init__(self,mname):
#         self.mname=mname
#     def showMName(self):
#         print(f"Mother name is: {self.mname} in class Mother ")

# class Son(Father,Mother):
#     def __init__(self,fname,mname,sname):
#         Father.__init__(self,fname)
#         Mother.__init__(self,mname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Father name is: {self.fname} and Mother name is: {self.mname} and Son name is: {self.sname} in class Son")

# a=Son("Jack","Ruby","Ron")
# a.showFName()
# a.showMName()
# a.showSName()

#Example 2
# class Father():
#     def __init__(self,fname):
#         self.fname=fname
#     def showName(self):
#         print(f"Father name is: {self.fname} in class Father ")

# class Mother():
#     def __init__(self,mname):
#         self.mname=mname
#     def showName(self):
#         print(f"Mother name is: {self.mname} in class Mother ")

# class Son(Father,Mother):                                            #MRO for this will be [<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]
#     def __init__(self,fname,mname,sname):
#         Father.__init__(self,fname)
#         Mother.__init__(self,mname)
#         self.sname=sname
    
# class Son(Mother,Father):                                            #MRO for this will be [<class '__main__.Son'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]
#     def __init__(self,fname,mname,sname):
#         Father.__init__(self,fname)
#         Mother.__init__(self,mname)
#         self.sname=sname

# a=Son("Jack","Ruby","Ron")
# a.showName()

''' Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes.
    The MRO determines the order in which parent classes are searched for attributes and methods.'''
# print(Son.mro())



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''4. Hierarchical Inheritance
        When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.'''

# class Father():
#     def __init__(self,fname):
#         self.fname=fname
#     def showFName(self):
#         print(f"Father name is: {self.fname} in class Father ")

# class Son1(Father):                                                             #MRO :[<class '__main__.Son1'>, <class '__main__.Father'>, <class 'object'>]
#     def __init__(self,fname,sname):
#         Father.__init__(self,fname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Father name is: {self.fname} and Son name is: {self.sname} in class Son1")

# class Son2(Father):                                                             #MRO :[<class '__main__.Son2'>, <class '__main__.Father'>, <class 'object'>]
#     def __init__(self,fname,sname):
#         Father.__init__(self,fname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Father name is: {self.fname} and Son name is: {self.sname} in class Son2")

# a=Son1("Jack","Ron")
# b=Son2("Jack","Ryan")

# a.showSName()
# b.showSName()

# print(Son1.mro())
# print(Son2.mro())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''5. Hybrid Inheritance
        Inheritance consisting of multiple types of inheritance is called hybrid inheritance.'''

# class GrandFather:
#     def __init__(self,gname):
#         self.gname=gname
#     def showGName(self):
#         print(f"Grand Father name is: {self.gname} in class GrandFather")

# class Father(GrandFather):
#     def __init__(self,gname,fname):
#         GrandFather.__init__(self,gname)
#         self.fname=fname
#     def showFName(self):
#         print(f"Grand Father name is: {self.gname} and Father name is: {self.fname} in class Father ")

# class Mother():
#     def __init__(self,mname):
#         self.mname=mname
#     def showMName(self):
#         print(f"Mother name is: {self.mname} in class Mother ")

# class Son1(Father,Mother):                                           #MRO:[<class '__main__.Son1'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class '__main__.Mother'>, <class 'object'>]
#     def __init__(self,gname,fname,mname,sname):
#         Father.__init__(self,gname,fname)
#         Mother.__init__(self,mname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Grand Father name is: {self.gname} Father name is: {self.fname} and Mother name is: {self.mname} and Son name is: {self.sname} in class Son1")

# class Son2(Father,Mother):                                          #MRO:[<class '__main__.Son2'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class '__main__.Mother'>, <class 'object'>]
#     def __init__(self,gname,fname,mname,sname):
#         Father.__init__(self,gname,fname)
#         Mother.__init__(self,mname)
#         self.sname=sname
#     def showSName(self):
#         print(f"Grand Father name is: {self.gname} Father name is: {self.fname} and Mother name is: {self.mname} and Son name is: {self.sname} in class Son2")


# a=Son1("Max","Jack","Ruby","Ron")
# b=Son2("Max","Jack","Ruby","Ryan")
# a.showSName()
# b.showSName()
# print(Son1.mro())
# print(Son2.mro())


'''50 Access Specifiers'''
'''Access specifiers or access modifiers in python programming are used to limit the access of class variables 
    and class methods outside of class while implementing the concepts of inheritance.'''

'''Types of Access Specifiers'''

'''1. Public Access Specifiers
        All the variables and methods (member functions) in python are by default public. 
        Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.'''
# class Student:
#     def __init__(self):
#         self.name="Ron"                             #name is public variable
#     def showName(self):                             #showName is public method
#         print(f"Name is {self.name}")

# a=Student()
# print(a.name)
# a.showName()
# print(a.__dir__())                                  #__dir__ returns the valid list of the attributes for the objects in the current local scope

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2. Private Access Specifiers
        Private members of a class (variables or methods) are those members which are only accessible inside the class. 
        We cannot use private members outside of class.
        In Python, there is no strict concept of "private" access modifiers
        However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__).
        This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. '''

# class Student:
#     def __init__(self):
#         self.__name="Ron"                             #__name is private variable
#     def __showName(self):                             #__showName is private method
#         print(f"Name is {self.__name}")

# a=Student()
# print(a.__name)                                       #__name can't be accessed directely
# a.__showName()                                        #__showName can't be accessed directely

'''Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
    Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.'''

# print(a._Student__name)                                 #__name can be accessed using Name mangling
# a._Student__showName()                                  #__showName can be accessed using Name mangling
# print(a.__dir__())                                      #__dir__ returns the valid list of the attributes for the objects in the current local scope



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''3. Protected Access Specifiers
        In object-oriented programming (OOP), the term "protected" is used to describe a member 
        (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.
        In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_).
        It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member.'''

# class Student:
#     def __init__(self,name):
#         self._name=name                             #_name is protected variable
#     def _showName(self):                             #_showName is protected method
#         print(f"Name is {self._name}")

# class Id(Student):
#     def __init__(self,name,id):
#         Student.__init__(self,name)
#         self._id=id
#     def showNameAndId(self):
        
#         print(f"Name is {self._name} and id is {self._id}")


# a=Student("Ron")
# print(a._name)                                       #_name can be accessed directely in this class and its subclass
# a._showName()                                        #_showName can be accessed directely in this class and its subclass   
# b=Id("Ron",1)
# print(b._id)
# b.showNameAndId()
# print(a.__dir__())                                    #__dir__ returns the valid list of the attributes for the objects in the current local scope
# print(dir(b))                                         #same as __dir__                  



'''Exercise 5'''
''' Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class 
    and show how you can print all books, add a book and get the number of books using different methods. 
    Show that your program doesnt persist the books after the program is stopped! '''
# class library:
#     def __init__(self):
#         self.num_book=0
#         self.name_book=[]
#     def addBooks(self,name):
#         self.name_book.append(name)
#         self.num_book=len(self.name_book)
#         print("Book added!")
#     def showBook(self):
#         print(f"Books present in library are: {self.name_book}")
#         print(f"Total number of books present in library are: {self.num_book}")
        
#     def remBook(self,name):
#         self.name_book.remove(name)
#         self.num_book=len(self.name_book)
#         print("Book removed!")

# a=library()
# a.addBooks("Sherlock Holmes")
# a.addBooks("Harry Potter")
# a.addBooks("Jungle book")
# a.addBooks("Lord of Rings")
# a.showBook()
# a.remBook("Lord of Rings")
# a.showBook()

# b=library()
# b.showBook()



'''51 Static Methods'''
''' Static methods in Python are methods that belong to a class rather than an instance of the class. 
    Static methods are often used to create utility functions that don't need access to instance data.
    They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self).'''

# class Calculator:
#     def __init__(self,num):
#         self.num=num
        
#     def addNum(self,n):
#         self.num=self.num+n
#         return self.num
#     @staticmethod
#     def add(a,b):                    #no need to give self. So it is not always mandatory to write self when defining a method in a class as we can make static methods.
#         return a+b

# x=Calculator(5)
# print(x.num)

# print("Inside instatnce method:",x.addNum(10))

# print("Inside static method:", x.add(2,3))
# print("Inside static method:", Calculator.add(2,3))



'''52 Instance vs Class Variables'''
''' Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method.
    Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method. 
    Class variables can be accessed via classname.varibale_name or self.class.variable_name.
    Instance variables can be accessed using self.variable_name.'''
# class Student:
    # schoolName="MIT"                                              #class variable
    # def __init__(self,name):
    #     self.name=name
    #     self.year= 2002
    # def showDetails(self):
    #     print(f"Name of student is: {self.name} and year of joining is: {self.year} and school name is {self.schoolName}")

# a=Student("Ron")
# # Student.showDetails(a)
# b=Student("Ryan")
# # Student.showDetails(b)
# a.year=2003
# print(Student.schoolName)
# Student.schoolName="Yale"                                                               #Modifies for the all instance
# print(Student.schoolName)
# a.schoolName="Stanford"                                                                 #Modifies for the particular instance
# a.showDetails()
# b.schoolName="Oxford"                                                                 #Modifies for the particular instance
# b.showDetails()



'''Exercise 5'''
'''Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:
sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png'''
# import os

# files = os.listdir("clutteredFolder")
# i = 1
# for file in files:
#     if file.endswith(".png"):
#         print(file)
#         os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
#         i = i + 1



'''53 Class Methods'''
''' A class method is a type of method that is bound to the class and not the instance of the class.
    Class methods are defined using the "@classmethod" decorator, followed by a function definition.
    The first argument of the function is always "cls," which represents the class itself.'''

# class Student:
#     school="MIT"
#     def showinfo(self):
#         print(f"Name of School is: {self.school}")
    
#     @classmethod                                                                          #using @classmethod decorator the first argument passed will be the class itself
#     def changeSchool(cls,newName):                                                        #by defualt this cls is thought as self only i.e instance is only passed
#         cls.school=newName

# a=Student()
# a.showinfo()
# print(Student.school)
# a.changeSchool("Stanford")
# a.showinfo()
# print(Student.school)

'''Class Methods as Alternative Constructors in Python'''
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     @classmethod
#     def fromStr(cls,s):
#         return cls(s.split("-")[0],int(s.split("-")[1]))                  #same as Student(s.split("-")[0],int(s.split("-")[1]))

#     def showInfo(self):
#         print(f"Student name is {self.name} and id is {self.id}")

# a=Student("Ron",1)
# print(a.name,a.id)

# s="Ryan-2"
# b=Student(s.split("-")[0],s.split("-")[1])
# print(b.name,b.id)

# c=Student.fromStr("Mark-3")                        #using class method as alt constructor
# c.showInfo()



'''54 dir(), __dict__ and help() methods'''
'''In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help()'''

''' dir() method: The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. 
    It is a useful tool for discovering what you can do with an object.'''

# x=[1,2,3]
# print(dir(x))
#Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


'''__dict__ attribute: It returns a dictionary representation of an object's attributes.'''
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

# a=Student("Ron",30)
# print(a.__dict__)               #Output: {'name': 'Ron', 'id': 30}


'''help() method: It is used to get help documentation for an object, including a description of its attributes and methods.'''
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# print(help(Student))



'''55 Super Keyword'''
''' It  is used to refer to the parent class. 
    It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.'''
# class Parent:
#     def func1(self):
#         print("Inside parent method..")

# class Child(Parent):
#     def func1(self):
#         print("Inside child method1..")
#         super().func1()
    
#     def func2(self):
#         print("Inside child method2..")
#         super().func1()

# a=Child()
# a.func1()
# a.func2()


# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

# class Programmer(Student):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)
#         self.lang=lang
#     def showInfo(self):
#         print(f"Name is {self.name} id is {self.id} and language is {self.lang}")

# a=Programmer("Ron",1,"Python")
# a.showInfo()

# class ParentClass1:
#     def parent_method(self):
#         print("This is the parent method of ParentClass1.")
# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent method of ParentClass2.")
# class ChildClass(ParentClass1, ParentClass2):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()
# child_object = ChildClass()
# child_object.child_method()



'''56 Magic/Dunder Methods'''
''' These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.
    Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.'''

'''__init__(): The init method is a special method that is automatically invoked when you create a new instance of a class. 
    his method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need.

    __str__() and __repr__(): The str and repr methods are both used to convert an object to a string representation. 
    The str method is used when you want to print out an object, while the repr method is used when you want to get a 
    string representation of an object that can be used to recreate the object.

    __len()__: The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

    __call__(): The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called.'''

# class Student:
#     def __init__(self,name):                                      
#         self.name=name

#     def __len__(self):
#         i=0
#         for c in self.name:
#             i+=1
#         return i
    
#     def __str__(self):
#         return (f"Name of student is {self.name} inside __str__")
    
#     def __repr__(self):
#         return (f"Name of student is {self.name} inside __repr__")

#     def __call__(self):
#         print(f"Code working..")

# a=Student("Ryan")                                   #__init__ is called
# print(a)                                            #__str__ is called if not present then __repr__called
# print(str(a))                                       #__str__ is called
# print(repr(a))                                      #__repr__ is called
# print(a.name)
# print(len(a))                                       #__len__ is automatically called
# a()                                                 #__call__ is called



'''57 Method Overriding'''
'''Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. 
The method in the derived class is said to override the method in the base class.'''
# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def area(self):
#         return self.x*self.y

# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#         super().__init__(r,r)

#     def area(self):
#         # return 3.14*self.r*self.r
#         return 3.14*super().area()

# a=Shape(2,3)
# print(a.area())

# b=Circle(3)
# print(b.area())



'''Exercise 6'''
''' Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. 
    You are welcome to add more functionalities. pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming
    the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.'''

# from pypdf import PdfReader
# from pypdf import PdfWriter
# reader = PdfReader("pdf1.pdf")
# page = reader.pages[0]
# print(page.extract_text())


# merger = PdfWriter()
# for pdf in ["pdf1.pdf", "pdf2.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()



'''58 Operator Overloading'''
'''Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. '''
# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return (f"{self.i}i + {self.j}j + {self.k}k")

#     def __add__(self, x):
#         return vector(self.i + x.i,  self.j+x.j, self.k+x.k)

# a=vector(2,3,5)
# print(a)

# b=vector(5,4,7)
# print(b)

# print(a+b)



'''Exercise 7'''
'''Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
l = ["Rahul", "Nishant", "Harry"]
Your program should pronouce:

Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry'''

# Method 1
# import pyttsx3
# engine=pyttsx3.init()

# l = ["Rahul", "Nishant", "Harry"]
# for i in l:
#     engine.say(f"Shoutout to {i}")
#     engine.runAndWait()

# Method2
# import win32com.client 
# speaker = win32com.client.Dispatch("SAPI.SpVoice") 
# l = ["Rahul", "Nishant", "Harry"]
# for i in l:
#     speaker.Speak(f"Shoutout to {i}") 



'''59 Time Module'''
''' time(): The time.time() function returns the current time as a floating-point number, 
    representing the number of seconds since the epoch (the point in time when the time module was initialized). 

    sleep(): The time.sleep() function suspends the execution of the current thread for a specified number of seconds.

    strftime(): The time.strftime() function formats a time value as a string, based on a specified format.
'''
# import time
# def usingWhile():
#     i=0
#     while(i<50000):
#         print(i)
#         i+=1
# def usingFor():
#     for i in range(50000):
#         print(i)

# init=time.time()
# usingWhile()
# print(time.time()-init)
# time.sleep(10)                                           #the program stops for 10 seconds
# init=time.time()
# usingFor()
# print(time.time()-init)

# t= time.localtime()
# formatted_time= time.strftime("%H:%M:%S %Y,%m,%d",t)       #output: 22:41:49 2024,05,27
# print(formatted_time)



'''60 Command Line Utility'''
'''Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows.'''
# import argparse
# import sys

# def calc(args):
#     if args.o== 'add':
#         return args.x + args.y
    
#     elif args.o== 'sub':
#         return args.x - args.y
    
#     elif args.o== 'mul':
#         return args.x * args.y

#     elif args.o== 'div':
#         return args.x / args.y

#     else:
#         return "Something went wrong!"

# if __name__=="__main__":
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,help='Enter first number.This is a utility for calculation')
#     parser.add_argument('--y',type=float,default=3.0,help='Enter second number.This is a utility for calculation')
#     parser.add_argument('--o',type=str,default="add",help='This is a utility for calculation')

#     args=parser.parse_args()
#     sys.stdout.write(str(calc(args)))



'''61 Walrus Operator'''
'''This operator allows you to assign a value to a variable within an expression.'''
# a=True
# print(a := False)

# l=[1,2,3,4,5,6,7,8]
# while((n := (len(l))) > 0):
#     print(n)
#     l.pop()

# l=[]
# while True:
#     n=int(input("Enter a number: "))
#     if n==0:
#         break
#     else:
#         l.append(n)

# using walrus operator
# while((n := int(input("Enter a number: "))) != 0):
#     l.append(n)

# print(l)



'''62 Shutil Module'''
''' Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility.
    
    shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists,
    the original file will be overwritten.

    shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

    shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. 
    If the destination location already exists, the original directory will be merged with it.

    shutil.move(src, dst): This function moves the file located at src to a new location specified by dst.
    This function is equivalent to renaming a file in most cases.

    shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. 
    This function is similar to using the rm -rf command in a shell.
'''
# import shutil
# import os
# shutil.copy("Python Tutorial.py","Python Tutorial2.py")
# shutil.copy2("Python Tutorial.py","Python Tutorial2.py")
# shutil.copytree("folder1","folder2")
# shutil.move("folder1/file1.txt","file1.txt")
# shutil.rmtree("folder1")
# os.remove("file1.txt")



'''63 Requests Module'''
'''The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. '''
# import requests 
# from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h1"):
#     print(heading.text)



'''Exercise 8'''
''' Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
    Go to: https://newsapi.org/ and explore the various options to build you application'''
# Method 1
# from newsapi import NewsApiClient
# from bs4 import BeautifulSoup

# newsapi = NewsApiClient(api_key='14e87ccdfdf64576b88f0f24b7b1f0a4')
# print("Welcome to NEWS App ")
# n=int(input("Enter 1 for sports news, 2 for business news, 3 Fashion news: "))

# if n==1:
#     top_headlines = newsapi.get_top_headlines(q='Sports',
#                                         sources='bbc-news,the-verge',
#                                         language='en')

# elif n==2:
#     top_headlines = newsapi.get_top_headlines(q='Business',
#                                         language='en')

# elif n==3:
#     top_headlines = newsapi.get_top_headlines(q='Fashion',
#                                         language='en')


# for article in top_headlines['articles']:
#     print(article['title'])
#     print("---------------------")

# Method 2
# import requests
# import json

# query=input("Enter what news you want to see: ")
# r=requests.get(f"https://newsapi.org/v2/everything?q={query}&from=2024-04-28&sortBy=publishedAt&apiKey=14e87ccdfdf64576b88f0f24b7b1f0a4")
# r=json.loads(r.text)
# i=1
# for article in r['articles']:
#     print(f"News {i}: {article['title']}")
#     print(f"News {i}: {article['description']}")
#     print("---------------------")
#     if(i==5):
#         break
#     i+=1



'''64 Generators'''
''' A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it.
    The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. 
    The next() function is used to request the next value from the generator, 
    and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.'''

# def my_generator():
#     for i in range(5):
#         yield i                         

#  the generator function my_generator() returns a generator object, which can be used to generate the values in the range 0 to 4.
# gen= my_generator()
# print(next(gen))                #Output:0
# print(next(gen))                #Output:1
# print(next(gen))                #Output:2

''' One of the main benefits of generators is that they allow you to generate the values on-the-fly,
    rather than having to create and store the entire sequence in memory.
    Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested.
'''



'''65 Function Caching'''
''' Function caching is a technique for improving the performance of a program by storing the results of
    a function call so that you can reuse the results instead of recomputing them every time the function is called.
    This can be particularly useful when a function is computationally expensive, 
    or when the inputs to the function are unlikely to change frequently.'''

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)     #maxsize is set to None, the cache will have an unlimited size.
# def fx(n):
#     time.sleep(5)
#     return n*10

# print(fx(20))
# print("Done for 20")
# print(fx(5))
# print("Done for 5")
# print(fx(2))
# print("Done for 2")
# # Now the below computation will be fetched from cache
# print(fx(20))
# print("Done for 20")
# print(fx(5))
# print("Done for 5")
# print(fx(2))
# print("Done for 2")
# # Now again computation is done 
# print(fx(11))
# print("Done for 2")



'''Exercise 9'''
''' Write a python program which reminds you of drinking water every hour or two. 
    Your program can either beep or send desktop notifications for a specific operating system'''
# Method 1
# import time
# from win10toast import ToastNotifier 

# n = ToastNotifier() 
# while True:
#     n.show_toast("Drink water", "You got notification", duration = 10) 
#     time.sleep(3600)


# Method 2
# from plyer import notification
# import time
# while true:
#     notification.notify(title = "Drink Water",message = "Drink Water",timeout = 10)
#     time.sleep(3600)



'''66 Regular Expressions'''
'''Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. '''
'''[]  Represent a character class
    ^   Matches the beginning
    $   Matches the end
    .   Matches any character except newline
    ?   Matches zero or one occurrence.
    |   Means OR (Matches with any of the characters
        separated by it.
    *   Any number of occurrences (including 0 occurrences)
    +   One or more occurrences
    {}  Indicate number of occurrences of a preceding RE 
        to match.
    ()  Enclose a group of REs'''


# import re

# pattern=r"[A-Z]+yclone"
# text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. 
#         Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. Dyclone
#         It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status.
#         Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph),
#         1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). 
#         As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March
# '''

# # match=re.search(pattern,text)
# # print(match)

# match=re.finditer(pattern,text)
# for m in match:
#     print(m)
#     print(m.span())
#     print(type(m.span()))
#     print(text[m.span()[0] : m.span()[1]])



'''67 Async IO'''
'''Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.'''
# import time
# import asyncio

# async def func1():
#     await asyncio.sleep(10)
#     print("func1")
#     return 1

# async def func2():
#     await asyncio.sleep(10)
#     print("func2")
#     return 2

# async def func3():
#     await asyncio.sleep(10)
#     print("func3")
#     return 3

# async def main():
#     # func will run one by one
#     # await func1()
#     # await func2()
#     # await func3()

#     # func will run together
#     L = await asyncio.gather(
#             func1(),
#             func2(),
#             func3()
#     )
#     print(L)

# asyncio.run(main())



'''68 Multithreading'''
'''Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.'''
'''To create a thread, we need to create a Thread object and then call its start() method. 
    The start() method runs the thread and then to stop the execution, we use the join() method. '''
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor


# def func(sec):
#     print(f"Sleeping for {sec} seconds.")
#     time.sleep(sec)
#     return(sec)


# time1=time.perf_counter()

# Normal Code
# func(5)
# func(2)
# func(4)

# time2=time.perf_counter()
# print(time2-time1)

# Code using threads
# t1=threading.Thread(target=func,args=[5])
# t2=threading.Thread(target=func,args=[2])
# t3=threading.Thread(target=func,args=[4])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# time3=time.perf_counter()
# print(time3-time2)

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#     #     future1 = executor.submit(func, 3)
#     #     future2 = executor.submit(func, 2)
#     #     future3 = executor.submit(func, 4)
#     #     print(future1.result())
#     #     print(future2.result())
#     #     print(future3.result())
        
#         l = [3, 5, 1, 2]
#         results = executor.map(func, l)
#         for result in results:
#             print(result)

# poolingDemo()



'''69 Multiprocessing'''
'''Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel.'''
# import multiprocessing
# import requests
# import concurrent.futures

# def download_file(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")

# if __name__ =="__main__":
#     url = "https://picsum.photos/2000/3000"
    # pros=[]
    # for i in range(5):
    #     # download_file(url,i)
    #     p=multiprocessing.Process(target=download_file,args=[url,i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     l1 = [url for i in range(10)]
    #     l2 = [i for i in range(10)]
    #     results = executor.map(download_file, l1, l2)
    #     for r in results:
    #         print(r)



'''70 Destructor'''
''' Destructor is called for destroying the object.
    Destructor gets called in the following two cases
    1. When an object goes out of scope or
    2. The reference counter of the object reaches 0.
    
    The __del__ method is called for any object when the reference count for that object becomes zero.
    The __del()__() doesn’t work correctly in the case of circular referencing. In circular referencing occurs when two objects refer to each other, 
    and when Exception occured in __init__() method'''

# class Student:
#     def __init__(self,name):
#         self.name=name
#         print("Inside Constructor!")
    
#     def show_name(self):
#         print(f"Name of Student is {self.name}")

#     def __del__(self):
#         print("Inside Destructor!")

# s=Student("Ron")
# s.show_name()
# del s
# s.show_name()                #this will throw NameError: name 's' is not defined since object is deleted



'''71 SQL Connection'''
# import sqlite3

# #connect to a new database
# conn=sqlite3.connect("alpha.db")

# #create a cursor
# cur=conn.cursor()

# #create a table 
# cur.execute('''CREATE TABLE employee(
# 	e_id int NOT NULL,
# 	e_name varchar(20),
# 	e_salary int,
# 	e_age int,
# 	e_gender varchar(20),
# 	e_dept varchar(20),
# 	PRIMARY KEY(e_id)
# 	);''')


# cur.execute('''INSERT INTO employee
#     VALUES(1,'SAM',40000,22,'MALE','GROUP FUNCTIONS');''')
# cur.execute('''INSERT INTO employee
#         VALUES(2,'ALEXA',40000,22,'FEMALE','GROUP FUNCTIONS');
#         ''')
# output=cur.execute('''SELECT * FROM employee''')
# for row in output:
#     print(row)
# conn.commit()
# cur.close()
# conn.close()



'''72 MYSQL connection'''
# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="user_name",passwd="password")

# cur=mydb.cursor()

# cur.execute('''Show databases''')
# for i in cur :
#     print(i)

# result=cur.fetchone()          #returns one data
# result=cur.fetchall()          #returns all data



'''SQLAlchemy'''    #To be verified
# import sqlalchemy as sa

# engine=sa.create_engine("sqlite:///:memory:")
# conn=engine.connect()

# metadata=sa.MetaData()
# user_table= sa.Table(
#     "user",
#     metadata,
#     sa.Column("id",sa.Integer, primary_key=True),
#     sa.Column("username",sa.String),
#     sa.Column("email",sa.String)
# )

# def insert_user(username: str,email: str)-> None:
#     query=user_table.insert().values(username=usernmae,email=email)
#     conn.execute(query)

# def select_user(username: str)-> sa.engine.Result:
#     query=user_table.select().where(user_table.c.username==username)
#     result= conn.execute(query)
#     return result.fetchone()

# if __name__=='main':
#     metadata.create_all(engine)
#     insert_user("Shubh","shubhpathak@gmail.com")
#     print("S")
#     print(select_user("Shubh"))
#     conn.close()



'''71 Logging'''
'''Constant	    Numeric Value	 String Value
logging.DEBUG	    10	            DEBUG
logging.INFO	    20	            INFO
logging.WARNING	    30	            WARNING
logging.ERROR	    40	            ERROR
logging.CRITICAL	50	            CRITICAL'''

# import logging

# logging.debug("This is a debug message")           #This doesn't give any error because by default, the logging module logs the messages with a severity level of WARNING or above. 
# logging.info("This is an info message")            #This doesn't give any error because by default, the logging module logs the messages with a severity level of WARNING or above. 
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


# To log debug and info level
# logging.basicConfig(level=logging.DEBUG)            #we can also use logging level numeric value or string value in level parameter
# logging.debug("This will get logged.")


# We can edit logging format
# logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
# logging.warning("Hello, Warning!")

# logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
# logging.warning("Hello, Warning!")


# to show time in logs
# logging.basicConfig(format="{asctime} - {levelname} - {message}",
#                     style="{",
#                     datefmt="%Y-%m-%d %H:%M",
#                     )
# logging.warning("Hello, World")


# to save logs in file
# logging.basicConfig(
#                     filename="app.log",
#                     encoding="utf-8",
#                     filemode="a",
#                     format="{asctime} - {levelname} - {message}",
#                     style="{",
#                     datefmt="%Y-%m-%d %H:%M",
#                     )
# logging.warning("Hello, World")

# to display variable values in logs
# logging.basicConfig(
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
#     level=logging.DEBUG)
# name = "Samara"
# logging.debug(f"{name}")

