def sum(num):
    if num==0:
        return 0
    return sum(num//10)+int(num%10)

print(sum(int(input('Please enter a value'))))