import pandas as pd


class DesignerDataProcessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.data_about_designers = {
            "www": 0, "van": 0, "uuu": 0, "mmm": 0, "ccc": 0, "mvm": 0,
            "ddd": 0, "bas": 0, "aga": 0, "apa": 0, "deb": 0, "lll": 0,
            "eee": 0, "kkk": 0, "ooo": 0, "ppp": 0, "m": 0, "pv": 0,
            "rrr": 0, "rpr": 0, "vaa": 0, "e": 0, "yyy": 0
        }

    def collect_data(self, choose_index):
        choose = ["Заказали, шт", "Доля карточки в выручке"]
        for index, row in self.dataframe.iterrows():
            article = row["Артикул продавца"]
            quantity = row[choose[choose_index]]

            temp = article.split(sep="-")
            for part in temp:
                key = part.lower()
                if key in self.data_about_designers:
                    self.data_about_designers[key] += quantity

        # Округление данных
        for part in self.data_about_designers:
            self.data_about_designers[part] = round(self.data_about_designers[part], 2)

    def get_results(self):
        return self.data_about_designers


class TotalProfit:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_results(self):
        total = 0
        for index, row in self.dataframe.iterrows():
            total += int(row["Выкупили на сумму, руб"])
        return total




df = pd.read_excel("данные.xlsx", sheet_name="Товары")
# Использование класса
if __name__ == "__main__":
    # choose_from_site = int(
    #     input("Представим что это кнопки на сайте (1 - сколько заказали от дизайнера, 2 - его доля в выручке): ")) - 1
    #
    # processor = DesignerDataProcessor(df)
    # processor.collect_data(choose_from_site)
    # results = processor.get_results()
    # print(results)
    tp = TotalProfit(df)
    print(tp.get_results())
