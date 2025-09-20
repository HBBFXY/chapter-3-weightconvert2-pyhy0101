MOON_WEIGHT_RATIO = 0.165
ANNUAL_WEIGHT_GAIN = 0.5
YEARS = 10
current_weight = 0
print("\n未来10年您在地球和月球上的体重变化:")
print("年数\t地球体重(kg)\t月球体重(kg)")
print("-" * 40)
# 计算并输出未来10年的体重变化
for year in range(YEARS + 1):
    earth_weight = current_weight + year * ANNUAL_WEIGHT_GAIN
    moon_weight = earth_weight * MOON_WEIGHT_RATIO
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
