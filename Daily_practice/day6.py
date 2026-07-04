"""


data = {
    "A": [1, 2],
    "B": [3]
}

copy = data

copy["A"].append(5)

print(data)
print(copy)


hmmm. i feel that A will get appended as the strict condition of immutability is only for the keys.
Not the values. 
this looks like an example of rebinding as we are binding copy to the object dictionary. 
same dict where data is bound. 

so it should print the updated dictionary. 
like 
{ "A" : [1,2,5] , "B" : [3]}
for both. 


"""

# I am only allowed to use dicts and if time allows file handling. 
# first i will make the dictionary. 
# then the fuctions. i will pass the list of marks and dicts to them for different operations. 
# then for the last on i will be standard file handling print to make a file. 

# the dict declaration and initialization. 

#-----functions----------------------------------------------------------------------------

def highest_marks(data):

    topper = data[0]

# sadly still no guard against multiple same enteries. 

    for i in range(len(data)):
        if topper >= data[i]:
            continue

        elif topper < data[i]:
            topper = data[i]

    return topper


def average_marks(data):

    sum = 0 

    for i in range(len(data)):
        sum = sum + data[i]

    return sum/len(data)



def passed_students(data):

 # i can't seem to get this function. the logic to get back the keys is little wonky. 

    graduates = { k: v for k, v in data.items() if v >= 40}

    # i will not deny here. i took help of internet. as i knew i had to filter the dict.
    # but i did not know the syntax for it. though it looks a bit complex by my standards. 
    # but here the idea is to first filter the dict as per the condition. 
    # and then just return the keys. 

    return list(graduates.keys())
            



#------------Main block-----------------------------------------------------------------------

while True: 
    try:
        numberOfStudents = int(input("Enter the number of students: "))
        break

    except ValueError:
        print("Wrong Input!!!. Try again.")
        break # yep i took into account the possible zero enter or negative entry or char enter. 


print("Enter student data: ")

studentData =  {}

for i in range(numberOfStudents):
    while True:
        try:
            name = input("Student name: ")
            break
        except ValueError:
            print("Enter correct names.")
            break

    while True:
        try:
            marks = int(input("Student marks: "))
            break
        except ValueError:
            print("Enter correct values only!!!")
            break

    # the above conditions will need some more refinement as i have not fully resolved the error yet. 

    studentData[name] = marks


avg = average_marks(list(studentData.values()))
print(f"The average is : {avg}")

highMarks = highest_marks(list(studentData.values()))
print(f"The highest marks are: {highMarks}")

graduates = passed_students(studentData)
print(f"The students who graduated are: {graduates}")


data = str(studentData) # i will need to see how separate them with \n. 

with open("student.txt", 'w+') as f:
    f.write(data)

    f.close()

    



#---------End of main block-------------------------------------------------------------------------------------


 
