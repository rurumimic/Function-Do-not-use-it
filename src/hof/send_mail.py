def make_mail(func):
    def inner(name):
        return func(name)
    return inner

def hello(name):
    return "Hello, " + name

def goodbye(name):
    return "Goodbye, " + name


if __name__ == "__main__":
    import inspect

    email_to = make_mail(hello)
    print(type(email_to), inspect.signature(email_to)) # <class 'function'>, (name)

    print(email_to("Alice"))
    print(email_to("Charlie"))

    print(make_mail(goodbye)("Alice"))
    print(make_mail(goodbye)("Charlie"))
