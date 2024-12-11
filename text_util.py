reset = "\x1b[0m"
normal_bright = '\x1b[2m'
bright = "\x1b[1m"
dim = "\x1b[2m"
underscore = "\x1b[4m"
blink = "\x1b[5m"
reverse = "\x1b[7m"
hidden = "\x1b[8m"

black = "\x1b[30m"
red = "\x1b[31m"
green = "\x1b[32m"
yellow = "\x1b[33m"
blue = "\x1b[34m"
magenta = "\x1b[35m"
cyan = "\x1b[36m"
white = "\x1b[38m"

BGblack = "\x1b[40m"
BGred = "\x1b[41m"
BGgreen = "\x1b[42m"
BGyellow = "\x1b[43m"
BGblue = "\x1b[44m"
BGmagenta = "\x1b[45m"
BGcyan = "\x1b[46m"
BGwhite = "\x1b[47m"

italic = '\x1B[3m'
normal = '\x1B[23m'

def red_text(text):
    return f'{red}{text}{white}'

def green_text(text):
    return f'{bright}{green}{text}{white}{normal_bright}'

def italic_text(string):
    return f'{italic}{string}{normal}'

is_red = True
def christmas_text(text):
    global is_red
    letters = []
    for letter in text:
        letters.append(f'{red if is_red else green}{letter}')
        is_red = not is_red
    red_green_text = ''.join(letters)
    return f'{red_green_text}{white}'
