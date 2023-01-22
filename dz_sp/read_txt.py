
def read_txt():
    file = open("file.txt")
    print('\nТелефонный справочник:\n' + file.read() )
    

def read_txt_sorted():
   lines = open("file.txt", 'r').readlines()
   output = open("file_id_sorted.txt", 'w')
   for line in sorted(lines, key=lambda line: line.split()[0]):
    output.write(line)
   output.close()

def read_txt_id():
    file = open("file_id_sorted.txt")
    print('Отсортированный список по ID:\n' + file.read() )   