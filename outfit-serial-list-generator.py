categories = [
    "Guns",
    "Turrets",
    "Secondary Weapons",
    "Ammunition",
    "Systems",
    "Power",
    "Engines",
    "Hand to Hand",
    "Unique",
    "Licenses"
]

gu_series = [""]

sw_series = [
    "Fixed Secondaries",
    "Turreted Secondaries"
]

sy_series = [
    "$Drives",
    "Shields",
    "Repair",
    "Cooling",
    "Scanners",
    "Jammers",
    "Ramscoops",
    "Special Systems",
    "$Fuel",
    "$Passenger",
    "%Utility",
]

po_series = [
    "Generators",
    "Batteries"
]

h2_series = [
    "Offensive H2H",
    "Defensive H2H",
    "Fortifications"
]

un_series = [
    "$Functional Unique",
    "$Non-Functional Unique"
]

species = [
    "Human",
    "Hai",
    "Remnant",
    "Korath",
    "Ka'het",
    "Gegno",
    "Coalition",
    "Wanderers",
    "Bunrodea",
    "Pug",
    "Quarg",
    "Incipias",
    "Successors",
    "Avgi",
    "%Other"
    ]

def iterate(category_series, s):
    s = ""
    label = 1

    for series in category_series:
        if series[0] == "$":
            index = label * 100
            s += '\t"' + (series.replace("$","") + '" '+ str(index) + "\n")
        elif series[0] == "%":
            index = 9999
            s += '\t"' + (series.replace("%","") + '" '+ str(index) + "\n")
        else:
            for spec in species:
                if spec[0] == "%":
                    index = (100 * label) + 99
                else:
                    index = (100 * label) + species.index(spec)
                
                s += '\t"' + (series + ": " + str(spec.replace("%","")) + '" ' + str(index) + "\n")
        label += 1
    return s

def iterate_singular(name, s):
    s = ""

    ser = 0
    for spec in species:
        if spec[0] == "%":
            index = 99
        else:
            index = species.index(spec)
        
        s += '\t"' + (name + ": " + str(spec.replace("%","")) + '" ' + str(index) + "\n")
    return s

f = open("series.txt", "w")
data = 'category "series":\n'
for category in categories:
    data += "\t"
    data += ("# " + category + "\n") # Add comment tags

    match category:
        case "Guns": data += iterate_singular("Guns", data)
        case "Turrets": data += iterate_singular("Turrets", data)
        case "Secondary Weapons": data += iterate(sw_series, data)
        case "Ammunition": data += iterate_singular("Ammunition", data)
        case "Systems": data += iterate(sy_series, data)
        case "Power": data += iterate(po_series, data)
        case "Engines": data += iterate_singular("Engines", data)
        case "Hand to Hand": data += iterate(h2_series, data)
        case "Unique": data += iterate(un_series, data)
        case "Licenses": data += iterate_singular("Licenses", data)

f.write(data)
f.close()