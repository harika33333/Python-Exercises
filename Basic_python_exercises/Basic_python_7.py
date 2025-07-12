#Exercise 7: Find the number of occurrences of a substring in a string

def word_list(str_x):
    global my_str
    my_str=str_x
    words = my_str.split(" ")
    return(words)

def count_occurences(words):
    count={}
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    return(count)

def sorted_maxlist(count):
    max_list=[]
    for i in count:
        max_list.append(count[i])
    max_list= sorted(max_list,reverse=True)
    return(max_list)


words=word_list("Emma is good developer. Emma is a writer")
print(words)
count=count_occurences(words)
print(count)
max_list=sorted_maxlist(count)
print(max_list)


for i in max_list:
    for j, k in count.items():
        if (i==k):
            print(j,"appears",k,"times")
            max_list.remove(i)


