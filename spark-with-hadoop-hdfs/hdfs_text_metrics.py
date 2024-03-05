from pyspark import SparkContext
import time

def text_file_metrics_spark(file_path):
    start_time = time.time()

    sc = SparkContext.getOrCreate()
    text_file = sc.textFile(file_path)

    line_count = text_file.count()
    word_count = text_file.flatMap(lambda line: line.split(" ")).count()
    character_count_including_spaces = text_file.map(lambda line: len(line)).reduce(lambda a, b: a + b)
    character_count_excluding_spaces = text_file.flatMap(lambda line: line.replace(" ", "")).map(lambda line: len(line)).reduce(lambda a, b: a + b)

    sc.stop()

    end_time = time.time()

    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters (including spaces): {character_count_including_spaces}")
    print(f"Number of characters (excluding spaces): {character_count_excluding_spaces}")
    print(f"Execution time: {end_time - start_time:.4f} seconds")

# Replace 'your_file_path.txt' with the path to the text file you want to analyze.
text_file_metrics_spark("hdfs://192.168.1.31:8020/lorem_ipsum_10m_lines.txt")
