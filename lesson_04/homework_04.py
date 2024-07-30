import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_abzac = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_krapky = adwentures_abzac.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_probylu = re.sub(r'\s+', ' ', adwentures_krapky)
adwentures_kinci = adwentures_probylu.strip()
print(adwentures_kinci)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count('h')
print(f"The 'h' letter appears: {count_h} times")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

adwentures_splited = adwentures_of_tom_sawer.split()
counter = 0
for capital_word in adwentures_splited:
    if capital_word[0].isupper():
        counter += 1

print(f"Amount of words what starts with capital letter is: {counter}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

word_to_find = "Tom"
count = 0

for index, word_tom in enumerate(adwentures_splited):
    if word_tom == word_to_find:
        count += 1
        if count == 2:
            print(f"The word '{word_to_find}' appears the second time at position: {index}")
            break

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_kinci.split('. ')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

# if adwentures_of_tom_sawer.startswith("By the time"):
#     print("The line starts with 'By the time'")
# else:
#     print("There is no line what starts with 'By the time'")

found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        found = True
        break

if found:
    print("There is a sentence what starts with: 'By the time'")
else:
    print("There is NO sentence what starts with: 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
count_last = len(last_sentence.split())
print(f"Amount of words in last sentence is: {count_last}")
