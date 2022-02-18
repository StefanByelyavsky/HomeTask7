lst = [1,0,3,0,0,0,5]
print(lst)
a = 0
lst_a = list()
while a < len(lst):
    if lst[a] != 0:
        a += 1
    else:
        lst_a.append(lst[a])
        del(lst[a])
        a = a - 1
lst.extend(lst_a)
print(lst)