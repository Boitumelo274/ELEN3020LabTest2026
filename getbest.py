#!/usr/bin/env python3

import sys # used to read the CSV filename in the same project folder

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''

    #Read the first line of the file(header-row)
    #and split it into a list using commas
    headings = f.readline().strip().split(",")
    
    #initialising column indexes
    #This block had a wrong column indexing of i = 1
    # i was never incrementing , so both num_col and mark_col would end up as 1
    # It had an indexing bug
    num_col = mark_col = -1 

    # Loop through headings with their index
    for i, head in enumerate(headings):

        #find which column contains "Student Number"
        if head == "Student Number": num_col=i

        #finds whcih column contains "Marks"
        elif head == "Mark" : mark_col = i
    return (num_col, mark_col)


def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''

    #Wrong indexing was here again. Both best and best_idx were tired to 0 so 
    #good for best but best-idx was nevr updating it was always 0.
    best =  0
    best_idx = ""

    #loop through each remaining line in the file
    for line in f:

        #removes spaces/newlines and split by comma
        data = line.strip().split(",")
        # convert mark column into integer
        mark = int(data[mark_col])
        # check if this student has the highest mark so far
        if mark > best:
            best=mark # updating the mark
            best_idx = data[num_col] # then store the student Number

    return best_idx, best # return the top student and their mark

f = open(sys.argv[1]) # opens the CSV file passed 
num_col, mark_col = getCols(f) #finds which columns contains student number and mark
best_idx, best = findTop(f,num_col,mark_col) # find the top student in the remaining file data
print("The top student was student %s with %d"%(best_idx,best)) #prints the final result

f.close() # close the file , so there are no free resources
