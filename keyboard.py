from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

interview_kb1 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Осень', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Лето', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Зима', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Весна', callback_data='D'))

interview_kb2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Spa-отель, детокс и релакс', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Пикник: друзья и барбекю', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Море, книга и бокал белого вина', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Камин, плед, кофе и джаз', callback_data='D'))


interview_kb3 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Нахожу плюсы во всем', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Организую какой-то движ', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Ничего – это тоже жизнь', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Рефлексирую', callback_data='D'))

interview_kb4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Шампанское+брускетта', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Кружка кофе+яблоко в дорогу', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Капучино+круассан', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Горячий шоколад+штрудель', callback_data='D'))

interview_kb5 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. На качество и стиль одежды', callback_data='A'),
                                                      InlineKeyboardButton(text='B. На его чувство юмора', callback_data='B'),
                                                      InlineKeyboardButton(text='C. На манеру его общения', callback_data='C'),
                                                      InlineKeyboardButton(text='D. На внешность', callback_data='D'))

interview_kb6 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Вхожу в «облако» духов', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Обливаюсь с ног до головы', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Пару «пшиков» перед выходом', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Капля на запястье', callback_data='D'))

interview_kb7 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Достаточно моего присутствия', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Море шампанского', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Море в шаговой доступности', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Море общения', callback_data='D'))

interview_kb8 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Терпеть не могу быть как все', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Выбираю образ под настроение', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Во всём хорошо соблюдать меру', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Стараюсь следовать тенденциям', callback_data='D'))

interview_kb9 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='A. Выставка и модный ресторан', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Прогулка с подругой', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Поработать над презентацией', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Побыть дома  с любимым', callback_data='D'))

next_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Далее', callback_data='nope'))
davai_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Давай)', callback_data='nope'))
poehali_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Поехали!', callback_data='nope'))
sticker_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Стикерпак', url='https://t.me/addstickers/Bee8March'),
                                                   InlineKeyboardButton(text='Пройти тест еще раз', callback_data='fork'))

fork_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Да', callback_data='true'),
                                                InlineKeyboardButton(text='Нет', callback_data='false'))

