let Temperatura_corregida = 0
let Temperatura = 0
let Temperatura_corrección = 3
basic.forever(function () {
    Temperatura = input.temperature()
    Temperatura_corregida = Temperatura - Temperatura_corrección
    basic.showNumber(Temperatura_corregida)
    basic.pause(2000)
})
