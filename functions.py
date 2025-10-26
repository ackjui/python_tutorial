def greet(name):
    print("Hello " + name)

# greet("Alice")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        print(a, end=",")

#fibonacci(10)

def fibonacci_list(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        a, b = b, a+b
        result.append(a)
    print(result)

#fibonacci_list(10)

def default_args(prompt, retries = 4, reminder="Please Try Again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "yes", "yo", "ye"}:
            return True
        if reply in {"n", "no", "naa"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)

#default_args("Do you want to see? : ")


def cheesecakeshop(kind, *name, **kwargs):
    print("Do you have,", kind, "?")
    print("Interesting, you do have", kind, ".")

    for n in name:
        print(n)
    print("-" * 40)

    for kw in kwargs:
        print(kw, " : ", kwargs[kw])

# cheesecakeshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

