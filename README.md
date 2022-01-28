# Bitly url shorterer

The program uses the Bitly service API and can create short links from regular URLs and show the number of clicks on the so-called. "Beatlinks" - ready-made short links.

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Register on Bitly.com

To work, you need to register on the site [bitly.com](https://app.bitly.com/) and generate a token.
Bitly documentation [link](https://dev.bitly.com/get_started.html).
How to generate a token [described here](https://app.bitly.com/settings/apps/).

### Create a file with environment variables

Since your token should be kept private, you need to create a ".env" file in your main.py folder.
This file will contain sensitive information known only to you.
The line with the generated token must be inserted into the ".env" file as follows:
```
BITLY_TOKEN="{TOKEN}"
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

# Обрезка ссылок с помощью Битли

Программа использует API сервиса Bitly и умеет создавать короткие ссылки из обычных URL и показывать количество кликов 
по т.н. "Битлинкам" - готовым коротким ссылкам.

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Регистрация на сайте Bitly.com

Для работы необходимо зарегистрироваться на сайте [bitly.com](https://app.bitly.com/) и сгенерировать токен.
Документация bitly [по ссылке](https://dev.bitly.com/get_started.html).
Как сгенерировать токен [описано здесь](https://app.bitly.com/settings/apps/).

### Создание файла с переменными окружения

Так как ваш токен следует хранить приватно, необходимо создать файл ".env" в папке с main.py. 
Этот файл будет содержать чувствительную информацию, известную только вам.
Строчку с сгенерированным токеном нужно вставить в файл ".env" следующим образом:

```
BITLY_TOKEN="{TOKEN}"
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
