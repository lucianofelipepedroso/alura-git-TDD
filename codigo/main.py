from codigo.bytebank import Funcionario

luciano = Funcionario('Luciano Felipe','26/06/1979',100000)
bonus= luciano.calcular_bonus()
print(bonus)