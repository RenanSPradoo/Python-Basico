num = int(input('Digite um numero para ver sua tabuada: '))

# print('-' * 12)
# print(f'{num}  x  {1:2} = {num*1}')
# print(f'{num}  x  {2:2} = {num*2}')
# print(f'{num}  x  {3:2} = {num*3}')
# print(f'{num}  x  {4:2} = {num*4}')
# print(f'{num}  x  {5:2} = {num*5}')
# print(f'{num}  x  {6:2} = {num*6}')
# print(f'{num}  x  {7:2} = {num*7}')
# print(f'{num}  x  {8:2} = {num*8}')
# print(f'{num}  x  {9:2} = {num*9}')
# print(f'{num}  x  {10:2} = {num*10}')
# print('-' * 12)

for i in range(1, 11):
    print(f'{num} x {i:2} = {num*i}')

