# Countdown - Create a function that accepts a number as an input.  
# Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  
# For example countDown(5) should return [5,4,3,2,1,0].
def countdown(num):
    for i in range(num, 0, -1):
        print(i)
print(countdown(5))

# Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.
def printreturn(arr):
    print(arr[0])
    return arr[1]
print(printreturn([1,2]))

# First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.
def first_plus_length(arr):
    return arr[0] + len(arr)
print(first_plus_length([1,2,3,4]))

# Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  
# Print how many values this is.  If the list is only one element long, have the function return False
def values_greater_than_second(arr):
    newArr = []
    if len(arr) <= 1:
        return False
    for i in arr:
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            print(len(newArr))
            return newArr
print(values_greater_than_second([2,3,4]))

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. 
# This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size, value):
    newArr = []
    for i in range(0, size):
        newArr.append(value)
        return newArr