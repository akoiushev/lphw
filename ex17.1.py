from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Можете следующие две строки разместить в одну? 
#in_file = open(from_file)
#indata = in_file.read()
# short code
in_file = open(from_file).read()

print(f"Исходный файл имеет размер {len(in_file)} байт")

out_file = open(in_file, "w")
out_file.write(in_file)

out_file.close()
