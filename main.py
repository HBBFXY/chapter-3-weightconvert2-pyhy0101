moonup= 0.165*0.5
earthup=0.5
years= 10
print("\n未来10年您在地球和月球上的体重变化:")
print("年数\t地球体重(kg)\t月球体重(kg)")
print("-" * 40)
for year in range(years + 1):
    earth_weight = year * earthup     
    moon_weight = year * moonup 
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
