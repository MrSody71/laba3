class AdvancedList(list):
    def average(self):
        if not self:
            return 0
        return sum(self) / len(self)

    def max_value(self):
        return max(self) if self else None

    def min_value(self):
        return min(self) if self else None


nums = AdvancedList([10, 20, 30, 40])

print("Список:", nums)
print("Среднее значение:", nums.average())
print("Максимум:", nums.max_value())
print("Минимум:", nums.min_value())
