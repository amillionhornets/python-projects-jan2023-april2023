regions = ["North", "South", "East", "West"]

regions.append("SouthWest")
regions.remove("South")
regions.sort()
for region in regions:
    print(region)
