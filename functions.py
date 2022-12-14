import random
from tkinter import messagebox


def easter_agg():
    msg = ['В поезде едут 3 юзера и 3 программиста.\
    У юзеров 3 билета, у программистов 1. Заходит контроллер.\
    Юзеры показывают билеты, программисты прячутся в туалет. Контроллер стучится в туалет,\
    оттуда высовывается рука с билетом. Программисты едут дальше.\
    На обратном пути. У юзеров 1 билет, у программистов ни одного. Заходит контроллер.\
    Юзеры прячутся в туалет. Один из программистов стучит, из туалета высовывается рука\
    с билетом. Программисты забирают билет и прячутся в соседний туалет. Юзеров ссаживают с поезда.\
    Вывод — не всякий алгоритм, доступный программисту, доступен юзеру.', 'Программист звонит в библиотеку.\
    — Здравствуйте, Катю можно?\
    — Она в архиве.\
    — Разархивируйте ее пожалуйста. Она мне срочно нужна!', 'Жена посылает мужа-программиста в магазин:\
    - Купи батон колбасы. Да, и спроси, есть ли яйца. Если есть - возьми десяток.\
    Программист приходит в магазин:\
    - Батон колбасы, пожалуйста. Ага, спасибо. А яйца у вас в продаже есть?\
    - Есть.\
    - Тогда, пожалуйста, ещё девять батонов колбасы.', 'Из комбинации лени и логики\
    получаются программисты.', 'Жил-был программист и было у него два сына - Антон \
    и Неантон.', 'Программист залезает в холодильник, достает пачку масла, читает на обертке:\
    Массливочное. 72%. В голове быстрая мысль:\
    - О! Скоро загрузится! Возвращает масло в холодильник. Закрывает дверцу.']
    return messagebox.showinfo('Пасхалка', str(random.choice(msg)))


def all_authors():
    messages = ['Авторы:', 'Антон Федонин', 'Андрей Полянский', 'Татьяна Вальчик',
                'Марина Ноздрачева', 'Александр Новиков', 'Эльмира Нургалеева']
    return messages
