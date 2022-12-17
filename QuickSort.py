import time
import random

def QuickSort(list):
    l = len(list)#get length
    if l >= 2:#if length is greater than 2(so we can split it)
        mid = list[l//2]#find a middle number
        llist = []#define two lists
        rlist = []
        list.remove(mid)#remove the middle number
        for num in list:#go through every number in the list
            if num < mid:#sort them into the leftList and the rightList
                llist.append(num)
            else:
                rlist.append(num)
        return QuickSort(llist) + [mid] +QuickSort(rlist)#return the result of the function calling itself
    else:
        return list#if we can't split it, just return the original list without calling itself

num_list = [10,4,6,9,99,101,11,20,31,47,12,0,1000,284,364]
for i in range(100):
    num_list.append(random.randint(0,100000))#genarate a random list

#timer start
start = time.time()

print(QuickSort(num_list))

end = time.time()
Time = end - start
print(Time)#timer end and print run time