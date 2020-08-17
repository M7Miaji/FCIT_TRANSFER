import college_requirements_greater_than_15 as cg
import college_requirments_less_than_15 as cl
import no_student_check as no_stu
import student_applied as sa
import lowest_grade as lw
import xlrd

# _______________________________________
# this is for the excel file to be read.
loc = "sample_fcit.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# _______________________________________


# For row 0 and column 0
# print(int(sheet.cell_value(1, 0)))
# print(sheet.row_values(1,0))
# First we will need to check if the students are less than 15
# so that we can decide if we need a second checking
# brings out the number of students
# and the numbers of columns
stu_row = sheet.nrows - 1
stu_col = sheet.ncols - 1

# this part is where all the data is stored so that it can be used
# it is an array of arrays that contains the data for each student
# the first index is for the student ID number
# num_stu_less_15 = no_stu.no_student.check(stu_row)

array2 = [[0 for i in range(stu_col)] for j in range(stu_row)]
k = 1
for i in range(stu_row):
    for j in range(stu_col):
        k = i + 1
        array2[i][j] = sheet.cell_value(k, j)

# _________________________________________________________________
# This part is to add a zero to the list to make it easier to sort
lw.sort_stu.add_zero(array2)
org_array = array2
pass_array = [0 for i in range(stu_row)]
# This is where the sorting happens
# so = lw.sort_stu.lowest_highest(array2, 2)
if no_stu.no_student.check(stu_row):
    for i in range(stu_row):
        if sa.applied.success(array2[i]):
            pass_array[i] = array2[i][0]

print(pass_array)

# for i in range(stu_row):
#    print(*array2[i])
#    print("------------------------------")

# A sample has been provided for testing there
# are several types of files such as an excel,
# an text and several others to test
# Go to the documentation file to understand
# how to implement these techniques
