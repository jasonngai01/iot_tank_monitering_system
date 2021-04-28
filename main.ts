let Algae_Tank_Temperture = 0
let Fish_Tank_Temperture = 0
MuseIoT.initializeWifi()
MuseIoT.setWifi("Iphone9", "95078437")
basic.pause(5000)
basic.forever(function on_forever() {
    
    Fish_Tank_Temperture = Muse21.Thermometer_Liquid(Muse21.NTCType.NTC_temperature_C, AnalogPin.P0)
    Algae_Tank_Temperture = Muse21.Thermometer_Liquid(Muse21.NTCType.NTC_temperature_C, AnalogPin.P1)
    MuseOLED.writeStringNewLine("IoT_montior")
    MuseOLED.writeStringNewLine("Fish_Temp:")
    MuseOLED.writeNum(Fish_Tank_Temperture)
    MuseOLED.writeStringNewLine("Algae_Temp:")
    MuseOLED.writeNum(Algae_Tank_Temperture)
    MuseOLED.writeStringNewLine("Envir_Temp:")
    MuseOLED.writeNum(input.temperature())
    MuseIoT.sendThingspeak("I0S05W9QM4RKAGHI", Fish_Tank_Temperture, Algae_Tank_Temperture, input.temperature())
    basic.pause(5000)
})
