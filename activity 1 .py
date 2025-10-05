#TO ask the user for their scores in 5 different  subjects and to calculate the total of it
English=int(input("what is your score in English ?"))
math=int(input("what is your score in math?"))
science=int(input("what is your score in science?"))
geography=int(input("what is your score in geography?"))
history=int(input("what is your score in history?"))
print(English+math+science+geography+history)


#TO ask the user for their scores (float) in 5 different  subjects and to calculate the total of it
english=float(input("what is your score in english"))
math=float(input("what is your score in math"))
science=float(input("what is your score in science"))
geography=float(input("what is your score in geography"))
history=float(input("what is your score in history"))
print(english+math+science+geography+history)


#to ask the user for their choice of cake and return the total bill amount
quantity=int(input("How many slice of lotus biscoff cake do you want?"))
print(quantity)
totalcost=20*quantity
print(totalcost)
#Convert the following into boolean: "True", "False", "0", "1".
a="True"
b=bool(a) 
print(b)
print(type(b))

c=bool("False")
print(c)
print(type(c))

d=bool("0")
print(d)
print(type(d))

e=bool("1")
print(e)
print(type(e))