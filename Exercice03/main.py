words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

def get_vowels_number(word) :
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']
    vowels_number = 0
    for letter in word :
        if letter in vowels :
            vowels_number += 1    
    return vowels_number

result = [(word, get_vowels_number(word)) for word in words]
print(result)