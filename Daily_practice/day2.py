"""
nums = [1, 2, 3]
a = nums
a.append(4)
print(nums)
print(a)
This should print the same answer for both.
We are using the concept of binding and mutation
output: [1,2,3,4]
"""

text = str(input("Enter the string: "))
text = text.lower()
text = text.split()
TextSet = set(list(text))
ResultDict = {}

for i in TextSet:
    # Idea here is to check for each substring from set to main string.
    count = 0
    for j in text:
        if i == j:
            count = count + 1
    ResultDict[i] = count

print(ResultDict)