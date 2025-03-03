import pandas as pd

df = pd.read_excel("данные.xlsx", sheet_name="Товары")

data_about_designers = {"www": 0, "van": 0, "uuu": 0, "mmm": 0, "ccc": 0, "mvm": 0, "ddd": 0, "bas": 0, "aga": 0,
                        "apa": 0, "deb": 0, "lll": 0, "eee": 0, "kkk": 0, "ooo": 0, "ppp": 0, "m": 0, "pv": 0, "rrr": 0,
                        "rpr": 0, "vaa": 0, "e": 0, "yyy": 0}

choose = ["Заказали, шт", "Доля карточки в выручке"]

choose_from_site = int(input("Представим что это кнопки на сайте ( 1 - сколько заказали от дизайнера,"
                             "2 - его доля в выручке): ")) - 1

for index, row in df.iterrows():
    article = row["Артикул продавца"]
    quantity = row[choose[choose_from_site]]

    temp = article.split(sep="-")
    for part in temp:
        key = part.lower()
        if key in data_about_designers:
            data_about_designers[key] += quantity

    for part in data_about_designers:
        data_about_designers[part] = round(data_about_designers[part], 2)
print(data_about_designers)