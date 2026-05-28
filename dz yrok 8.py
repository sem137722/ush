from pprint import pprint


toyota_rav4 = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1650000,
    "enginevolume": 2.5,
    "totalweight": 2225,
    "maxspeed": 180
}


toyota_rav4["max weight with trailer and brakes"] = 1650

toyota_rav4["insurance_payment"] = toyota_rav4["price"] * 0.005

print(toyota_rav4["model"])
print(toyota_rav4["price"])

pprint(toyota_rav4)