def largest_difference(list1):
    list1=sorted(list1)
    return list1[-1] - list1[0]

# # short solution
# def largest_difference(numbers):
#     return max(numbers) - min(numbers)

# # naive solution
# def largest_difference(numbers):
#     smallest = 100
#     for n in numbers:
#         if n < smallest:
#             smallest = n

#     largest = -100
#     for n in numbers:
#         if n > largest:
#             largest = n

#     difference = largest - smallest
#     return difference
print(largest_difference([1, 5, 3,90]))