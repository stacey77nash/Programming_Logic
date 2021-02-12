#PROGRAM: testAverage.py
#COURSE: ITSE 1311 20Z1
#AUTHOR: Stacey Nash
#DESCRIPTION: The program testAverage.py will calculate and display the average of four test grades.

# print statements prompt the user for input
# test scores are cast to INTEGER

print("Enter test 1 score, and press ENTER:")
test1 = int(input())
print("Enter test 2 score:")
test2 = int(input())
print("Enter test 3 score:")
test3 = int(input())
print("Enter test 4 score:")
test4 = int(input())

#testAverage is cast to FLOAT in order to display decimal values for averages that are not integers
#testAverage is calculated by adding the test scores and dividing the sum by the number of test scores

testAverage = float((test1 + test2 + test3 + test4) / 4)

#testAverage is output and cast as a STRING

print("Average test score is: " , testAverage)
