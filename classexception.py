class NumberError(Exception):
    pass
try:
    age=int(input("age:"))
    if age<20 or age>=80:
        raise NumberError()
except ValueError:
    print("please give the valid integer")
except NumberError:
    print("please give the valid positive integer and value in between 20-80")
else:
    print(age)