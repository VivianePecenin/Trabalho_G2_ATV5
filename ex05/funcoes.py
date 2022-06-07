from math import pi

def calcular_area_quadrado(lado: float) -> float:
    return lado ** 2

def calcular_area_circulo(raio: float) -> float:
    return pi * raio ** 2

def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def tipo_de_calculo():
    print('escolha um opção para calcular a area:')
    print('1- quadrado')
    print('2- circulo')
    print('3- triangulo')
    opcao = int(input(' opção: '))
    return opcao

def opcao_1(opcao: int):
    lado = float(input('informe o lado do quadrado: '))
    area = calcular_area_quadrado(lado)
    return area

def opcao_2(opcao: int):
    raio = float(input('informe o raio do circulo: '))
    area = calcular_area_circulo(raio)
    return area

def opcao_3(opcao: int):
    base = float(input('informe a base do triangulo: '))
    altura = float(input('informe a altura do triangulo: '))
    area = calcular_area_triangulo(base, altura)
    return area