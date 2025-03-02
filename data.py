import pandas as pd

df = pd.read_excel("данные.xlsx", sheet_name="Товары")

print("Hi")
print("Alastats top")
df.drop(columns=["Артикул WB", "Удаленный товар", "Доля карточки в выручке",
                 "Доля карточки в выручке (предыдущий период)", "Переходы в карточку"])

for i in range(5):
    print("Alastats Top")
print("Hello, World!")
print(df)