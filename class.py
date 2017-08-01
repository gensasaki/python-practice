# class
# function and method
# python can not restrict access right unlike private or protected

class User:
    # class variable
    count = 0
    def __init__(self, name):
        # assign to class variable
        User.count += 1
        # instance variable
        # conventionally, restricted variable's name is __somthing
        self.__name = name
    # instance method
    def say_hi(self):
        print("hi {0}".format(self.__name))
    # class method
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

# tom.say_hi()
# bob.say_hi()

User.show_info()
