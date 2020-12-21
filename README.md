![Баннер](https://i.ibb.co/fXDPf45/Frame-97.png)  

![Technology](https://img.shields.io/badge/svelte-svelte--v3-orange) ![Technology](https://img.shields.io/badge/python-3.7-blue) ![Forks](https://img.shields.io/github/forks/common-data-team/common-data-app?style=social)

# 🗒 Содержание

* [О проекте](https://github.com/Common-Data-Team/common-data-app#-%D0%BE-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B5)
* [Текущий функционал платформы](https://github.com/Common-Data-Team/common-data-app#%EF%B8%8F-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B9-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB-%D0%BF%D0%BB%D0%B0%D1%82%D1%84%D0%BE%D1%80%D0%BC%D1%8B)
* [Will be soon](https://github.com/Common-Data-Team/common-data-app#-will-be-soon)
* [Get started](https://github.com/Common-Data-Team/common-data-app#-get-started)
* [Запуск с помощью докера](https://github.com/Common-Data-Team/common-data-app#-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D0%B4%D0%BE%D0%BA%D0%B5%D1%80%D0%B0)

# 🤓 О проекте

**[Common data](https://commondata.ru/)** — веб-платформа краудсорсинга данных для проектов и исследований.  
Основной целью платформы является популяризация и развитие ***движения донорства данных (data donation)**** за счет снижения рисков связанных с безопасностью доноров. 

****Донорство данных — добровольная передача человеком своих данных для коллективного использования и исследований.***

# ⚙️ Текущий функционал платформы 

* Возможность выбора и просмотра интересующих проектов 
* Функционал донорства данных в интересующие проекты 
* Возможность создания своего проекта и формы сбора данных
* Функционал сбора данных в рамках проекта 
* Отслеживания личного прогресса в донорстве данных на платформе
* Отслеживания прогресса проекта в сборе данных на платформе 
* Markdown для проектов

# ⏰ Will be soon
   :white_check_mark: Возможность публикации новостей о проекте
   :white_check_mark: Возможность загрузить изображение проекта и профиля
   :white_check_mark: Функционал отслеживания новостей донором  
   :white_check_mark: Возможность отслеживания интересующих проектов  
   :white_check_mark: Функционал выгрузки собранных данных  
   :white_check_mark: Геймификация процесса сбора данных  
   :white_check_mark: Отслеживание процесса заполнения формы в процентах
   :white_check_mark: Возможность удаления и архивирования проекта 
   :white_check_mark: Модерация анкет сбора данных с примением алгоритмов машинного обучения  

## 🚀 Get started

Установите зависимости

```bash
npm install
```
Запустите проект 

```bash
npm run dev
```

## 🐳 Запуск с помощью докера

Соберите образ
```bash
docker build -t frontend .
```

Запустите контейнер
```bash
docker run -p 80:80 -d frontend
```
