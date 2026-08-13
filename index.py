import random

def crear_baraja():
    """Crea una baraja de poker estándar de 52 cartas."""
    palos = ['Corazones ♥', 'Diamantes ♦', 'Tréboles ♣', 'Picas ♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # Creamos la lista combinando cada valor con cada palo
    baraja = [f"{valor} de {palo}" for palo in palos for valor in valores]
    return baraja

def sacar_cartas(baraja, cantidad):
    """
    Saca un número determinado de cartas. 
    Como usamos random.choice, la misma carta puede volver a salir.
    """
    cartas_sacadas = []
    for _ in range(cantidad):
        # random.choice elige un elemento al azar sin borrarlo de la lista original
        carta = random.choice(baraja)
        cartas_sacadas.append(carta)
        
    return cartas_sacadas

# --- EJEMPLO DE USO ---
mi_baraja = crear_baraja()

# Vamos a sacar 7 cartas al azar
numero_de_cartas = 7
resultado = sacar_cartas(mi_baraja, numero_de_cartas)

print(f"Has sacado {numero_de_cartas} cartas (¡pueden repetirse!):\n")
for i, carta in enumerate(resultado, 1):
    print(f"Carta {i}: {carta}")
