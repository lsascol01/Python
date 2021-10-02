# def double_letters(word):
#     word=str(word)
#     memory=""
#     double=False
#     for i in word:
#         if i == memory:
#                 double=True
#                 break
#         else:
#             memory=i
#     if double == True:
#         return True
#     else:
#         return False
#     # naive solution
# def double_letters(string):
#     for i in range(len(string) - 1):
#         letter1 = string[i]
#         letter2 = string[i+1]
#         if letter1 == letter2:
#             return True
#     return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
print(double_letters("abcc"))