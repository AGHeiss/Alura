from veiculo import Carro, Moto

carro_01 = Carro('Chevrolet', 'Cobalt', ligado=True, portas=4)
carro_02 = Carro('Volkswagen', 'Polo', ligado=False, portas=4)
carro_03 = Carro('Toyota', 'Corolla', ligado=True, portas=4)

moto_01 = Moto('Suzuki', 'A20', ligado=True, tipo='Casual')
moto_02 = Moto('Suzuki', 'A30', ligado=True, tipo='Esportiva')
moto_03 = Moto('Yamaha', 'A40', ligado=False, tipo='Esportiva')

print(carro_01)
carro_01.ligar()
print(carro_02)
carro_02.ligar()
print(carro_03)
carro_03.ligar()
print(moto_01)
moto_01.ligar()
print(moto_02)
moto_02.ligar()
print(moto_03)
moto_03.ligar()
