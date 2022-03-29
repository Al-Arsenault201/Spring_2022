# in-class coding for Monday, March 28

dogs = {} # empty dictionary

dogs['doug'] =['beagle', 'bulldog']

dogs['bentley'] = ['Australian Cattle dog', 'golden retriever', 'boxer', 'chow']

dogs['lizzie'] = 'blue heeler'

# create a dictionary of governors

governors = {"Maryland": "Hogan", "Virginia":"Youngkin", "New York":"Hochul"}
governors['California'] = "Newsome"
governors["Maryland"] = "Rutherford"

dogs.keys()
dogs.values()

if "pepper" in dogs.keys():
    print(dogs['pepper'])
else:
    print("Sorry, that dog isn't there")


answer = dogs.get('pepper', -1)
print(answer)

name = input("What dog do you want to know about?")
answer = dogs.get(name,"Sorry, that dog isn't there")
print (answer)

dogs.values()

type = input("What type of dog do you want to look for?")
if type in dogs.values():
    print("okay, I'll look")
else:
    print("sorry, we have none of that breed")