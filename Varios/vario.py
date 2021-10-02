# def flatten(list):
#     super_list=[]
#     for i in list:
#         for j in i:
#             super_list.append(j)
#     return super_list
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]


print(flatten([[1, 2], [3, 4]]))


