text = 'Зимбабвийский абвер самозабвенно предавал забвению сабвуфер'
list_text = text.split(' ')
print(f'Исходный текст: {text}')
new_text = []
for word in list_text:
    if 'абв' not in word:
        new_text.append(word)
print(f'Итоговый текст: {" ".join(new_text)}')