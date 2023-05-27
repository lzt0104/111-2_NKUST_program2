from weight_calculator import WeightCalculator

height = float(input("請輸入身高（公分）："))
gender = int(input("請輸入性別（1代表男性；2代表女性）："))

calculator = WeightCalculator(height, gender)
standard_weight = calculator.calculate_standard_weight()

print("標準體重為：", standard_weight)