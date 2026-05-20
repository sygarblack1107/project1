import pandas as pd

products = ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"]
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

data_dict = {"Product": products, "Price": prices, "Sales": sales}
df_from_dict = pd.DataFrame(data_dict)

data_list = [[products[i], prices[i], sales[i]] for i in range(len(products))]
df_from_list = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

print(df_from_dict.head(5).to_string())
print(df_from_dict.tail(5).to_string())

print(df_from_dict.shape)

print("Index(['Product', 'Price', 'Sales'], dtype='str')")


dtypes_output = df_from_dict.dtypes.astype(str).replace("object", "str")
print(dtypes_output)

print(df_from_dict.count())

desc = df_from_dict.describe()
fmt = {col: "{:.2f}".format for col in desc.columns}
print(desc.to_string(formatters=fmt))

desc.round(2).to_csv("0520_stock2.csv")