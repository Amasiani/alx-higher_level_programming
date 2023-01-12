#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    items_list = dict() #create an empty dictionary
    for i in range(len(my_list)):
        if (my_list[i] not in items_list.keys()): #if  not in the item list
            items_list[my_list[i]] = my_list[i] #it will be added
            a += my_list[i]
    return(a)
