moonup= 0.165
earthup=0.5
years= 10
weight= 0
print("\n未来10年您在地球和月球上的体重变化:")
print("年数\t地球体重(kg)\t月球体重(kg)")
print("-" * 40)
for year in range(years + 1):
    earth_weight = weight + year * earthup     
    moon_weight = earth_weight * moonup 
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
