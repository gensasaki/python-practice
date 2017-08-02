# module

# import module2
# from module2 import AdminUser, User

# package

# import package.module2 as mymodule
from package.module2 import AdminUser

# bob = module2.AdminUser("bob", 23)
# bob = AdminUser("bob", 23)
# bob = mymodule.AdminUser("bob", 23)
bob = AdminUser("bob", 23)

# tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()
