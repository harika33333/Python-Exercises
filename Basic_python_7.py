#Exercise 7: Find the number of occurrences of a substring in a string

str_x = "Emma is good developer. Emma is a writer"
word=""
word_lst = []
for i in str_x:

    if i not in [" ", "."]:
        word += i
    if (i==" "):
        word_lst.append(word.lower())
        word = ""
if word:
    word_lst.append(word.lower())
#print(word_lst)
count = {}
for i in word_lst:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
#print(count)

max_list=[]

for i in count:
    max_list.append(count[i])
max_list= sorted(max_list,reverse=True)
#print(max_list)

for i in max_list:
    for j, k in count.items():
        if (i==k):
            print(j,"appears",k,"times")
            max_list.remove(i)


