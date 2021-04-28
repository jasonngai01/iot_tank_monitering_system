Algae_Tank_Temperture = 0
Fish_Tank_Temperture = 0
MuseIoT.initialize_wifi()
MuseIoT.set_wifi("Iphone9", "95078437")
basic.pause(5000)

def on_forever():
    global Fish_Tank_Temperture, Algae_Tank_Temperture
    Fish_Tank_Temperture = Muse21.Thermometer_Liquid(Muse21.NTCType.NTC_TEMPERATURE_C, AnalogPin.P0)
    Algae_Tank_Temperture = Muse21.Thermometer_Liquid(Muse21.NTCType.NTC_TEMPERATURE_C, AnalogPin.P1)
    MuseOLED.write_string_new_line("IoT_montior")
    MuseOLED.write_string_new_line("Fish_Temp:")
    MuseOLED.write_num(Fish_Tank_Temperture)
    MuseOLED.write_string_new_line("Algae_Temp:")
    MuseOLED.write_num(Algae_Tank_Temperture)
    MuseOLED.write_string_new_line("Envir_Temp:")
    MuseOLED.write_num(input.temperature())
    MuseIoT.send_thingspeak("I0S05W9QM4RKAGHI",
        Fish_Tank_Temperture,
        Algae_Tank_Temperture,
        input.temperature())
    basic.pause(5000)
basic.forever(on_forever)
