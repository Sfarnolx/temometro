Temperatura_corregida = 0
Temperatura = 0
Temperatura_corrección = 3

def on_forever():
    global Temperatura, Temperatura_corregida
    Temperatura = input.temperature()
    Temperatura_corregida = Temperatura - Temperatura_corrección
    basic.show_number(Temperatura_corregida)
    basic.pause(1000)
basic.forever(on_forever)
