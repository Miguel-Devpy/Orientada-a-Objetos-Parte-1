import carro, moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)

print(f"A quantidade de combustivel do carro vermelho é : {uno_vermelho.qtd_combustivel}")

moto_vermelho = moto.Moto("vermelho","gasolina",1.0, 2)
moto_vermelho.ligar()
print(moto_vermelho.is_ligado)





