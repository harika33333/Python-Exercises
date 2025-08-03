# Exercise 8: Print the value of key ‘history’ from nested dict
sampleDict = {
     "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# Expected output:
#
# 80
print(sampleDict['class']['student']['marks']['history'])
