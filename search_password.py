import time
import datetime;

search_words = "Configuration"
file = open("system.log", "r")
read_data = file.read()
word_count = read_data.count(search_words)
word_count = str(word_count)
print(word_count)

f = open("my_count_file", "a")
f.write(word_count)
f.write("errors")
my_time = str(datetime.datetime.now())
f.write(my_time)
f.write("\n ")
f.close()