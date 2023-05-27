class WeightCalculator:
    def __init__(self, height, gender):
        self.height = height
        self.gender = gender

    def calculate_standard_weight(self):
        if self.gender == 1:  # 男性
            standard_weight = (self.height - 80) * 0.7
        elif self.gender == 2:  # 女性
            standard_weight = (self.height - 70) * 0.6
        else:
            raise ValueError("Invalid gender value. Please enter 1 for male or 2 for female.")
        return standard_weight