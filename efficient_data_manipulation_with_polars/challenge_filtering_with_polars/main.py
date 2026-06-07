import polars as pl

def filter_above_threshold(df, column, threshold):
    googol = df.filter(pl.col(column) > threshold)
    return googol

data = {
    "customer_id": [101, 102, 103, 104, 105],
    "purchase_amount": [120.5, 99.9, 200.0, 75.0, 305.5]
}
df = pl.DataFrame(data)

result = filter_above_threshold(df, "purchase_amount", 100.0)
print(result)