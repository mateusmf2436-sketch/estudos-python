l = float(input('quantos metros mede a largura da sua parede: '))
a = float(input('quantos metros mede a altura da sua parede: '))
area = l*a
litros_tinta = area/2
print(f'a area de sua parede é {area :.2f};\n sera necessario {litros_tinta :.2f}L de tinta para pinta-la')