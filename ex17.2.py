from sys import argv;
from os.path import exists; script, from_file, to_file = argv; in_file = open(from_file).read(); print(f"Исходный файл имеет размер {len(in_file)} байт"); out_file = open(in_file, "w"); out_file.write(in_file); out_file.close();
