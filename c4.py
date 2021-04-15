#Given threeintegers, print the smallestone.(Threeintegers should be user input)
num_1=int(input("enter 1st integer"))
num_2=int(input("enter 2nd integer"))
num_3=int(input("enter 2nd integer"))
if num_1>num_2<num_3:
    print(f'{num_2}is the smallest')
elif num_2>num_1<num_3:
    print(f'{num_1} is the smallest')
else:
    print(f'{num_3} is the smallest')