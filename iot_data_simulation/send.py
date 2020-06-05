import os
import time

from parser import parseDHMZ

from sensors import AqualaboOPTOD
from sensors import AqualaboPHEHT
from sensors import AqualaboC4E
from sensors import AqualaboNTU
from sensors import AqualaboCTZN
from sensors import EurekaFluorometer


# Is DHMZ data being parsed and used
IS_DHMZ_PARSING_ACTIVE=True


# Constants
MQTT_ADAPTER_IP="hono.eclipseprojects.io"
MY_DEVICE="636ea23e-45db-4106-b1c7-bdeb14f6861c"
MY_TENANT="4082acd7-4e7e-4c3d-b2b5-d9e8e056a147"
MY_PWD="pass"

TIME_TO_SLEEP=900
TIME_TO_SLEEP_BETWEEN_SENDING_MESSAGE=2


# Example of a working command
# mosquitto_pub -h $MQTT_ADAPTER_IP -u $MY_DEVICE@$MY_TENANT -P $MY_PWD -t telemetry -m '{"temp": -15}'
# Example of working parameters: location = "temp"; value = "-38"
def send(location, value):
    print("Sending... " + location + " -> " + value)
    cmd = "mosquitto_pub -h " + MQTT_ADAPTER_IP + " -u " + MY_DEVICE + "@" + MY_TENANT + " -P " + MY_PWD + " -t telemetry -m '{\"" + location + "\": " + value + "}'"
    os.system(cmd)
    time.sleep(TIME_TO_SLEEP_BETWEEN_SENDING_MESSAGE)


# Code starts here
myAqualaboOPTOD = AqualaboOPTOD()
myAqualaboPHEHT = AqualaboPHEHT()
myAqualaboC4E = AqualaboC4E()
myAqualaboNTU = AqualaboNTU()
myAqualaboCTZN = AqualaboCTZN()
myEurekaFluorometer = EurekaFluorometer()


# Function that sends data from a virtual device
def virtualDevice(name):

    # Data from sensor AqualaboOPTOD
    if (IS_DHMZ_PARSING_ACTIVE):
        parsedValue = parseDHMZ(name)
        send(name + "/" + "Temperature", str(parsedValue))
    else:
        send(name + "/" + "Temperature", str(myAqualaboOPTOD.getTemperature()))

    send(name + "/" + "OxygenSaturation", str(myAqualaboOPTOD.getOxygenSaturation()))
    send(name + "/" + "OxygenMgL", str(myAqualaboOPTOD.getOxygenMgL()))
    send(name + "/" + "OxygenPpm", str(myAqualaboOPTOD.getOxygenPpm()))

    # Data from sensor AqualaboPHEHT
    send(name + "/" + "pH", str(myAqualaboPHEHT.getpH()))
    send(name + "/" + "RedoxORP", str(myAqualaboPHEHT.getRedoxORP()))

    # Data from sensor AqualaboC4E
    send(name + "/" + "Conductivity", str(myAqualaboC4E.getConductivity()))
    send(name + "/" + "Salinity", str(myAqualaboC4E.getSalinity()))
    send(name + "/" + "TDSKcl", str(myAqualaboC4E.getTDSKcl()))

    # Data from sensor AqualaboNTU
    send(name + "/" + "NephelometricTutrbidity", str(myAqualaboNTU.getNephelometricTurbidity()))
    send(name + "/" + "SS", str(myAqualaboNTU.getSS()))

    # Data from sensor AqualaboCTZN
    send(name + "/" + "ConductivityNCWT", str(myAqualaboCTZN.getConductivityNCWT()))

    # Data from sensor EurekaFluorometer
    send(name + "/" + "CDOMfDOM", str(myEurekaFluorometer.getCDOMfDOM()))


# Main thread
if __name__ == "__main__":

    try:

        while True:

            virtualDevice("Unije")
            virtualDevice("Susak")
            virtualDevice("Ilovik")
            virtualDevice("Premuda")
            virtualDevice("Tramerka")
            virtualDevice("Kornati")
            virtualDevice("Mljet")
            virtualDevice("Cavtat")
            virtualDevice("Plavnik")
            virtualDevice("Vir")

            time.sleep(TIME_TO_SLEEP)

    except KeyboardInterrupt:

        pass
