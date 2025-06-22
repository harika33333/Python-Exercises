# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
# For example, if the input is 12, the output should be “00012“

num=int(input("enter a number:"))

len_num=len(str(num))

diff=5-len_num
print(str(0)*diff+ str(num))
