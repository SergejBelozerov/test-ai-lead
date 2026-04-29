import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

if not N8N_WEBHOOK_URL:
    raise RuntimeError("N8N_WEBHOOK_URL is missing in .env")

leads = [
    {
    "name": "Sergey",
    "company": "Private Buyer",
    "message": "Хочу купить оригинальную синюю Labubu, готов оплатить сегодня"
  },
  {
    "name": "Anna",
    "company": "Toy Collectors",
    "message": "Нужна оригинальная Labubu большого размера, желательно красного цвета"
  },
  {
    "name": "Maksym",
    "company": "Unknown",
    "message": "Куплю оригинал Labubu, интересует наличие, цена и доставка"
  },
  {
    "name": "Olena",
    "company": "Gift Shop",
    "message": "Хочу заказать 2 оригинальные Labubu разных цветов для подарка"
  },
  {
    "name": "Ivan",
    "company": "Private Buyer",
    "message": "Ищу оригинальную Labubu маленького размера, готов забрать сегодня"
  },
  {
    "name": "Victoria",
    "company": "Collector Club",
    "message": "Куплю оригинальную Labubu в коробке, цвет не важен, главное оригинал"
  },
  {
    "name": "Yaroslav",
    "company": "Unknown",
    "message": "Нужна оригинальная зелёная Labubu, напишите цену и как оплатить"
  },

  # 4–8: средние / неоднозначные лиды
  {
    "name": "Dmitry",
    "company": "Unknown",
    "message": "Куплю игрушку для ребёнка, что есть?"
  },
  {
    "name": "Kateryna",
    "company": "Unknown",
    "message": "Есть Labubu синего цвета?"
  },
  {
    "name": "Oleg",
    "company": "Unknown",
    "message": "Сколько стоит Labubu?"
  },
  {
    "name": "Nina",
    "company": "Unknown",
    "message": "Чем оригинальная Labubu отличается от копии?"
  },
  {
    "name": "Artem",
    "company": "Unknown",
    "message": "Хочу Labubu, но пока думаю какой цвет выбрать"
  },
  {
    "name": "Maria",
    "company": "Gift Market",
    "message": "Интересует Labubu для подарка, можете показать варианты?"
  },
  {
    "name": "Vlad",
    "company": "Unknown",
    "message": "Есть недорогая Labubu или похожая игрушка?"
  },
  {
    "name": "Yulia",
    "company": "Unknown",
    "message": "Покажите какие Labubu сейчас есть в наличии"
  },
  {
    "name": "Roman",
    "company": "Unknown",
    "message": "Мне нужна мягкая игрушка, возможно Labubu, но я ещё не уверен"
  },
  {
    "name": "Sofia",
    "company": "Unknown",
    "message": "Ищу подарок девочке, слышала про Labubu, что можете предложить?"
  },
  {
    "name": "Tanya",
    "company": "Unknown",
    "message": "Есть Labubu дешевле оригинала?"
  },
  {
    "name": "Kirill",
    "company": "Unknown",
    "message": "Какие цвета Labubu бывают и какая самая популярная?"
  },

  # 1–3: слабые / нерелевантные / продукты / электротехника
  {
    "name": "Alex",
    "company": "Grocery Buyer",
    "message": "Хочу купить кофе, сахар и молоко, есть доставка?"
  },
  {
    "name": "Bogdan",
    "company": "Unknown",
    "message": "Нужна микроволновка недорогая, какие модели есть?"
  },
  {
    "name": "Ira",
    "company": "Unknown",
    "message": "Вы продаёте телефоны Samsung?"
  },
  {
    "name": "Pavel",
    "company": "Home Electronics",
    "message": "Интересует электрочайник и тостер для кухни"
  },
  {
    "name": "Denis",
    "company": "Unknown",
    "message": "Есть скидки на рис, макароны и подсолнечное масло?"
  },
  {
    "name": "Marta",
    "company": "Unknown",
    "message": "Нужен новый фен или плойка, что можете посоветовать?"
  }
]

for lead in leads:
    response = requests.post(N8N_WEBHOOK_URL, json=lead, timeout=30)
    print(f"{lead['name']}: {response.status_code} - {response.text}")
    time.sleep(12)