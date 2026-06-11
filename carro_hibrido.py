from carro_eletrico import CarroEletrico
from carro_combustao import CarroCombustao

class CarroHibrido(CarroCombustao, CarroEletrico):
  """
  Classe carro hibrido que herda de C.C. e C.E.
  """
  def __init__(self, modelo, marca, cor, ano, placa,
                     volume_tanque, tipo_combustivel, # Especificas para C.Combustao
                     cambio, consumo_combustao,
                     capacidade_bateria, tipo_bateria, # Especificas para C.Eletrico
                     autonomia, consumo_eletrico):
    CarroCombustao.__init__(self, modelo, marca, cor, ano, placa,
                     volume_tanque, tipo_combustivel, # Especificas para C.Combustao
                     cambio, consumo_combustao)
    CarroEletrico.__init__(self, modelo, marca, cor, ano, placa,
                     capacidade_bateria, tipo_bateria, # Especificas para C.Eletrico
                     autonomia, consumo_eletrico)
