# compare two lists using python
list1 = [10, 20, 30, 40, 50]
list2 = [50, 60, 30, 80, 90]

res = [x for x in list1 +list2 if x not in list1 or x not in list2]

print(res)
if not res:
    print("both the number lists are equal")
else:
    print("both the list are not equal")