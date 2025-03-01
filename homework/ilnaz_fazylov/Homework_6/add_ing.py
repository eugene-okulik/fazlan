def update_text(text):
    lst = text.split()
    result = ''

    for word in lst:
        if '.' in word or ',' in word:
            result = result + word[:-1] + 'ing' + word[-1] + ' '
        else:
            result = result + word + 'ing' + ' '

    return result


print(update_text(
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitaae libero'
)
)
