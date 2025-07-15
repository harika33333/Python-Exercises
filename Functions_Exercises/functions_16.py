# Given:
#
numbers = [1, 2, 3, 4, 5]
# Expected Output:
#
# The doubled numbers are: [2, 4, 6, 8, 10]

def double_num(num_list):
    s=[]
    for i in num_list:
        s.append(i*2)
    return(s)
print("The doubled numbers are:",double_num(numbers))
