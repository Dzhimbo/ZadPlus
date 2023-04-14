from functools import reduce

news = [
    "5 Курс биткоина вырос до 1000 долларов.",
    "10 В новогоднюю ночь выйдет новая первая серия нового сезона \"Шерлока\".",
    "10 Где-то далеко идут дожди.",
    "7 В Новосибирске из автобуса сбежала кондуктор.",
    "1 Самолет «Почты России» вылетел с опозданием в несколько месяцев.",
    "20 Козёл Тимур подружился с тигром Амуром.",
    "10 Инженерам из Space X удалось посадить первую ступень ракеты на землю.",
    "20 Самолёты сбиваются с пути.",
    "21 Просто не дай ему уйти."
]


def filter_positive_news(acc, item):
    positivity, news_text = int(item.split(" ")[0]), " ".join(item.split(" ")[1:])
    if not acc or positivity > acc[-1][0]:
        acc.append((positivity, news_text))
    return acc


result = reduce(filter_positive_news, news, [])

for positivity, news_text in result:
    print(f"{positivity} - {news_text}")