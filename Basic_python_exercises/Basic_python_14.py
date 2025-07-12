# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *
# * * * *
# * * *
# * *
# *
def my_patterns():
    s=""
    for i in range(5,0,-1):
        s=s+("* "*i)+"\n"
        return(s)

