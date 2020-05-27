
class Veiculo():

    """Essa é a clase carro. Esta clase é utlizada para instanciar novos carros em nosso programa"""
    # Definindo Atributos
    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print("o objeto foi removido da memoria")


    # Definindo Meoodos
    def abastecer(self, qtd_combustivel):
        """O metodo abastecer recebe como parametro a quantidade de combustivel e incrementa no atributo
        qtd_combustivel do objeto carro"""
        self.qtd_combustivel += qtd_combustivel
        return

    def ligar(self):
        if self.is_ligado:
            print("O veiculo esta ligado")
        else:
            self.is_ligado = True
            print("o veiculo foi ligado")

    def desligar(self):
        if self.is_ligado == False:
            print("O veiculo ja esta desligado")
        else:
            self.is_ligado = False

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("o veiculo precisa estar ligado para ser acelerado")


