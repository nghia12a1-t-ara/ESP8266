from time import sleep

def connect(ss_id, pw):
    import network
    ssid = ss_id
    password = pw
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        print("Not connected to network")
        sleep(0.5)
    print("Connected is successful")
    print(station.ifconfig())
