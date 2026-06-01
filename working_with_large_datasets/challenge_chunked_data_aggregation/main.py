import pandas as pd

url = "https://content-media-cdn.codefinity.com/b8f3c268-0e60-4ff0-a3ea-f145595033d8/section1/large_file.csv"


def sum_column_in_chunks(file_path, column_name, chunk_size):
    total = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        if column_name in chunk.columns:
            total += chunk[column_name].sum()
    return total
    #print(total)
        
result = 0        
result += sum_column_in_chunks(url, "Variable value", 100)

print(result)


