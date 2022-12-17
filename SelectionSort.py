import time
import random

def SelectionSort(list):
    l = len(list)#get length
    for i in range(l-1):#loop n-1 times(skip the ones at the start)
        min = i#set min to the first unsorted number
        for n in range(i+1,l):#start comparing with the second unsorted number
            if list[n] < list[min]:#if this number is smaller than the current largest
                min = n#update the min number
        list[i],list[min] = list[min],list[i]#after finding the smallest number, swap it with the first unsorted number
    return list

num_list = []
for i in range(1000):
    num_list.append(random.randint(0,10000))#genorate a random list

#timer start
start = time.time()

print(SelectionSort(num_list))

end = time.time()
Time = end - start
print(Time)#timer end and print run time