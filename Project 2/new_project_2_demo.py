with open("/Users/alfredarsenault/Project_2_data/Fall_2025.csv") as nextfile:

#the next two lines get rid of the two header lines that we don't care about
    nextfile.readline()
    nextfile.readline()

#now read the data we do care about
    results = nextfile.readlines()

# split each row on commas because that's how we handle .csv files
for i in range(len(results)):
    results[i] = results[i].split(",")

#test a little - what does this look like?
for entry in results:
    print(entry)
#oh good, it's working correctly to here

#now - create the list of dictionaries
# one dictionary per student

class_list = []

#for each student in my class I'm going to create a dictionary
for entry in results:
    d = {}
#    if entry[0][0] == '"':
#        entry[0] = entry[0][1:]  # gets rid of an initial double quote
    d["last_name"] = entry[0]
#    if entry[1][-1] == '"':
#        entry[1] = entry[1][:-1] #gets rid of the double quote at the end of the first name
    d["first_name"] = entry[1]
    d["Student_ID"] = entry[2]
    d["Projects"] = [int(entry[3]), int(entry[4]), int(entry[5])]
    d["Tests"] = [int(entry[6]), int(entry[7]),int(entry[8])]
    class_list.append(d)
# test a little
for entry in class_list:
    print(entry)

#getting rid of quotes:
for i in range(len(class_list)):
    if class_list[i]["last_name"][0] == '"':
        class_list[i]["last_name"] = class_list[i]["last_name"][1:]
    if class_list[i]["first_name"][-1] == '"':
        class_list[i]["first_name"] = class_list[i]["first_name"][:-1]
#test a little
for entry in class_list:
    print(entry)

#add the extra fields
for i in range(len(class_list)):
    class_list[i]["Project total"] = class_list[i]["Projects"][1] + class_list[i]["Projects"][2] + class_list[i]["Projects"][0]
    class_list[i]["Test total"] = # the same formula but with tests
    class_list[i]["Total"] = class_list[i]["Project total"] + class_list[i]["Test total"]
    # now calculate letter grade - it's an if - elif -elif - elif - else


# all of this deals with reading in one file


