#5.write a program to find sum of square of even numbes

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = list(filter(lambda x: x % 2 == 0, a))
e = list(map(lambda x: x ** 2, d))
total = sum(e)
print("Even numbers:", d)
print("Squares of even numbers:", e)
print("Sum of squares:", total)

