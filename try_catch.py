#try_catch
try:
    age = int(input("age: "))
    print(age)
    err = 20/(age)
except ValueError:
    print("invalid")
except ZeroDivisionError:
    print("invalid division")
