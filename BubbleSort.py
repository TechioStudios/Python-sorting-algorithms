import random
import time

def BubbleSort(list):
    l = len(list)#get the lenth of the list
    for i in range(l-1):#go through the list l-1 times
        for n in range(l-1):#repeat through each number in the list l-1
            if list[n] > list[n+1]:#if this number is larger than the number behund it
                list[n],list[n+1] = list[n+1],list[n]#swap the numbers
    return(list)#return the result



num_list = []
for i in range(1000):
    num_list.append(random.randint(0,10000))#genorate a random list

#timer start
start = time.time()

print(BubbleSort(num_list))

end = time.time()
Time = end - start
print(Time)#timer end and print run time
# print(BubbleSort([2,1,4,10,34,5,100,25]))#call the function