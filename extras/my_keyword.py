LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS=LETTERS.lower()

def encryptMessage(key, message):
    key=key.lower()
    message=message.lower()
    fixed_key=''.join([j for i,j in enumerate(key) if j not in key[:i]])
    NEW_LETTERS = fixed_key.upper() + ''.join([a.upper() if (a not in fixed_key) else '' for a in LETTERS])
    new_message=message
    for i in range(len(LETTERS)):
        new_message=new_message.replace(LETTERS[i],NEW_LETTERS[i])
    return new_message.lower()


def decryptMessage(key, message):
    key=key.lower()
    message=message.lower()
    fixed_key=''.join([j for i,j in enumerate(key) if j not in key[:i]])
    NEW_LETTERS = fixed_key + ''.join([a if (a not in fixed_key) else '' for a in LETTERS])
    COPY_LETTERS = LETTERS.upper()
    new_message=message
    for i in range(len(LETTERS)):
        new_message=new_message.replace(NEW_LETTERS[i],COPY_LETTERS[i])
    return new_message.lower()