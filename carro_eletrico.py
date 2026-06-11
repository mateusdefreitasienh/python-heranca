from veiculo import Veiculo

class CarroEletrico(Veiculo):
  """
  Implementa a classe de carro eletrico
  """
  def __init__(self, modelo, marca, cor, ano, placa,
                     capacidade_bateria, tipo_bateria, # Especificas para C.Eletrico
                     autonomia, consumo_eletrico):
    """
    Construtor da classe carro eletrico
    """
    Veiculo.__init__(self, modelo, marca, cor, ano, placa) # classe pai
    self.capacidade_bateria = capacidade_bateria
    self.tipo_bateria = tipo_bateria
    self.nivel_bateria = 0
    self.autonomia = autonomia
    self.consumo_eletrico = consumo_eletrico

  def recarregar(self, carga):
    """
    Metodo para recarregar carro eletrico
    """
    if carga >= 0: # carga valida
      if self.nivel_bateria + carga <= self.capacidade_bateria:
        self.nivel_bateria += carga
        print("Carro recarregado com sucesso!")
        print(f"Nivel: {self.nivel_bateria}")
      else:
        print("Sobrecarga!")
    else:
      print("Carga deve ser positiva!")

  def __str__(self): 
    msg  = super().__str__()
    msg += f"Nivel bateria: {self.capacidade_bateria}\n"
    msg += f"Tipo bateria: {self.tipo_bateria}\n"
    msg += f"Autonomia: {self.autonomia}\n"
    msg += f"Consumo eletrico: {self.consumo_eletrico}\n"
    return msg

