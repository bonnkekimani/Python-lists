lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

# min(lst)
print("Maximum element in the list is:", max(lst),
    #   "\n Second largest element in the list is:", numbers-1(lst),
      "\n Minimum element in thr list is:", min(lst))