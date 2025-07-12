#Exercise 5: Check if the first and last numbers of a list are the same

numbers_x = [10, 20, 30, 40, 10]
# output True
def check_first_last(*numbers_x):
    if numbers_x[0]==numbers_x[len(numbers_x)-1]:
        return(True)
    else:
        return(False)
print(check_first_last(10,49,70,78))

