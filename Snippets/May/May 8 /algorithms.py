#web var for storing "websites", has a bunch of statistics that imitate what might come from a pdf scraping.
#Plays into all steps by being the "web" being searched.
web = {
    "https://www.mouser.com/datasheet/2/315/ABA0000C1212-1516607.pdf": {
        "componentName": "Panasonic Aluminum Capacitor", "RoHs": "Yes", "Voltage": "10-63", "Current": 100, 
        "Capacitance": "100-4700μF", "ESR": "0.8-1.2Ω", "Endurance": "20000 hrs", "Tolerance": "20%"
    },
    "https://cdn.andymark.com/media/W1siZiIsIjIwMTkvMDcvMTIvMTIvMDYvMjUvODkzM2EwNGYtZDhiMC00YjFhLTgzZTItOWEwY2FhOWE2ZjZlL0xpbWl0IFN3aXRjaC5wZGYiXV0/Limit%20Switch.pdf?sha=235d01d491142030": {
        "componentName": "Andymark Limit Switch","RoHS": "Yes", "Voltage": 12, "Current": 11, "Force": .78, "Pretravel": 4
    },
    "https://baomain.com/products/b07sgppgd4": {
        "componentName": "Baomain Full Bridge Rectifier", "RoHs": "Yes", "Voltage": 1600, "Current": 200, "MaxTemp": "150℃", "Weight": "1091g"
    },
    "https://www.mouser.com/datasheet/2/813/DS-16888-Omron_Relay_G5LE-1_DC3-1888652.pdf": {
        "componentName": "Omron Cube Relay", "RoHs": "Yes", "Voltage": 48, "Current": 10, "Poles": 1, "Resistance": "100mΩ", "Temperature": "85℃"
    }
}

def formatOutput(url):
    #probably (definitely) a better way to do this, but it makes it much more configurable to just add each fstring together
    #adds each str together in "otherStats", then prints that at the end because each has different stats.
    if url == "https://www.mouser.com/datasheet/2/315/ABA0000C1212-1516607.pdf":
        otherStats = f"Capacitance: {web[url]['Capacitance']}", f"ESR: {web[url]['ESR']}", f"Endurance: {web[url]['Endurance']}", f"Tolerance: {web[url]['Tolerance']}"
    elif url == "https://cdn.andymark.com/media/W1siZiIsIjIwMTkvMDcvMTIvMTIvMDYvMjUvODkzM2EwNGYtZDhiMC00YjFhLTgzZTItOWEwY2FhOWE2ZjZlL0xpbWl0IFN3aXRjaC5wZGYiXV0/Limit%20Switch.pdf?sha=235d01d491142030":
        otherStats = f"Force: {web[url]['Force']}N", f"Pretravel: {web[url]['Pretravel']}mm"
    elif url == "https://baomain.com/products/b07sgppgd4":
        otherStats = f"Maximum Temperature: {web[url]['MaxTemp']}", f"Weight: {web[url]['Weight']}"
    elif url == "https://www.mouser.com/datasheet/2/813/DS-16888-Omron_Relay_G5LE-1_DC3-1888652.pdf":
        otherStats = f"Poles: {web[url]['Poles']}", f"Coil Resistance: {web[url]['Resistance']}", f"Maximum Temperature: {web[url]['Temperature']}"
    else:
        #exits if the url isn't right from the 4 options
        print("Invalid URL. Check the dictionary for a list of valid URLs.")
        exit()
    #getting rid of tuple's formatting, namely the parenthesis and 's.
    otherStats = str(otherStats).replace(")", "").replace("(", "").replace("'", "")
    return otherStats

def main():
    #userInput line is both Step 1: Find the name of the component, and Step 2: Filter out unnecessary information
    #gets URL, which in turn finds the name of the component, later printed in line 47.
    userInput = input("URL: ").lower().strip()
    #Step 3: Search the Web
    if userInput in web:
        otherStats = formatOutput(userInput)
    #Step 4: Print datasheet values
    print(f"""
Component: {web[userInput]['componentName']}
--------------------------------------------
RoHs Compliant: {web[userInput]['RoHs']}
Maximum Voltage: {web[userInput]['Voltage']}V
Maximum Current: {web[userInput]['Current']}A
--------------------------------------------
Other statistics:
{otherStats}""")


main()