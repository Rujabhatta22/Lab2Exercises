#weight converter:
#input the weight of a person in either kg or lbs. if person provides his/her weight in kg
#convert it intp lbs else convert into kg
temp=0
weight = float(input("enter your weight in kg or lbs:"))
choose = input("kg or in lbs")
if weight==kg:
    weight=weight*2.2406
elif weight==lbs:
    weight=weight/2.2406
print(f"weight is {weight}")
