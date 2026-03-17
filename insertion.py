def insertion_sort(arr):
a = arr[:] # do not modify original array
n = len(a)
for i in range(1, n):
key = a[i]
j = i - 1
while j >= 0 and a[j] > key:
a[j + 1] = a[j]
j -= 1
a[j + 1] = key
return a
