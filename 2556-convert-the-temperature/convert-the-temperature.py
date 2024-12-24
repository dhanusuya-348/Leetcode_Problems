class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = celsius + 273.15
        ans.append(kelvin)
        farenheit = celsius * 1.80 + 32.00
        ans.append(farenheit)
        return ans
        