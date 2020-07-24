# session 2

## Functions

### Something
This is a class object which has the objects(something_new) initiated in the __init__().  
#### __init__
something_new is assigned with None

### SomethingNew
This is a class object which has the objects(i and something) initiated in the __init__().  
#### __init__
i and something  are initiated b
### add_something
This is a function that initiates the cyclical referencing of Something and Something_New which keeps of adding to its collection list.

### reserved_Function
Will be used in future if required

### clear_memory
Collection.clear will clear the lists but not the references of the classes that are initiated in the list. Hence we are using gc.collect to to clear the references also so that our memory will be free
### critical_function
This is the function that creates the cyclical references using the function add_something and classes(something and something_new).

### compare_strings_old, compare_strings_new, sleep, char_list
compare_strings_old and compare_strings_new are two functions in which compare_strings_old is roughly written which is not the optimal way of coding. And as part of assignment we are supposed to write the new fiunction with the name of compare_strings_new in a optimal way. Sleep is used in the new function as a place holder for time being
compare_strings_old : 
Two strings are compared as many times as the input to the function. And checks whether d is in the list of the characters of the string a.
Its efficient to refer to memory location of long string using sys.intern() for comparison. 

So when we run the old code, we are able to finish the execution in 6.2658839999999145 seconds. And now our new function is able to complete the execution in 0.6056751000000986 seconds which 10 times faster that the previous function
##### sleep
As suggested we removed sleep from the assignment. Objective of this function is to stop executing for a specified amount of time.

#####  char_list
Initially  this was a list which was later changed to set. Reason being list had multiple 'd's whereas our objective is to check whether d is present in a string. List will have repetitive elements whereas set will have unique values of a list. Hence set is used inplace of list to optimise code.

### collection
collection is a list of 131072 objects created using a for loop. Each object is class of Something and Something_new which is cyclically referenced to each other.

Objective of creating Something, Something_New, add_something, critical_function is to ensure that we are able to clean the memory when object is no longer in use. THis will help us save memory and write the code efficiently.

Initially when the code is shared garbage collector is not used. Due to which even when the collection.clear() clears the lists, still there are cyclical references that are there in the memory which neither removed nor used. With the help of the garbage collector we were able to free up that space.

Without the garbage collector memory usage for critical_function is  51 MB. After running garbage collector the same is around 2MB



# Results of test_session2.py
!pytest test_session2.py
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\Users\jayasans4085\OneDrive - ARCADIS\Desktop\EPAi\session2-jai2shan-master
plugins: arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collected 10 items

test_session2.py ..........                                              [100%]

============================= 10 passed in 9.04s ==============================