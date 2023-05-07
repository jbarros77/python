from hashtag2023.python.classes import Vendedor

vendedor1 = Vendedor('Lira')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)
vendedor1.presente = True
vendedor1.estar_na_loja()
vendedor1.fechar = False
vendedor1.fechar_caixa()

vendedor2 = Vendedor('Alon')
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)
vendedor2.presente = False
vendedor2.estar_na_loja()
vendedor2.fechar = False
vendedor2.fechar_caixa()

vendedor3 = Vendedor('Sabino')
vendedor3.vendeu(1000)
vendedor3.bateu_meta(900)
vendedor3.presente = True
vendedor3.estar_na_loja()
vendedor3.fechar = True
vendedor3.fechar_caixa()