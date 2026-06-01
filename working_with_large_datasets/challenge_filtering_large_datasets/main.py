import pandas as pd

def filter_large_csv(input_file, output_file, column, threshold, chunk_size=10000):
    first_chunk = True

    # Make sure the file is empty before we start
    open(output_file, 'w').close()

    
    for chunk in pd.read_csv(input_file, chunksize=chunk_size):
        filtered = chunk[chunk[column] > threshold]
        if not filtered.empty:
            filtered.to_csv(output_file,
                            mode='a',           # append aftrer the first write
                            header=first_chunk, # write header only once
                            index=False)
            first_chunk = False
    if first_chunk:
        # no rows matched:  write only header
        pd.read_csv(input_file, nrows=0).to_csv(output_file, index=False)
# Sample calls
input_file = "https://staging-content-media-cdn.codefinity.com/b8f3c268-0e60-4ff0-a3ea-f145595033d8/section1/large_file.csv"

output_file = "filtered_output.csv"
column = "value"
threshold = 100


try:
    filter_large_csv(input_file, output_file, column, threshold)
except Exception as e:
    error_message = str(e)
    print(error_message)
