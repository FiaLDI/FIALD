# lisr = [0, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
#
#
# def num(list):
#     s = 0
#     for i in list:
#         s += 1
#     return s
#
#
# run = True
# while run:
#     f = int(input('Введите силу(1-10) '))
#     t0=int(input('Введите время полёта '))
#     run1 = True
#     while run1:
#         if f == 0:
#             print('Шар не летит')
#             run1 = False
#             run = False
#         elif f > 0:
#             print('Шар летит')
#             n = num(lisr)
#             v0=5
#             v=v0-lisr[f]
#             s=v*t0
#             print('Скорость полёта',v)
#             print('Длинна полёта',s)
#             run1=False
#

t0=int(input('Введите время полёта'))
filename = 'pytdz.txt'
with open(filename, 'w') as biik:
    run = True
    while run:
        s=0
        while s<=t0:
            for i in range(t0):
                v=str(input('Введите изменение скорости:'))
                biik.write(v+'\n')
                s+=2
        run=False


with open(filename) as rrri:
    lineq = rrri.read()
    words = lineq.split()
    print(words)
    re=len(words)
    print(re)
    sr=0
    for i in range(re):
        words[i]=int(i)
    for i in words:
        sr+=i
    sr1=sr/re
    print(sr1)
    s=sr1*t0
    print("Путь пройденный - ",s)