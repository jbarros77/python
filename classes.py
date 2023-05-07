class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
        self.presente = True
        self.fechar = True

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(self.nome, 'Bateu meta!')
        else:
            print(self.nome, 'Não bateu meta!')

    def estar_na_loja(self):
            if self.presente:
                print(self.nome, 'Está presente na loja!')
            else:
                print(self.nome, 'Está ausente!')

    def fechar_caixa(self):
        if self.fechar:
            print(f"Fechando o caixa {self.nome} ")
        else:
            print('Larguei')

