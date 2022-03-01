#in-class coding for Monday, February 28

phrase = "You put your left hand in, you put your left hand out"
words = phrase.split()
print (words)

# string_var = "separator".join(list_var)

new_phrase = "".join(words)
print(new_phrase)

next_phrase = " ".join(words)
print(next_phrase)

#separate by any valid Python string
again = "\t".join(words)
print(again)

ridiculous = "ridiculous ".join(words)
print(ridiculous)
