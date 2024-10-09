def main():
    words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'é', 'à', 'è', 'ù', 'â', 'ê', 'î', 'ô', 'û'}
    list_of_word_vowel = [(word, len([i for i in word.lower() if i in vowels])) for word in words]
    print(list_of_word_vowel)

    # correction
    list_tuples = [(word, sum(1 for letter in word if letter in 'aeiouAEIOU')) for word in words]
    print(list_tuples)


if __name__ == '__main__':
    main()
