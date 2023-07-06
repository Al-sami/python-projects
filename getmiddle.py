def get_middle(s):
    letters = ""
    lenStr = len(s)
    if lenStr % 2 == 0:
        num1 = int((lenStr / 2) -1)
        num2 = int((lenStr/2))
        letters = s[num1] + s[num2]
        return letters
    else:
        index = int((lenStr - 1) / 2)
        letters = s[index]
        return letters

print(get_middle("eshal"))