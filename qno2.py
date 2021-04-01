#WAP which accepts marks for four subject and display total marks, percentage and grade.
#Hint: more than 70%_> distinction, more than 60% _> first, more than 40% _> pass, less than 40% _> fail.
maths=int(input('enter the marks'))
english=int(input('enter the marks'))
physics= int(input('enter the marks'))
chemistry=int(input('enter the marks'))
sum= maths + english + physics + chemistry
percent = sum/100 * 100
if percent >= 70:
    print('distinction')
if percent >= 60:
    print('first division')
if percent >= 40:
    print('pass')
else:
    print('fail')