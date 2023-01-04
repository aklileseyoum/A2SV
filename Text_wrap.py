import textwrap

def wrap(string, max_width):
    if max_width == 0:
        return ""
        
    paragraph = ""
    index = 0
    while index < len(string):
        if index % max_width == 0 and index != 0:
            paragraph += '\n'
        paragraph += string[index]
        index += 1
        
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
