def preciosfrutas():
    frutas = {'Fresa': 48.00, 'Kiwi':30.02, 'Manzana':28.90, 'Naranja':14.90}
    fruta = input('¿Qué fruta quieres? Frutas disponibles: Fresa, Kiwi, Manzana ').title()
    kg = float(input('¿Cuántos kilos? '))
    if fruta in frutas:
        print(kg, 'kilos de', fruta, 'valen','$', frutas[fruta]*kg)
    else: 
        print("Lo siento, la fruta", fruta, "no está disponible.")