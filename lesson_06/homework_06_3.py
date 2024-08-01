lst1: list[object] = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2: list[str] = [item for item in lst1 if isinstance(item, str)]

# for item in lst1:
#     if isinstance(item, str):
#         lst2.append(item)

print(lst2)
