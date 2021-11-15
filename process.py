log_file = open("um-server-01.txt") # opening the um-server-01.txt file so the information can be accessed and giving it a simpler name


def sales_reports(log_file): #creating a function that is taking in the opened file
    for line in log_file: #looping over each line in log_file
        line = line.rstrip() #removing any whitespace at the end of the string
        day = line[0:3] #grabbing the first three characters in the string
        if day == "Mon": #if statement to be used if day has a value of 'Tue'
            print(line) #prints out line if if statement is true


sales_reports(log_file) #closes the file
