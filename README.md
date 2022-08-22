# Файловый менеджер для Windows

Программа распределяет файлы по папкам по их типу.

## Установка

Для запуска понадобится `Python 3`. Если у вас он не установлен, воспользуйтесь [статьей по его установке]("https://docs.microsoft.com/ru-ru/windows/python/beginners#install-python").
Затем скачайте форк репозитория себе на компьютер.
Никакие сторонние библиотеки и заваисимости устанавливать не нужно.

## Запуск

Поместите файл `main.py` рядом с папкой, которую нужно почистить (из которой брать файлы).
Перейдите в командную строку. Вам поможет пункт `Запуск командной строки в Проводнике` [статьи по командной строке]("https://wp-seven.ru/instruktsii/tips/windows-10-tips/komandnaya-stroka-v-windows-10.html#:~:text=В%20Windows%2010%201607%20Anniversary,затем%20на%20Открыть%20командную%20строку"). Затем используйте следующую команду для запуска с аргументом `--original_dir`. В нем укажите, какую папку нужно почистить.

```python
python main.py --original_dir <папка>
```

Вы увидите сообщение об успешном окончании работы программы.

## Цель проекта

Респределить набитые в кучу файлы по типу.

## Автор

George Salt: [Вконтакте]("https://vk.com/george_salt"), [YouTube]("https://www.youtube.com/channel/UCwKOJwwsnmZeo5xSLgx5HgA").