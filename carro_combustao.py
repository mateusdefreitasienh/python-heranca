from veiculo import Veiculo

class CarroCombustao(Veiculo):
  """
  Implementa a classe de carros a combustao
  """
  def __init__(self, modelo, marca, cor, ano, placa,
                     volume_tanque, tipo_combustivel, # Especificas para C.Combustao
                     cambio, consumo_combustao):
    """
    Construtor da classe carro a combustao
    """
    Veiculo.__init__(self, modelo, marca, cor, ano, placa) # classe pai
    self.volume_tanque = volume_tanque # Especificas para C. Combustao
    self.nivel_tanque = 0 # cria o carro com o tanque zerado
    self.tipo_combustivel = tipo_combustivel
    self.cambio = cambio
    self.consumo_combustao = consumo_combustao

  def __str__(self):
    msg  = super().__str__() # reuso do metodo da classe pai
    msg += f"Volume do tanque: {self.volume_tanque} l\n"
    msg += f"Tipo de Combustivel {self.tipo_combustivel}\n"
    msg += f"Cambio {self.cambio}\n"
    msg += f"Consumo medio: {self.consumo_combustao} km/l\n"
    return msg

  def abastacer(self, volume):
    """
    Metodo para abastecer carro a combustao
    """
    if volume >= 0: # volumes positivo
      if self.nivel_tanque + volume <= self.volume_tanque: # tem capacidade!
        self.nivel_tanque += volume
        print("Abastecimento ok!")
        print(f"Volume atual: {self.nivel_tanque}")
      else:
        print("O tanque vai transbordar!")
    else:
      print("Volume deve ser positivo!")