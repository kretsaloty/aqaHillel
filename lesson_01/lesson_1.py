# task 01 == Виправте синтаксичні помилки

print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки


hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

yabluna = 4
grusha = yabluna + 5
sluva = yabluna - 2
sum_derev = yabluna + grusha + sluva
print("В саду посадили всього", sum_derev, "дерев")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

morning_temperature = 5
launch_temperature = morning_temperature - 10
evening_temperature = launch_temperature + 4
print("In the evening the temperature is", evening_temperature, "degrees")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = 24/2
absent_boys = 1
absent_girls = 2
sum_children = (boys + girls) - (absent_boys + absent_girls)
print("Today there are only", sum_children, "children in the theatre group")

# task 10

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
sum_books = first_book + second_book + third_book
print("The sum of all books will be", sum_books, "UAH")