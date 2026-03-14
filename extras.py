#list method convert into list
s = "abc"
convert_into_list = list(s)
print(convert_into_list)
#Replace
school = "kaushal,vidhyabhavn"
print(school.replace(","," "))

#strip- it removes from start and end of the string

name = "$$$$$my name is sneh$$"
print(name.strip("$"))

#Split-Splits a string into a list using a separator

fruits = "apple banana mango"
veges = "potato,tomato,brinjal"
print(fruits.split())
print(veges.split(","))

# Insert something at a specific index

text = "HelloWorld"
index = 5
new_text = text[:index] + " " + text[index:]
print(new_text)  # Output: Hello World

# Insert between words (split & join)
sentence = "My name is Sneh"
words = sentence.split()  # ['My', 'name', 'is', 'Sneh']
new_sentence = " INSERT ".join(words)
print(new_sentence)  # Output: My INSERT name INSERT is INSERT Sneh
