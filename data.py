import pandas as pd

df = pd.read_excel("данные.xlsx", sheet_name="Товары")

df.drop(columns=["Артикул WB", "Удаленный товар", "Доля карточки в выручке",
                 "Доля карточки в выручке (предыдущий период)", "Переходы в карточку"])

print("Hi")
print(df)