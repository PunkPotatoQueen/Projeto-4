import pytest
from validacao import validar_entrada

def test_valido():
    valor, mensagem = validar_entrada("123.45")
    assert valor is True
    assert mensagem == ""

def test_vazio():
    valor, mensagem = validar_entrada("")
    assert valor is False
    assert mensagem == "Este campo é obrigatório."

def test_nao_numerico():
    valor, mensagem = validar_entrada("texto")
    assert valor is False
    assert mensagem == "Valor inválido. Insira um número."

def test_espacos():
    valor, mensagem = validar_entrada("  456  ")
    assert valor is True
    assert mensagem == ""

def test_numero_ponto():
    valor, mensagem = validar_entrada("1234.56")
    assert valor is True
    assert mensagem == ""

def test_numero_virgula():
    valor, mensagem = validar_entrada("1234,56")
    assert valor is False
    assert mensagem == "Valor inválido. Provavelmete você utilizou vírgula ao invés de ponto."

def test_numero_grande():
    valor, mensagem = validar_entrada("1e+100")
    assert valor is True
    assert mensagem == ""
