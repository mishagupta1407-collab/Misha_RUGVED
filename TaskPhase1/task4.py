# Write a python function to perform selection sort on a given string.

def selection_sort_string(s):
    ls = list(s)
    n = len(ls)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if ls[j] < ls[min]:
                min = j
        ls[i], ls[min] = ls[min], ls[i]
    return ''.join(ls)

s = input("Enter a string: ")
sortedstr = selection_sort_string(s)
print("Sorted string:", sortedstr)
