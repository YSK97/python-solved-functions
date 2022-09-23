#To create function to find length of string

def findLen(str):
    count = 0   
    for i in str:
        count += 1
    return count
str='apple'
print(findLen(str))
