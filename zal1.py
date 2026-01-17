def sherlockAndAnagrams(s):

    if len(s)<2 or len(s)>100 : return -1

    for i in s:
        if i <'a' or i >'z' : return -2

    letters = list(s)
    substr = []

    for i in range(len(letters)):

        substr.append([letters[i]])
        x = [letters[i]]

        for j in range(i + 1, len(letters)):
            x.append(letters[j])
            y=x.copy()
            substr.append(y)

    for i in substr:
        i.sort()

    count = 0
    a = substr.copy()

    for i in range(len(substr) - len(letters)):
        b = a.pop()
        for j in a:
            if j == b : count += 1

    return count

s = input()
print(sherlockAndAnagrams(s))
