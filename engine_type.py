VEHICLE_PETROL = 0
VEHICLE_DIESEL = 1
VEHICLE_LPG = 2
VEHICLE_ELECTRIC = 3

FUEL_RATES = [
    #["ENGINE_SIZE", "Petrol", "Diesel", "LPG", "Electric"],
    [11, None, 8, 4], #1,400cc or less
    [0, 9, None, 4], #1,600cc or less
    [13, None, 9, 4], #1,401cc - 2,000cc
    [None, 11, None, 4], #1,601cc to 2,000cc
    [19, 13, 14, 4], #Over 2,000cc.
]