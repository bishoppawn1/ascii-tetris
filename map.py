
tesla_car = {
    "vehicle": "car",
    "model": "tesla",
    "electric": "yes",
    "range": "medium",
    "cost": "high",
    "year": "2021",
    "colors": ["silver", "red", "blue"],
    "time": "1year",
    "new": "yes"
}

print(tesla_car["cost"])
tesla_car["cost"] = "24000"
print(tesla_car["cost"])