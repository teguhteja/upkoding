message = 'dyvayv9 f6b dr5a a6 b5t6cv9 ayv 0vt9va0 6w ayv b5zcv90v, 69 f6b 1b0a dr5a a6 7b90bv r tr9vv9 z5 ayv ih0a tv5ab9f, sr0zt t647bav9 796x9r44z5x z0 r5 v00v5azr3 02z33 a6 3vr95 - 0av7yv5 yrd2z5x' #encrypted message
LETTERS = 'abcdefghijklmnopqrstuvwxyz1234567890'
# decrypt = 'whether you want to uncover the secrets of the universe, or you just want to pursue a career in the 21st century, basic computer programming is an essential skill to learn - stephen hawking'
# key = 17

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol
    print('Hacking key #%s: %s' % (key, translated))
