import pytest
import primeira_aula

def test_realizar_soma_com_numero():
    assert primeira_aula.Calculadora.soma(1,2) == 3, "Deveria ser igual a 3"

def test_realizar_soma_com_string():
    assert primeira_aula.Calculadora.soma('1','2') == 3, "Deveria ser igual a 3"
    
def test_realizar_soma_com_string_e_numero():
    assert primeira_aula.Calculadora.soma('1',2) == 3, "Deveria ser igual a 3"

def test_realizar_soma_nao_numerico():
    with pytest.raises(ValueError):
        primeira_aula.Calculadora.soma('a', 'b')

def test_data_nascimento_em_dias():
    assert primeira_aula.Calculadora.calcular_idade_em_dias('29/04/2025') == 1

def test_data_nascimento_em_dias_hoje():
    assert primeira_aula.Calculadora.calcular_idade_em_dias('30/04/2025') == 1


def test_data_nascimento_futura_invalida():
    with pytest.raises(ValueError):
        primeira_aula.Calculadora.calcular_idade_em_dias('29/05/2030')
    
        