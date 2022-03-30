class_list = []
with open ("student_data.txt","r") as infile:
    infile.readline() # this line reads in and throws away the header line
    data = infile.readline()
    while data != "":    # an empty string is the "End of File" marker in Python
        student = {}     # create a new dictionary to hold another student record
        data = data.split()
        student["last"]  = data[0]
        student["first"] = data[1]
        student["ID"] = data[2]
        student["project scores"] = [int(data[3]), int(data[4]), int(data[5])]
        student["project_total"] =int(data[3]) + int(data[4])+ int(data[5])
        student["test scores"] = [int(data[6]), int(data[7]), int(data[8])]
        student["test_total"] = int(data[6]) + int(data[7]) + int(data[8])
        student["total"] = student["project_total"] + student["test_total"]
        class_list.append(student)
        data = infile.readline()

    for i in range(len(class_list)):
        print(class_list[i])

