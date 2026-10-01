def calcular_frete(peso_kg, cliente_novo):
    frete_base = peso_kg * 5.0
    if not cliente_novo:
        frete_base = frete_base * 0.9
    return round(frete_base, 2)

peso = 10
novo_cliente = False
print(calcular_frete(peso, novo_cliente))