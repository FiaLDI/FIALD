# with open('done.txt') as book:
#     lines= book.readlines()
#     for i in lines:
#         print(i.rstrip())

# filename = 'done.txt'
# with open(filename) as book:
#     lines = book.readlines()
#     p_st=''
#     for i in lines:
#         p_st+=i.strip()
#     print(p_st[:3])
#     print(len(p_st))

# filename = 'pythr.txt'
# with open(filename) as book:
#     lines= book.read()
#     print(lines.replace('python', 'C'))
#     print(lines.replace('python', 'C'))
#     print(lines.replace('python', 'C'))

# filename = 'pytdz.txt'
# with open(filename, 'w') as biik:
#     print('1 - на текущей строке, 2 - на следующей')
#     run = True
#     while run:
#         op = int(input('Введите операцию - '))
#         if op == 1:
#             x = input("Введите текст - ")
#             biik.write(x)
#         elif op == 2:
#             y = input("Введите текст - ")
#             biik.write("\n" + y)
#         elif op == 0:
#             run = False
#         elif op != 1 or op!=0 or op!=2:
#             print("Операции не существует")
# with open(filename) as rrri:
#     lineq = rrri.read()
#     words = lineq.split()
#     print(words)
#     print(len(words))
