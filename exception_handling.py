# exception handling

class MyException(Exception):
    pass

def div(a, b):
    try:
        if (b > 0):
            raise MyException("not minus!")
        print(a / b)
    except ZeroDivisionError:
        print("not by zero!")
    except MyException as err:
        print(err)
    else:
        print("no exception!")
    finally:
        print("-- end --")


div(10, 0)
div(10, 3)