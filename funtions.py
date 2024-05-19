
 #Task 1. Write a Python function called greet that takes a name parameter with
#a default value of "Student". The function should print a greeting message
 #including the provided name. Test the function with both default and custom
 #name values.
# Code:
 def function5(name= ' niazi'):
 print('hello,', name)
 function5()
 function5('kalia')
 #Output:
 #Task 2. Create a Python function called generate_numbers() that generates
 #and prints numbers within a specified range. The function should take two
 #parameters, start and end, with default values of 1 and 10 respectively. Test
 #the function with different ranges.
 #Code:
 def numberFunction(num1, num2):
 for i in range(num1, num2+1):
 print(i)
 numberFunction(3, 9)
#Output:
 #Task 3. Write a function Count( ) which takes a list as argument and returns
 #how many elements are in the list (without using built-in function len). def
# Count (list1): #your code logic here … print(“number of elements are”,
 #Count([4,7,8,10,3]))
 #Code:
 def listFunction(mylist):
 count = 0
 for i in mylist:
 count = count + 1
 print(count)
 list = [2, 3, 4, 1, 4, 5, 9, 3, 8]
 listFunction(list)
 #Output:
#Task 4.
 #Write a function Count_Z( ) which takes a list as argument and returns how
 #many elements are zero in the
 #list (without using built-in function count).
 #def Count_Z (list2):
 #your code logic here …
 #print(“number of zero elements are” , Count_Z ( [ 4 , 0 , 0 , 7 , 8 , 18 , 0 , 32] ))
 #Code:
 def zeroCount(List):
 zerocount = 0
 for i in List:
 if i == 0:
 zerocount += 1
 return zerocount
 mylist = [1, 0, 0, 7, 8, 1, 0, 2, 3, 0]
 endresult = zeroCount(mylist)
 print("There are", endresult, "zero/s in this list." )
 #Output:
 #Task 5.
 #Write a function Search( ) which takes a list as argument and a number to be
 #searched in list and another
 #number to be replaced in place of searched item and returns the updated list.
 #def Search (list3, search, replace):
 #your code logic here …
# print(“New list after changes is” , Search( [ 4 , 10 , 17 , 45 , 8 , 11 , 0 , 32 , 17 ],
 #17 , 30 ))
#Code:
 def Searchreplacefunction(List, Search, Replace,):
 updatedlist = []
 for i in List:
 if i == Search:
 updatedlist.append(Replace)
 else:
 updatedlist.append(i)
 print("the Search value was replaced with value: ")
 return updatedlist
 MyList = [4 , 10 , 17 , 45 , 8 , 11 , 0 , 32 , 17]
 Search = 10
 Replace = 199
 print(MyList)
 NewList = Searchreplacefunction(MyList, Search, Replace)
 print('new list after the update is ', NewList)
 #Output:------------------------------------------------END------------------------------------------------
