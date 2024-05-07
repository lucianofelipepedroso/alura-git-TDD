import sys

import pytest
from pytest import mark

from codigo.bytebank import Funcionario


class TestClass(object):
    #@pytest.mark.skipif(sys.version_info < (3, 11), reason="Requer Python na versão 3.9 ou superior")
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given contexto
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When ação

        assert resultado == esperado  # Then desfecho

    def test_quando_sobrenome__recebe_Luciano_Felipe_Pedroso_deve_retornar_Pedroso(self):
        entrada = 'Luciano Felipe Pedroso'  # Given contexto
        esperado = 'Pedroso'

        funcionario_teste = Funcionario(entrada, '26/06/1979', 1111)
        resultado = funcionario_teste.sobrenome()  # When ação

        assert resultado == esperado  # Then desfecho

    #@pytest.mark.skip(reason="não quero executar isso agora")
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = 'Luciano Felipe Pedroso'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '26/06/1979', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcula_bonus
    #@pytest.mark.xfail # Através do uso do marker xfail especificamos que o teste deve retornar uma falha, em vez de passar.
    def test_calcular_bonus_salrio_100(self):
        entrada_salario = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario('Luciano Felipe Pedroso', '26/06/1979', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcula_bonus
    def test_quando_calcular_bonus_recebe_salario_maior_1000_deve_retornar_exeception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given

            funcionario_teste = Funcionario('Luciano Felipe Pedroso', '26/06/1979', entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then

    # def test_str(self):
    #     nome, data_nascimento, salario = 'Luciano Felipe Pedroso', '26/06/1979', 1000
    #     esperado = "Funcionario(nome='Luciano Felipe Pedroso', data_nascimento='26/06/1979', salario=1000)"
    #     teste = Funcionario(nome, data_nascimento, salario)
    #     assert teste.__str__() == esperado
