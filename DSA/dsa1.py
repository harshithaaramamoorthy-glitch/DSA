"""n = 12345
total = 0
while n > 0:
    last = n% 10 # 5
    total = total + last #5 (total+=last)
    n = n // 10 
    print(total)"""


"""a = [1,2,3,4,5]
if 4 in a:
    print("4 is in a list:)"""
"""def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam")) 
print(is_palindrome("hello"));"""




"""x = 10
a = [1001]
b = a[::-1]
a==b
while start<end:
    if a[start]!=a[end]:
        start+=1
        end-=1
        return False"""



"""n=int(input())
left=n.bit_length() - 1
right = 0  
while left > right:
    l = (n>>left) & 1 
    r = (n>>right) & 1 
    if l !=r:
        print("not palindrome")
        break
    left += 1
    right -= 1
else:
    print("Is palindrome")"""


"""#selection sort
def selection_sort(lst1):
    n = len(lst)
    for z in range(n):
        min_index = z #
        for x in range(z+1,n):
            if lst1[x] < lst[min_index]:
                min_index = x # 3
        lst1[z], lst1[min_index] = lst1[min_index], lst1[z]
    
    return lst1
# 11 25 12 22 64
# 11 12 25 22 64
# 11 12 22 25 64

lst = [64,25,12,22,11] # 11 12 22 25 64
selection_sort(lst)"""


# Quick sort
# choose a pivot
# smaller then pivot goes left
# larger then pivot goes 

def Quick_sort(lst1):
    if len(lst1) <= 1:
        return lst1
    else:
        pivot = lst1[0]
        left = [x for x in lst1[1:] if x <= pivot]
        right = [x for x in lst1[1:] if x > pivot]
        return Quick_sort(left)+ [pivot] + Quick_sort(right)        
        for i in lst1[1:]:
            if 1 <= pivot:
                left.append(i)


lst = [20,25,12,22,11] # 11 12 22 25 64
print (Quick_sort(lst))



