from string import ascii_letters


"""
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    amir, 3 => dplu
    amir, 4 => eqmv
    amir_bigZ
    
    55 % 52 = 3
"""

def encrypt(data, step):
    alpha = ascii_letters
    result = ''

    for character in data:
        if character not in alpha:
            result += character
        else:
            new_key = (alpha.index(character) + step) % len(alpha)
            result += alpha[new_key]

    return result

def decrypt(data, step):
    step *= -1
    return encrypt(data, step)

def brute_force(data):
    alpha = ascii_letters
    brute_force_data = {}

    for step in range(1, len(alpha)+1):
        brute_force_data[step] = decrypt(data, step)

    return brute_force_data
