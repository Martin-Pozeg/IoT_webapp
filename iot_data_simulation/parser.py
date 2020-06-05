from datetime import datetime
from lxml import html
import requests


def parseDHMZ(name):

    # datetime object containing current date and time
    now = datetime.now()
    #print("now =", now)

    # dd/mm/YY H:M:S
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)

    currentHours = now.strftime("%H")
    #print(currentHours)
    hours = int(currentHours)


    # Parser
    page = requests.get('https://meteo.hr/podaci.php?section=podaci_vrijeme&param=more_n')
    tree = html.fromstring(page.content)


    dhmzDubrovnik07 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[2]/text()')
    dhmzDubrovnik08 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[3]/text()')
    dhmzDubrovnik11 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[4]/text()')
    dhmzDubrovnik14 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[5]/text()')
    dhmzDubrovnik15 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[6]/text()')
    dhmzDubrovnik17 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[3]/td[7]/text()')

    dhmzMaliLosinj07 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[2]/text()')
    dhmzMaliLosinj08 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[3]/text()')
    dhmzMaliLosinj11 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[4]/text()')
    dhmzMaliLosinj14 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[5]/text()')
    dhmzMaliLosinj15 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[6]/text()')
    dhmzMaliLosinj17 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[9]/td[7]/text()')

    dhmzZadar07 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[2]/text()')
    dhmzZadar08 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[3]/text()')
    dhmzZadar11 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[4]/text()')
    dhmzZadar14 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[5]/text()')
    dhmzZadar15 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[6]/text()')
    dhmzZadar17 = tree.xpath('//*[@id="table-aktualni-podaci"]/tbody[1]/tr[17]/td[7]/text()')
    

    if (name == "Unije"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzMaliLosinj17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzMaliLosinj07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzMaliLosinj08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzMaliLosinj11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzMaliLosinj14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzMaliLosinj15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzMaliLosinj17[0])


    if (name == "Susak"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzMaliLosinj17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzMaliLosinj07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzMaliLosinj08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzMaliLosinj11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzMaliLosinj14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzMaliLosinj15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzMaliLosinj17[0])
        

    if (name == "Ilovik"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzMaliLosinj17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzMaliLosinj07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzMaliLosinj08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzMaliLosinj11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzMaliLosinj14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzMaliLosinj15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzMaliLosinj17[0])
        

    if (name == "Premuda"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzZadar17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzZadar07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzZadar08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzZadar11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzZadar14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzZadar15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzZadar17[0])


    if (name == "Tramerka"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzZadar17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzZadar07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzZadar08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzZadar11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzZadar14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzZadar15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzZadar17[0])


    if (name == "Kornati"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzZadar17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzZadar07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzZadar08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzZadar11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzZadar14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzZadar15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzZadar17[0])
        

    if (name == "Mljet"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzDubrovnik17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzDubrovnik07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzDubrovnik08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzDubrovnik11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzDubrovnik14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzDubrovnik15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzDubrovnik17[0])


    if (name == "Cavtat"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzDubrovnik17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzDubrovnik07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzDubrovnik08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzDubrovnik11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzDubrovnik14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzDubrovnik15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzDubrovnik17[0])


    if (name == "Plavnik"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzMaliLosinj17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzMaliLosinj07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzMaliLosinj08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzMaliLosinj11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzMaliLosinj14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzMaliLosinj15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzMaliLosinj17[0])


    if (name == "Vir"):
        
        if (hours >= 0 and hours < 7):
            return float(dhmzZadar17[0])

        if (hours >= 7 and hours < 8):
            return float(dhmzZadar07[0])

        if (hours >= 8 and hours < 11):
            return float(dhmzZadar08[0])

        if (hours >= 11 and hours < 14):
            return float(dhmzZadar11[0])

        if (hours >= 14 and hours < 15):
            return float(dhmzZadar14[0])

        if (hours >= 15 and hours < 17):
            return float(dhmzZadar15[0])

        if (hours >= 17 and hours < 24):
            return float(dhmzZadar17[0])


#print(parseDHMZ("Susak"))
#print(parseDHMZ("Kornati"))
#print(parseDHMZ("Mljet"))
