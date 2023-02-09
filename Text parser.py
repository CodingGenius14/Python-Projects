#Text Analyzer

text = input("Enter random text: ")
text = text.lower()
word_list = text.split()
total_words = len(word_list)

print("\n")

random_letters = []

random_letters.append(input("Enter your first letter: ").lower())
random_letters.append(input("Enter your second letter: ").lower())
random_letters.append(input("Enter your third letter: ").lower())
letter_list = list(text.strip())

letter_1_occurence = letter_list.count(random_letters[0])
letter_2_occurence = letter_list.count(random_letters[1])
letter_3_occurence = letter_list.count(random_letters[2])

first_letter = letter_list[0]
last_letter = letter_list[-1]
is_python = 'python' in text
dic = {True: "was", False: "was not"}

print("\n")
print("Random Letters Occurence in Text:")
print(f"{random_letters[0]} appears {letter_1_occurence} times in the text")
print(f"{random_letters[1]} appears {letter_2_occurence} times in the text")
print(f"{random_letters[2]} appears {letter_3_occurence} times in the text")

print("\n")
print("Words in Text:")
print(f"There are {total_words} words in your text")

print("\n")
print("First and Last Letter in Text:")
print(f"'{first_letter}' is the first letter in the text")
print(f"'{last_letter}' is the last letter in the text")

print("\n")
print("Inverted Text:")
word_list.reverse()
inverted_text = " ".join(word_list)
print(f"Your text written backward is '{inverted_text}'")

print("\n")
print(f"The word python {dic[is_python]} found in the text")





