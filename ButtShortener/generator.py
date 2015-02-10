import random

beginnings = [
    'pb',
    'f',
    'ph',
    'bl',
]
middles = [
    'f',
    'b',
    'p',
    'r',
    'a',
    '4'
]
ends = [
    't',
    'p',
    'r',
    'b',
    '7'
]
words = [
    'good',
    'awesome',
    'epic',
    'bootylicious',
    'outtathisworld',
    'amazing',
    'trashy',
    'bubbly'
]


def make_fart_sound():
    output = random.choice(beginnings)
    length = random.randint(3, 10)
    for x in range(length):
        output += random.choice(middles)
    output += random.choice(ends)

    return output


def generate_shortened_url():
    real_word = not bool(random.randint(0, 250))
    if real_word:
        shortcode = random.choice(words)
    else:
        shortcode = make_fart_sound()

    output = ""
    for letter in shortcode:
        uppercase = bool(random.randint(0, 1))
        if uppercase:
            letter = letter.upper()
        output += letter

    return output