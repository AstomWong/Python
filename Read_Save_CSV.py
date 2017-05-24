import csv
import os
import sys

#This part is open the CSV File
pathProg = 'put your location here!'
os.chdir(pathProg)

if os.getcwd() != pathProg:
    print "EEROR: the file path incorrect."
    sys.exit()
    
#File_name could be any, included the file which is not exist
file = open(pathProg + 'file_name', 'r')
csvCursor = csv.reader(file)

for row in csvCursor:
    # push the data into list
    rawData.append(row)
    #print Data

#To push the data into a list, using this line 23 to add the data into csv
csvCursor.writerows('list_name')

#At the end, you need to close for safty
file.close()