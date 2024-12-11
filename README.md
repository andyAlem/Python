# Виджет банковских операций клиента
## Описание проекта
Программа для фильтрации и сортировки банковских счетов по дате и оплате.

## Инструкция по установке
Установить зависимости:
pip install -r requirements.txt


## Автор работы над заданием:
Осипов Андрей Вячеславович

## Примеры использования функций
### filter_by_state 

В модуле processing реализована функция filter_by_state, которая принимает список словарей и опционально значение для ключа state
(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.

### filter_by_currency 

В модуле generator создана функция, которая принимает список словарей
и возвращает итератор

## Декоратор Log 
Добавлен Генератор Log для логирования выполнения функций

## Добавлен модуль с обращением к внешнему API

## Тестирование 
Проведено тестирование трех модулей:
masks, processing, widget

Тестовые функции находятся в Пакете "tests". Тестирование
проведено с при помощи фрэймворка pytest. 

Добавлены тесты для нового модуля generators.py

Добавлены тесты для нового декоратора. 

Добавлено тестирование для модулей utils, external_api


## Контакт для связи с командой разработки:
andrej.osipov@outlook.com
## Источник
[Программа создана при поддержке онлайн-школы] (skypro@skyeng.ru) 
