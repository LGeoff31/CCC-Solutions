long_text = input()
cyclic_word = input()

qualified = False

def all_cyclic(word):
    lst = [word]
    changed_word = word
    while True:
        b = changed_word[0]
        changed_word = changed_word[1:] + b
        if changed_word == word:
            break
        lst.append(changed_word)
    return lst
for char in all_cyclic(cyclic_word):
    if char in long_text:
        qualified = True
        break

if qualified: print("yes")
else: print("no")