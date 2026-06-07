import polars as pl

def groupby_mean(df: pl.DataFrame, group_col: str, value_col: str) -> pl.DataFrame:
    categories =  df.group_by(group_col).agg([pl.col(value_col).mean().alias("mean_" + value_col)])
    return categories
    

df = pl.DataFrame({
    "category": ["A", "B", "A", "B", "C", "A"],
    "value": [10, 20, 30, 40, 50, 60]
})

result = groupby_mean(df, "category", "value")
print(result)