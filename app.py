from veiculo import Veiculo
from carro_combustao import CarroCombustao
from carro_eletrico import CarroEletrico
from carro_hibrido import CarroHibrido

moto = Veiculo(marca  = "Yamaha",
               modelo = "MT303",
               ano    =  2020,
               cor    = "Azul",
               placa  = "III-1234")
voyage = CarroCombustao(marca  = "Volkswagen",
                        modelo = "Novo Voyage",
                        ano    =  2018,
                        cor    = "Vermelho",
                        placa  = "AAA-1234",
                        volume_tanque = 55, # especificos C.Combustao
                        tipo_combustivel = "Flex",
                        cambio = "Manual",
                        consumo_combustao = 10)
byd = CarroEletrico(marca  = "BYD",
                    modelo = "Dolphin",
                    ano    =  2025,
                    cor    = "Preta",
                    placa  = "AAA-4321",
                    capacidade_bateria = 100,
                    tipo_bateria = "LFP",
                    autonomia = 348,
                    consumo_eletrico = 12)

corolla_altis = CarroHibrido()


print(moto)
print(voyage)
print(byd)

voyage.abastacer(10)
voyage.abastacer(46)
byd.recarregar(10)

