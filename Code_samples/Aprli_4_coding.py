# in-class coding for Monday, April 4

with open("/Users/alfredarsenault/Documents/GitHub/Spring_2021/Spring_2021_projects/Spring_2023.csv","r") as infile:
    #read the first two header lines in the file and throw them away
    infile.readline()
    infile.readline()
    # now we get to the real data

    data = infile.readlines()  #reads the REST of the file into a list

    #check to see what we have by printing
    for i in range(len(data)):
        data[i] = data[i].split(',')  #if this is .tsv: change this to .split("\t")
        for j in range(3,9):
            data[i][j] = int(data[i][j])

        #insert a new column 6 that is the total of the 3 project scores
        data[i].insert(6, data[i][3] + data[i][4] + data[i][5])

        #insert a new column 10 that is the total of the 3 test scores
        data[i].insert(10, data[i][7] + data[i][8] + data[i][9])

        #now append a letter grade to the end of each row
        total_points = data[i][6] + data[i][10]
        if total_points >= 576:
            grade = "A"
        elif total_points >= 512:
            grade = "B"
        else:
            grade = "C"
        data[i].append(grade)
        print(data[i])


    #Now, let's find all the students who got an A
    for i in range(len(data)):
        if data[i][-1] == "A":
            print(data[i][1], data[i][0])

    #find all the students who got a "C" and print out a warning notice
    for i in range(len(data)):
        if data[i][-1] == "C":
            print (data[i][1], data[i][0], " we have notified the coach \n You need to improve this grade")

    #    print(data[i])

#now we're going to try writing a .csv file

with open("/Users/alfredarsenault/PycharmProjects/results.csv","w") as outfile:
    for i in range(len(data)):
        for j in range(3,11):
            data[i][j] = str(data[i][j])
        newstring = ",".join(data[i])
        outfile.write(newstring + "\n")