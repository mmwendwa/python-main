def announce(f): #A decorator is a function that modifies another function and returms the new decorated one
    def wrapper():
        print("About to run the function...!")
        f()
        print("Done with the function")
    return wrapper


# Example

@announce
def hello():
    print("Hello, World!")

hello()
