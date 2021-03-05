n, m = input().split()
myArray = input().split()
happinessArray = set(input().split())
sadArray = set(input().split())
happiness = 0
for num in myArray:
    if num in happinessArray:
        happiness += 1
    if num in sadArray:
        happiness -= 1
print(happiness)