#if temperature is greater than 30, its a hot day otherwise if its less than 10;
#its a cold day; otherwise, its neither hot nor cold.
temperature = float(input("enter the temperature"))
if temperature>30:
    print("it is a very hot day")
elif temperature<10:
    print("it is a cold day")
else:
    print("its neither hot nor cold")
