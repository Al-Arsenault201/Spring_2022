# how to read in and create a 2D list from a Comma-Separated-Value (.csv) file
filename = "/Users/alfredarsenault/Downloads/Winter_Olympics_Medal_Table - Sheet1.csv"
with open(filename,"r") as infile:
    data = infile.read()
    data_list = data.split("\n")
    data_list.pop(0)
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(',')
