def order_letters(text):
    word = []
    for letter in text:
        if letter != " ":
            word.append(letter.lower())
    word.sort()
    return word


text_one = input("Please, enter first text: ")
text_two = input("Please, enter second text: ")

order_text_one = order_letters(text_one)
order_text_two = order_letters(text_two)

if order_text_one == order_text_two:
    print("Anagrams")
else:
    print("Not Anagrams")
