def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) < 123:
            print("{}".format(chr(ord(c) - 32)), end='')

        else:
            print("{}".format(c), end='')
    print("")
