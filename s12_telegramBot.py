import telegram
import s10_getStockPrice as getStockPrice

# 본인의 토큰주소를 입력하시오
MY_TOKEN = '1918143090:AAFLkKc_jA8SX9Fnlsgd_w3eFf9g5CBVyPQ'
bot = telegram.Bot(MY_TOKEN)

# 본인의 채팅 아이디를 넣어주세요
MY_ID = 1624404774
stocks = getStockPrice.setPrice(getStockPrice.stocks)
print(stocks)

text_lst = []
for _key, _value in stocks.items():
    _price = _value['price']
    text_lst.append(f'{_key} 현재가: {_price}')
# print(text_lst)
_text4tele = '\n'.join(text_lst)
bot.send_message(chat_id=MY_ID, text=_text4tele)


# 참고) 이 코드로 id 얻어올 수도 있음
# MY_ID=bot.getUpdates()[0].message.chat.id
