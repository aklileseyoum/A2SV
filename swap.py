def swap_case(s):
    outp = ""
    for i in s:
        if i.islower():
            outp += i.upper()
        else:
            outp += i.lower()
    return outp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
