import string

def max_length(str):
    splitted_str = str.split( )
    max = 0
    for word in splitted_str:
        print(word)
        count = 0
        for let in word:
            if let in string.ascii_letters:
                count += 1
        if (count == len(word)) and (max < count):
            max = count
        else:
            count = 0
            for let in word:
                if let in string.ascii_letters:
                    count +=1
                else:
                    pass
            if max < count:
                max = count
    return max


print(max_length("pr#@$#@$@#$ivet, kak de####%#!!%!#%#%###la"))