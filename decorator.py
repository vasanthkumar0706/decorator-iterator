def uppercase(func):
    count = 0

    def wrapper():
        count += 1

        print("before function called...")
        print("function called", count, "times")

        func()
        print("after function called...")

    return wrapper

uppercase
def greet():
    print("hello greet")

greet()
greet()
greet()
