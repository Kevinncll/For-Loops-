import random
import time


#used to calculate time used to excute bubble_sort and selective_sort
def sortTime(items):
    #calculates time in milliseconds throughout the duration of bubble_sort
    timeStartbubble = time.time()
    bubble_sort(items)
    timeEndbubble = (time.time() - timeStartbubble) * 1000
    #records new time value for bubble_sort after every execution
    #Opens bubbleTime File, and appends a new Integer Within
    #Uses value determined via bubble_sort function
    print(f'It took {timeEndbubble} milliseconds to sort using Bubble Sort\n')
    bubbleTime = open("bubbleTime.txt", "a")
    bubbleTime.write(f'{timeEndbubble}\n')
    bubbleTime.close()

    #calculates time in milliseconds throughout the duration of selective_sort
    timeStartSelect = time.time()
    selective_sort(items)
    timeEndSelect = (time.time() - timeStartSelect) * 1000
    #records new time value for selective_sort after every execution
    #Opens bubbleTime File, and appends a new Integer Within
    #Uses value determined via selective_sort function
    print(f'It took {timeEndSelect} milliseconds to sort using Selective Sort\n')
    selectTime = open("selectTime.txt", "a")
    selectTime.write(f'{timeEndSelect}\n')
    selectTime.close()


#function for bubble sort algorithm
def bubble_sort(items):
    # goes through all item elements
    for i in range(len(items)):
        already_sorted = True
        for j in range(len(items) - i - 1):
            # swaps if the element found is greater than the next element
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False
        if already_sorted:
            break
    return items


#function for selective sort algorithm
def selective_sort(items):
    # goes through all item elements
    for i in range(len(items)):
        # swaps minimum element with the first element
        for j in range(i, len(items)):
            if items[j] < items[i]:
                items[i], items[j] = items[j], items[i]
    return items


#list of unsorted values
items = []

#randomized generated list using user input
userInput = input("Type of List: Random or Fixed ")
if userInput == "Random":
    amount = int(input("Input Length of List "))
    loop = 0
    while loop < amount:
        n = random.randint(1, 64000)
        items.append(n)
        loop += 1
    print(f"User List is:{items}\n")
    print(f"Sorted List is:{bubble_sort(items)}\n")
    # calls sortTime function to time algorithm
    sortTime(items)

#randomized generated list using a default length from a list of values
elif userInput == "Fixed":
    defaultLength = [1000, 2000, 3000, 4000, 5000]
    for elements in defaultLength:
        items = random.sample(range(1, 64000), elements)
        # calls sortTime function to time algorithm
        sortTime(items)
