from multiprocessing import Pool
import time

def analyze_data(data_chunk):
    print(f"Processing chunk: {data_chunk}")
    time.sleep(2)  # Simulate a time-consuming analysis
    return f"chunk {data_chunk} analyzed"

if __name__ == "__main__":
    data_chunks = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:
        results = pool.map(analyze_data, data_chunks)
    print("Analysis Results:")
    for result in results:
        print(result)
    print("All data chunks have been processed.")
    

