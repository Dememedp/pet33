def count_letters(str):
    lenlen = len(str)
    i = 0
    dict = {}
    while i < lenlen:
        dict[str[i]] = i + 1
        i += 1
    return dict

print(count_letters("stringsample"))