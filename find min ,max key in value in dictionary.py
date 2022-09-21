# write a python program to get the key of lowest value from the dictionary.

from multiprocessing.sharedctypes import Value
from optparse import Values


item={"price":5000,"year":2022,"rate":2000}

#print(min(item))
#print(max(item))
a=min(item.keys(),key=(lambda k:item[k]))
print("maximum value =" ,item[a])
b=max(item.keys(),key=(lambda h:item[h]))
print(item[b])