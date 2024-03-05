from pyspark import SparkContext
import time

def top_word_occurrences(file_path):
    start_time = time.time()
    sc = SparkContext.getOrCreate()
    
    # Reading the text file into an RDD
    text_file = sc.textFile(file_path)
    
    # Splitting the text into words and counting each word's occurrences
    word_counts = text_file.flatMap(lambda line: line.split(" ")) \
                           .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda a, b: a + b)
    
    # Sorting the words by their count in descending order and taking the top 10
    top_words = word_counts.sortBy(lambda word_count: word_count[1], ascending=False).take(10)
    
    sc.stop()
    end_time = time.time()
    
    # Printing the top 10 words and their counts
    for word, count in top_words:
        print(f"{word}: {count}")

    print(f"Execution time: {end_time - start_time:.4f} seconds")

# Replace 'your_file_path.txt' with the path to the text file you want to analyze.
top_word_occurrences('hdfs://192.168.1.31:8020/lorem_ipsum_1000_lines_fr.txt')
