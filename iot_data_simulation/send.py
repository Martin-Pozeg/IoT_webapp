import os

from sensors import AqualaboOPTOD
from sensors import AqualaboPHEHT
from sensors import AqualaboC4E
from sensors import AqualaboNTU
from sensors import AqualaboCTZN
from sensors import EurekaFluorometer

# Constants
MQTT_ADAPTER_IP="hono.eclipseprojects.io"
MY_DEVICE="6bedc376-7fbe-4c67-8791-cd9999f333a2"
MY_TENANT="68297be8-b81f-49fd-9303-310e90374d48"
MY_PWD="pass"

# Example of a working command
# mosquitto_pub -h $MQTT_ADAPTER_IP -u $MY_DEVICE@$MY_TENANT -P $MY_PWD -t telemetry -m '{"temp": -15}'
# Example of working parameters: location = "temp"; value = "-38"
def send(location, value):
    print("Sending... " + location + " -> " + value)
    cmd = "mosquitto_pub -h " + MQTT_ADAPTER_IP + " -u " + MY_DEVICE + "@" + MY_TENANT + " -P " + MY_PWD + " -t telemetry -m '{\"" + location + "\": " + value + "}'"
    os.system(cmd)


# Code starts here
myAqualaboOPTOD = AqualaboOPTOD()
myAqualaboPHEHT = AqualaboPHEHT()
myAqualaboC4E = AqualaboC4E()
myAqualaboNTU = AqualaboNTU()
myAqualaboCTZN = AqualaboCTZN()
myEurekaFluorometer = EurekaFluorometer()

# Data from sensor AqualaboOPTOD
send("Temperature", str(myAqualaboOPTOD.getTemperature()))
send("OxygenSaturation", str(myAqualaboOPTOD.getOxygenSaturation()))
send("OxygenMgL", str(myAqualaboOPTOD.getOxygenMgL()))
send("OxygenPpm", str(myAqualaboOPTOD.getOxygenPpm()))

# Data from sensor AqualaboPHEHT
send("pH", str(myAqualaboPHEHT.getpH()))
send("RedoxORP", str(myAqualaboPHEHT.getRedoxORP()))

# Data from sensor AqualaboC4E
send("Conductivity", str(myAqualaboC4E.getConductivity()))
send("Salinity", str(myAqualaboC4E.getSalinity()))
send("TDSKcl", str(myAqualaboC4E.getTDSKcl()))

# Data from sensor AqualaboNTU
send("NephelometricTutrbidity", str(myAqualaboNTU.getNephelometricTurbidity()))
send("SS", str(myAqualaboNTU.getSS()))

# Data from sensor AqualaboCTZN
send("ConductivityNCWT", str(myAqualaboCTZN.getConductivityNCWT()))

# Data from sensor EurekaFluorometer
send("CDOMfDOM", str(myEurekaFluorometer.getCDOMfDOM()))