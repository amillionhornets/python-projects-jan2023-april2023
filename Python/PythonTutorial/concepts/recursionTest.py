

# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps-1)
#     print(f"You take step #{steps}")

# walk(100)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

if __name__ == "__main__":
    print(factorial(10))