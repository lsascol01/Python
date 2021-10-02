# def add_dots(s):
#     out = ""
#     for letter in s:
#         out += letter + "."
#     return out[:-1]

# def remove_dots(s):
#     out = ""
#     for letter in s:
#         if letter != ".":
#             out += letter
#     return out

def add_dots(word):
    return ".".join(word)
def remove_dots(word):
    return word.replace(".","")

print(add_dots("Hola"))