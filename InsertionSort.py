import time
import random

def InsertionSort(list):
    l = len(list)#get list length
    for i in range(1,l):#start comparing on the second number
        key = list[i]#set the first uncompared number as the key(save its value)
        n = i - 1#first sorted number to compare the key to(save its pos)
        while n >= 0 and list[n] > key:#keep looping until n is smaller than 0 or the comparing number is smaller than the key(which means the key goes here)
            list[n+1] = list[n]#move the compared number oonto where th key is right now
            n = n - 1#n minus one, so the next time we can compare to the number before it
        list[n+1] = key#once we found where the key is supposed to go, insert it in its proper place(we have to plus one because that's the last thing we did in the loop)
    return list#return the result

num_list = []
for i in range(1000):
    num_list.append(random.randint(0,10000))#genorate a random list

#timer start
start = time.time()

print(InsertionSort(num_list))

end = time.time()
Time = end - start
print(Time)#timer end and print run time