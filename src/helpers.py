from machine import ADC


def get_temperature():
    # read the temperature
    sensor = ADC(4)
    conversion_factor = 3.3 / (65535)

    reading = sensor.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    
    return temperature

    
def do_connect(ssid, password):
    import network, ntptime, machine
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('>> Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('>> Network config:', wlan.ifconfig())
    
    # set time and date with NTP
    print('>> Synchronizing time...')
    ntptime.settime()
    rtc = machine.RTC()
    now = rtc.datetime()
    print(f'>> Current time: {now[0]}-{now[1]:02}-{now[2]:02}T{now[4]:02}:{now[5]:02}:{now[6]:02}Z')