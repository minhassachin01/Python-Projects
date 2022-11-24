#Part-1 The simplest encryption algorithm!
import string
print("Part 1: The simplest encryption algorithm!")
mainline = input("Enter a string : ")
number = int(input("Enter a number for rotation: "))
maintext = " "


def ceaser_cypher(maintext, number):
    if maintext.isupper():
        startrotation = ord('A')
    elif maintext.islower():
        startrotation = ord('a')
    else:
        return maintext
    differnce = ord(maintext)-startrotation
    rotatedword = (differnce+number) % 26+startrotation
    return chr(rotatedword)


def roatate_line(mainline, number):
    rotatedline = ''
    for maintext in mainline:
        rotatedline += ceaser_cypher(maintext, number)
    return rotatedline


roatate = ceaser_cypher(maintext, number)
roatateline = roatate_line(mainline, number)
print("Orginal string is: ",mainline)
print("Rotated string is: ",roatateline)

#Part-2 Binary Search Algorithm Implementation in Python
print("Part 2: Binary Search Algorithm Implementation in Python")
item_list = []
user_list = int(input("Enter numbers of elements: "))
print(f"Enter {user_list} numbers in sorted: ")
for i in range(0, user_list):
    ele = int(input())
    item_list.append(ele)
sorted_list = sorted(item_list)
print("list is: ", sorted_list)
item = int(input("Enter a number you want to search : "))
first = 0
last = len(item_list)-1


def binary_search(first, last, item, sorted_list):
    found = 0
    while (first <= last and not found):
        mid = (first+last)//2
        if sorted_list[mid] == item:
            found = 1

            print(f"Number is at {mid+1}th position in the list.")

        else:
            if item < sorted_list[mid]:
                last = mid-1
            else:
                first = mid+1
    return found


def found_or_notfound(search):
    if search == 0:
        return 'Number not found'
    else:
        return 'Number found'


search = binary_search(first, last, item, sorted_list)
print(found_or_notfound(search))

import math

#Part-3 Formula Implementation
print("Part 3: Formula Implementation")
def factorial(n):
    if n == 0:
        return 1
    else:
        return math.factorial(n)


def estimate_pi():
    total = 0
    k = 0
    factor = float(2*math.sqrt(2)/9801)
    keep_going = True
    while keep_going == True:
        whole_numerator = float(factorial(4*k)*(1103+(26390*k)))
        whole_demonitor = float((factorial(k)**4)*(396**(4*k)))

        total_part = float(factor*(whole_numerator/whole_demonitor))
        total += total_part
        k += 1
        if total_part < 1e-15:
            keep_going == False
            break
    return 1/total


pi = estimate_pi()
print("value of pi is: ", pi)

