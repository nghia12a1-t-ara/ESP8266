import ConnectWIFI as wifi
import weatherData

wifi.connect("CamLinh_2.4Ghz", "xomtro36")
weatherData.getData('honoi')
