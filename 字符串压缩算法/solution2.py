# -*- coding:utf-8 -*-
def compress_str(string):
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

    if len(result) >= len(string):
        print(string)
    print(''.join(result))

if __name__ == "__main__":
    processstring = input("Input string:\n")
    compress_str(processstring)