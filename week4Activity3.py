"""
Jingwen Guan
Week 4 activity 3
"""
#example 1 ) for loop: create a for loop that will print 20 times that message "hello World"
for x in range (0,20):
    print('Hello',x)

#example 2) for loop with three arguments
#print from 2 to 30(exclusive) with an increment of 3

for x in range(2,30,3):
    print("Now counter is: ",x)

#example 3) for loop that will display from 10 to 0 with a decrement of 2

for x in range(10,-20,-2):
    print("decrement: ",x)

#example  4)for loop through an array
colors =['red', 'blue', 'green', 'yellow','pink']
    for c in colors:
        print(c)
# example 6) nesting for loop and if statement
#use a for loop to print numbers form 0 to 10 (exclusive) and break when the counter reaches 5
print("Example 6")
for counter in range(0,10):
    print(counter)
    if counter==5:
        print("Counter = ",counter)
        break
print('Line outside of for loop')
#example 7) use for loop to skip number 8 in the count from 10 to 0 with decrement
for e in range(10,0,-1):
    if e ==8:
        continue
        print(e)
        print('Line outside of for loop')
#example8 )using for loop to skip numbers that are multiple of 4 in the count form 10 to 0 with decrement of -1
print ('example 8 ')
for counter in range(10,0,-1):
    if counter %4 ==0:
        print(counter)
        print(counter)
        print('Line outside of for loop')
#example 9)Print all numbners from 10 to 0, and print a message Happy New Year!
print('Example 9')
for counter in range(10,-1,-1):
    print(counter)
else:
    print("Happy New Year!")


# example 10) use a while loop to print numbers form 1 to 6 (exclusive )
print('\n Example 10\n')
counter = 1
while counter<6
print("while loop now is counting ", counter)
counter +=1
#example 11) use a while loop to check if a number is between 0 and 10
print('\n Example 11\n')

number = int(input("Enter a number between 0 and 10: "))
    #ACTIVITY 3A
print("================ACTIVITY 3A============")
    num = input('Enter the number of fruits: ')
for num in range (1,num):
