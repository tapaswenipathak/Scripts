import re

file_read = open("Phase1.txt", "r")
file_write = open("Permalinks.txt", "w")

for line in file_read:
    line = line.lower()
    line = re.sub('  ', ' ', line)
    line = re.sub(' ', '-', line)
    line = re.sub('-to-', '-', line)
    line = re.sub('-the-', '-', line)
    line = re.sub('-for-', '-', line)
    line = re.sub('-in-', '-', line)
    line = re.sub('-using-', '-', line)
    line = re.sub('-is-', '-', line)
    line = re.sub('-a-', '-', line)
    line = re.sub('-by-', '-', line)
    line = re.sub('-with-', '-', line)
    line = re.sub('-of-', '-', line)
    line = re.sub('-an-', '-', line)
    line = re.sub('c\+\+', 'cplusplus', line)
    line = re.sub('--', '-', line)
    file_write.write(line)


file_read.close()
file_write.close()
