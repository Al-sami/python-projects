def reverse_words(text):
    str = text.split(" ")
    new_str = " "
    length = len(str)
    for i in range(length):
        word = str[i]
        str[i] = word[::-1]
    return new_str.join(str)


reverse_words('The quick brown fox jumps over the lazy dog.')

