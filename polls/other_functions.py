import string, random


def random_slug():
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(5))