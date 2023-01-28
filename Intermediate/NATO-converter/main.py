import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word to convert: ").upper()
converted_word = [nato_dict[letter] for letter in word]
print(converted_word)
