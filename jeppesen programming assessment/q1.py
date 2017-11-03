# QUESTION 1

# Write a function that takes a list of numbers as input
# and prints true if any number is repeated, otherwise false.

def duplicates(n):
    if len(set(n)) == len(n):  # compares length of original list to set() list, if the same then no duplicates
        print False
    elif len(set(n)) != len(n):  # if different, duplicates exist
        print True


# list1 = (1,2,3,4,5,6,7,8,9,10,11,10)    #list of numbers w duplicate
# list2 = (0,1,2,3,4,5,6,7,8,9,19)        #list of number w/o duplicate
        
# duplicates(list1)  #run