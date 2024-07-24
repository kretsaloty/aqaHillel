alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——(" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)  # task 03

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402  # Площа Чорного моря
azov_sea_area = 37800    # Площа Азовського моря

total_area = black_sea_area + azov_sea_area  # Загальна площа

print("Загальна площа Чорного та Азовського морів становить", total_area, "км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375291  # Загальна кіл-ть продуктів

third_supermarket = total_products - 250449  # Кіл-ть проуктів в треньому супермаркеті
first_supermarket = total_products - 222950  # Кіл-ть проуктів в другому супермаркеті
second_supermarket = total_products - third_supermarket - first_supermarket  # Кіл-ть проуктів в першому супермаркеті

print('В першому супермаркеті знаходиться', first_supermarket, 'товару\n'
      'В другому супермаркеті знаходиться', second_supermarket, 'товару\n'
      'В третьому супермаркеті знаходиться', third_supermarket, 'товару')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

suma_platy = 1179  # Ціна грн/місяць
suma_months = 18   # Кіл-ть місяців до сплати
suma_computer = suma_months * suma_platy  # Сумма комп'ютера

print("Сумма комп'ютера складає", suma_computer, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
tuple = (8019 % 8, 9907 % 9, 2789 % 5, 7248 % 6, 7128 % 5, 19224 % 9)

print(tuple[0:6])

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

suma_tovaru = pizza_big + pizza_medium + juice + cake + water

print('Ірині необхідно', suma_tovaru, 'грн для данного замовлення')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
odna_storinka = 8

suma_storinok = photos // odna_storinka

if photos % odna_storinka != 0:  # Якщо кількість сторінок не дорівнює цілому числу, додаємо одну сторінку щоб влізли всі фото
    suma_storinok += 1

print('Небхідно',suma_storinok, 'сторінок, щоб вклеїти всі фото')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
zapas_benzyna_100km = 9
zapas_baka = 48

kilkisty_benzyna = (distance // 100) * zapas_benzyna_100km
print(f"Необхідна кількість бензину: {kilkisty_benzyna} літрів")

kilkisty_zapravok = kilkisty_benzyna // zapas_baka
print(f"Кількість заправок: {kilkisty_zapravok}")