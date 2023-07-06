def comp(array1, array2):
    if array1 and array2 is not None:
        size = len(array1)
        res = ""
        if array1[0] == array2[0]:
            for i in range(1, size):
                if array2[i] == array1[i-1] * array1[i-1]:
                    res = True
                    continue
                else:
                    res = False
                    break
            return res

        else:
            return False
    else:
        return False


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
