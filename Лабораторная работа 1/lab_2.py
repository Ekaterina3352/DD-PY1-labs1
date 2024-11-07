# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44    # объем дискеты, мегабайт
pages = 100    # количество страниц в книге
lines = 50    # число строк на странице
symbols = 25    # количество символов в строке
volume_for_symbol = 4    # объем для одного символа, байт

volume *= 1024**2
number_of_characters = (symbols * lines * pages)
number_of_books = (volume / (number_of_characters * volume_for_symbol))

print("Количество книг, помещающихся на дискету:", round(number_of_books))
