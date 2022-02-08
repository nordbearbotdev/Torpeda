<h1 align="center">💣 Torpeda Bomber для Termux 💣 </h1> 
<div align="center">
<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> <img src="https://svgshare.com/i/ZhY.svg"> <img src="https://img.shields.io/github/forks/nordbearbotdev/Torpeda?style=social&label=Fork&maxAge=2592000"> <img src="https://img.shields.io/github/stars/nordbearbotdev/Torpeda?style=social&label=Star&maxAge=2592000"> <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"> 
</div>
<h2 align="center">😈 Follow 😈 </h2>
<p align="center">
<a href="https://t.me/HackSploiitt"><img title="Telegram" src="https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=Telegram"></a>
</p>

![test3](https://user-images.githubusercontent.com/85753549/152636631-18d2dc9a-fda8-4558-a190-a57fbb69750e.png)

# Содержание

* [📒 Сайт](https://github.com/nordbearbotdev/Torpeda/blob/main/README.md#%D1%81%D0%B0%D0%B9%D1%82)
* [📌 Wiki](https://github.com/nordbearbotdev/Torpeda/blob/main/README.md#wiki)
* [📥 Установка]()
* [Windows]()
* [Linux]()
* [Termux](https://github.com/nordbearbotdev/Torpeda#--termux)
* [❓Q&A](https://github.com/nordbearbotdev/Torpeda/blob/main/README.md#-как-использовать-прокси)

# 📒 Сайт
Офицальный [сайт](nordbearbotdev.github.io/torpeda/) Torpeda

# 📌 Wiki
Вы можете помочь новичкам написав или поправив статьи о использовании [Torpeda](https://github.com/nordbearbotdev/Torpeda) в офицальной [Wiki](https://github.com/nordbearbotdev/Torpeda/wiki)

# 📥 Установка

<h2>Windows</h2> <img src="https://cdn.iconscout.com/icon/free/png-256/windows-221-1175066.png" width="50" height="50">  

  - Установите Python 3.8 [Скачать](https://www.python.org/downloads/release/python-38)
  - Откроется установщик и нажмите на кнопку: `add python to PATH`
  - Скачайте архив Torpeda <a href="https://github.com/nordbearbotdev/Torpeda/archive/refs/heads/main.zip" target="blank">Скачать</a>
  - Откройте cmd или PowerShell с Torped(a)
  - Введите команду: `pip install -r requirements.txt`  

<h2> 🐧 Linux</h2>

```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/nordbearbotdev/Torpeda
cd Torpeda
pip3 install -r requirements.txt or python -m pip install -r requirements.txt
python3 main.py
```

<h2> 🐧 Termux</h2><img src="https://brandslogos.com/wp-content/uploads/images/large/terminal-logo.png" width="50" height="50">  

```
apt update
apt upgrade
git clone https://github.com/nordbearbotdev/Torpeda
cd Torpeda
pip3 install -r requirements.txt
python3 main.py
```

## ❓ Как использовать прокси?
Основная команда чтоб использовать прокси.

```python
proxies = {
 "http": "http://10.10.10.10:8000",
 "https": "http://10.10.10.10:8000",
}
```
