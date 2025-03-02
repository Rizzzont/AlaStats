import pandas as pd

df = pd.read_excel("данные.xlsx", sheet_name="Товары")

print("Welcome to the AlaStats")
df.drop(columns=["Артикул WB", "Удаленный товар", "Доля карточки в выручке",
                 "Доля карточки в выручке (предыдущий период)", "Переходы в карточку"])

print("Hello, World!")
print(df)