from docx.enum.text import WD_ALIGN_PARAGRAPH

SIZE_L, SIZE_W = 450, 625  # размеры окна
READ_ONLY = True  # только чтение

# Все возможные заголовки
TITLE = {'Заголовок': 'Title',
         'Заголовок 1': 'Heading 1',
         'Заголовок 2': 'Heading 2',
         'Заголовок 3': 'Heading 3',
         'Заголовок 4': 'Heading 4'}

# Тут должен быть правильный порядок Заголовков
CORRECTSEQUENCE = {"Содержание": 1,
                   "Введение": 2,
                   "Теоретическая часть": 3,
                   "Принцип работы протоколов http и https": 4,
                   "База данных mongodb": 5}

# Выравнивание параграфов
setter = {
    "по ширине": WD_ALIGN_PARAGRAPH.JUSTIFY, "по левому краю": WD_ALIGN_PARAGRAPH.LEFT,
    "по правому краю": WD_ALIGN_PARAGRAPH.RIGHT, "по центру": WD_ALIGN_PARAGRAPH.CENTER,
    "по умолчанию": WD_ALIGN_PARAGRAPH is None
}