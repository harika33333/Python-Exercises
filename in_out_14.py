#You have two lists: names = ["Alice", "Bob", "Charlie"]
# and scores = [85, 92, 78]. Print these lists as a simple table
# with columns “Name” and “Score”.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# Name       Score
# ---------------
# Alice      85
# Bob        92
# Charlie    78
print("Name       Score")
print("---------------")
for i in range(len(names)):
    print(names[i],scores[i])
