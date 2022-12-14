import random
import time

def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n - 1)

def choose(n, k):
return factorial(n) / (factorial(k) * factorial(n - k))

def binomial(n, k, p):
return choose(n, k) * pk * (1 - p)(n - k)

def main():
random.seed(time.time())

while True:
    n = random.randint(0, 10)
    k = random.randint(0, n)
    p = random.random()

    print(f"binomial({n}, {k}, {p:.2f}) = {binomial(n, k, p):.3f}")

    try:
        again = input("Again? [y/n] ")
        if again.lower() != "y":
            break
    except EOFError:
        break
if name == "main":
main()
