file = open("text.txt")
data = file.read()
words = data.split()

print('Кількість слів у текстовому файлі:', len(words))

