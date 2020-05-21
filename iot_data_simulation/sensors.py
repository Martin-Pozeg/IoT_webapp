import random

class AqualaboOPTOD:

    def __init__(self):

        # degrees Celsius
        self.Temperature = 0
        self.TemperatureRangeMin = 0
        self.TemperatureRangeMax = 50
        self.TemperatureResolution = 0.01
        self.TemperatureAccuracy = 0.5

        # percentage saturation
        self.OxygenSaturation = 0
        self.OxygenSaturationRangeMin = 0
        self.OxygenSaturationRangeMax = 200
        self.OxygenSaturationResolution = 0.1
        self.OxygenSaturationAccuracy = 1

        # mg/L
        self.OxygenMgL = 0
        self.OxygenMgLRangeMin = 0
        self.OxygenMgLRangeMax = 20
        self.OxygenMgLResolution = 0.01
        self.OxygenMgLAccuracy = 0.1

        # Ppm
        self.OxygenPpm = 0
        self.OxygenPpmRangeMin = 0
        self.OxygenPpmRangeMax = 20
        self.OxygenPpmResolution = 0.01
        self.OxygenPpmAccuracy = 0.1


    def getTemperature(self):

        scaledFactor = 1 / self.TemperatureResolution
        scaledRangeMax = self.TemperatureRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getOxygenSaturation(self):

        scaledFactor = 1 / self.OxygenSaturationResolution
        scaledRangeMax = self.OxygenSaturationRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getOxygenMgL(self):

        scaledFactor = 1 / self.OxygenMgLResolution
        scaledRangeMax = self.OxygenMgLRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getOxygenPpm(self):

        scaledFactor = 1 / self.OxygenPpmResolution
        scaledRangeMax = self.OxygenPpmRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


class AqualaboPHEHT:

    def __init__(self):

        # degrees Celsius
        self.Temperature = 0
        self.TemperatureRangeMin = 0
        self.TemperatureRangeMax = 50
        self.TemperatureResolution = 0.01
        self.TemperatureAccuracy = 0.5

        # pH
        self.pH = 0
        self.pHRangeMin = 0
        self.pHRangeMax = 14
        self.pHResolution = 0.01
        self.pHAccuracy = 0.1

        # mV
        self.RedoxORP = 0
        self.RedoxORPRangeMin = -1000
        self.RedoxORPRangeMax = 1000
        self.RedoxORPResolution = 0.1
        self.RedoxORPAccuracy = 2
    

    def getTemperature(self):

        scaledFactor = 1 / self.TemperatureResolution
        scaledRangeMax = self.TemperatureRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result
    
    def getpH(self):

        scaledFactor = 1 / self.pHResolution
        scaledRangeMax = self.pHRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getRedoxORP(self):

        scaledFactor = 1 / self.RedoxORPResolution
        scaledRangeMax = self.RedoxORPRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


class AqualaboC4E:

    def __init__(self):

        # degrees Celsius
        self.Temperature = 0
        self.TemperatureRangeMin = 0
        self.TemperatureRangeMax = 50
        self.TemperatureResolution = 0.01
        self.TemperatureAccuracy = 0.5

        # uS/cm
        self.Conductivity = 0
        self.ConductivityRangeMin = 0
        self.ConductivityRangeMax = 200
        self.ConductivityResolution = 0.01
        self.ConductivityAccuracy = 2

        # Ppt = g/Kg
        self.Salinity = 0
        self.SalinityRangeMin = 5
        self.SalinityRangeMax = 60
        self.SalinityResolution = 0.01
        self.SalinityAccuracy = 0.06

        # ppm
        self.TDSKcl = 0
        self.TDSKclRangeMin = 0
        self.TDSKclRangeMax = 133000

    
    def getTemperature(self):

        scaledFactor = 1 / self.TemperatureResolution
        scaledRangeMax = self.TemperatureRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result
    
    def getConductivity(self):

        scaledFactor = 1 / self.ConductivityResolution
        scaledRangeMax = self.ConductivityRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getSalinity(self):

        scaledFactor = 1 / self.SalinityResolution
        scaledRangeMax = self.SalinityRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getTDSKcl(self):

        scaledFactor = 1 #/ self.TDSKclResolution
        scaledRangeMax = self.TDSKclRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


class AqualaboNTU:

    def __init__(self):

        # degrees Celsius
        self.Temperature = 0
        self.TemperatureRangeMin = 0
        self.TemperatureRangeMax = 50
        self.TemperatureResolution = 0.01
        self.TemperatureAccuracy = 0.5

        # NTU
        self.NephelometricTurbidity = 0
        self.NephelometricTurbidityRangeMin = 0
        self.NephelometricTurbidityRangeMax = 50
        self.NephelometricTurbidityResolution = 0.01
        self.NephelometricTurbidityAccuracy = 2.5

        # mg/L
        self.SS = 0
        self.SSRangeMin = 0
        self.SSRangeMax = 4500

    
    def getTemperature(self):

        scaledFactor = 1 / self.TemperatureResolution
        scaledRangeMax = self.TemperatureRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getNephelometricTurbidity(self):

        scaledFactor = 1 / self.NephelometricTurbidityResolution
        scaledRangeMax = self.NephelometricTurbidityRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getSS(self):

        scaledFactor = 1 #/ self.SSResolution
        scaledRangeMax = self.SSRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


class AqualaboCTZN:

    def __init__(self):

        # degrees Celsius
        self.Temperature = 0
        self.TemperatureRangeMin = 0
        self.TemperatureRangeMax = 50
        self.TemperatureResolution = 0.01
        self.TemperatureAccuracy = 0.5

        # mS/cm
        self.Conductivity = 0
        self.ConductivityRangeMin = 0
        self.ConductivityRangeMax = 100
        self.ConductivityResolution = 0.01

        # Ppt = g/kg
        self.Salinity = 0
        self.SalinityRangeMin = 5
        self.SalinityRangeMax = 60
        self.SalinityResolution = 0.1

        # mS/cm
        self.ConductivityNCWT = 0
        self.ConductivityNCWTRangeMin = 0
        self.ConductivityNCWTRangeMax = 100
        self.ConductivityNCWTResolution = 0.1


    def getTemperature(self):

        scaledFactor = 1 / self.TemperatureResolution
        scaledRangeMax = self.TemperatureRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getConductivity(self):

        scaledFactor = 1 / self.ConductivityResolution
        scaledRangeMax = self.ConductivityRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getSalinity(self):

        scaledFactor = 1 / self.SalinityResolution
        scaledRangeMax = self.SalinityRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result

    def getConductivityNCWT(self):

        scaledFactor = 1 / self.ConductivityNCWTResolution
        scaledRangeMax = self.ConductivityNCWTRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


class EurekaFluorometer:

    def __init__(self):

        # degrees Celsius
        self.CDOMfDOM = 0
        self.CDOMfDOMRangeMin = 0
        self.CDOMfDOMRangeMax = 1250

    
    def getCDOMfDOM(self):

        scaledFactor = 1 #/ self.CDOMfDOMResolution
        scaledRangeMax = self.CDOMfDOMRangeMax * scaledFactor

        result = random.randrange(0, scaledRangeMax, 1)
        result = result / scaledFactor

        return result


