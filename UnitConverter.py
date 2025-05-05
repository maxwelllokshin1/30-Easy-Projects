lengthUnits = ("in", "mm", "ft", "cm", "yd", "m", "miles", "km")
massUnits = ("oz", "g", "lbs", "kg", "ton")
volUnits = ("tsp", "ml", "tbsp", "l", "fl oz", "gal", "cup", "pint", "cubic m", "cubic ft", "cubic in")
tempUnits = ("F", "C", "K")

def lengthCon(number, from_, to):
    to_meters = {
        "in": 0.0254,
        "mm": 0.001,
        "ft": 0.3048,
        "cm": 0.01,
        "yd": 0.9144,
        "m": 1.0,
        "miles": 1609.34,
        "km": 1000.0
    }

    from_meters = {unit: 1 / factor for unit, factor in to_meters.items()}

    meters = number * to_meters[from_]
    result = meters * from_meters[to]

    return result

def massCon(number, from_, to):
    to_kg = {
        "oz": 35.274,
        "lbs": 2.205,
        "g": 1000,
        "kg": 1.0,
        "ton": 1/1000,
    }

    from_kg = {unit: 1 / factor for unit, factor in to_kg.items()}

    meters = number * to_kg[from_]
    result = meters * from_kg[to]

    return result

def volumeCon(number, from_, to):
    to_cubMeters = {
        "gal": 0.00378541, 
        "pint": 0.000473176,
        "cup": 0.000236588, 
        "fl oz": 0.000029574,
        "tbsp": 0.000014787, 
        "tsp": 0.0000049289, 
        "cubic m": 1.0, 
        "l": 0.001,  
        "ml": 0.000001, 
        "cubic ft": 0.0283168, 
        "cubic in": 0.000016387,
    }

    from_cubMeters = {unit: 1 / factor for unit, factor in to_cubMeters.items()}

    meters = number * to_cubMeters[from_]
    result = meters * from_cubMeters[to]

    return result

def tempCon(number, from_, to):
    to_kelvin = {
        "F": lambda x: (x - 32) * 5/9 + 273.15,
        "C": lambda x: x + 273.15,
        "K": lambda x: x,
    }

    from_kelvin = {
        "F": lambda x: (x - 273.15) * 9/5 + 32,
        "C": lambda x: x - 273.15,
        "K": lambda x: x,
    }

    kelvin = to_kelvin[from_](number)
    result = from_kelvin[to](kelvin)

    return result



def main():
    number = float(input("value: "))
    from_ = input("from: ")
    to = input("to: ")
    res = None
    if from_ in lengthUnits and to in lengthUnits:
        res = lengthCon(number, from_, to)
    if from_ in massUnits and to in massUnits:
        res = massCon(number, from_, to)
    if from_ in volUnits and to in volUnits:
        res = volumeCon(number, from_, to)
    if from_ in tempUnits and to in tempUnits:
        res = tempCon(number, from_, to)

    if res != None:
        print(number, from_, "---->",res, to)

if __name__ == "__main__":
    main()