from classes import car
from classes import bus
from classes import students

e1c = car("dezire","white",5363)
print(e1c.color + str(e1c.price) + e1c.model)

s1 = students(56,"julia","computer")
s2 = students(75,"john","econ")
s3 = students(79,"smith","chem")

print(s1.should_call_parents())

print(s2.should_call_parents())

print(s3.should_call_parents())
