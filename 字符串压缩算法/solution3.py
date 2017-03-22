# -*- coding:utf-8 -*-
def check(string):
    if not string:
        return 0
    if len(string) >= 100:
        print("string too long")
        quit()
    size = 2
    current = string[0]
    count = 1
    for ch in string[1:]:
        if ch != current:
            size += 2
            current = ch
            count = 1
        if ch == current:
            count += 1
            if count >= 10:
                size += 1
    print(size)
    return size


def compress_str(string):
    if check(string) >= len(string):
        print(string)
        return
    result = []
    count = 1
    current = string[0]

    for ch in string[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current)
            result.append(str(count))
            count = 1
            current = ch
    result.append(current)
    result.append(str(count))
    print(''.join(result))
    return

if __name__ == "__main__":
    processstring = input("Input string:\n")
    compress_str(processstring)
