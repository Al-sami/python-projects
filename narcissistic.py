def narcissistic(value):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        i = int(i)
        sum += i**size
    value = int(value)
    if(value == sum):
        return True
    else:
        return False

print(narcissistic(371))

