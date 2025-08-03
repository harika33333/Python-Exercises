list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(id(list_a))
print(id(list_b))
# 125657119640384
# 125657119642176


list_a = [1, 2, 3]
list_b = list_a
print(id(list_a))
print(id(list_b))
# 138327136940608
# 138327136940608



list_a = [1, 2, 3, 5]
list_b = list_a
list_b[3] = 4
print("list a : " + str(list_a))
print("list b : " + str(list_b))
# list a : [1, 2, 3, 4]
# list b : [1, 2, 3, 4]
list_a = [1, 2]
list_b = list_a
list_a = [6, 7]
print("list a : " + str(list_a))
print("list b : " + str(list_b))
print(id(list_a))
print(id(list_b))
# list a : [1, 2]
# list b : [6, 7]
# 134725517365824
# 134725517364032


list_a = [1, 2]
list_b = list_a
list_a = list_a + [6, 7]
print("list a : " + str(list_a))
print("list b : " + str(list_b))
print(id(list_a))
print(id(list_b))
# list a : [1, 2, 6, 7]
# list b : [1, 2]
# 131783638831680
# 131783639145600


list_a = [1, 2]
list_b = list_a
list_a += [6, 7]
print("list a : " + str(list_a))
print("list b : " + str(list_b))
print(id(list_a))
print(id(list_b))
# list a : [1, 2, 6, 7]
# list b : [1, 2, 6, 7]
# 137921027558208
# 137921027558208


list_a = [1,2]
list_b = [3, list_a]
list_a[1] = 4
print(list_a)
print(list_b)
print(id(list_a))
print(id(list_b))
# [1, 4]
# [3, [1, 4]]
# 131802997644416
# 131802997330496



