class FrequencyTracker:
    def __init__(self) -> None:
        self.number_frequency = Counter()  
        self.frequency_count = Counter()
        
    def add(self, number):
        self.number_frequency[number] += 1
        self.frequency_count[self.number_frequency[number]] += 1
        self.frequency_count[self.number_frequency[number] - 1] -= 1
        
    def deleteOne(self, number):
        if self.number_frequency[number] > 0:
            self.number_frequency[number] -= 1
            if self.number_frequency[number] == 0:
                del self.number_frequency[number]
            self.frequency_count[self.number_frequency[number]] += 1
            self.frequency_count[self.number_frequency[number] + 1] -= 1
    
    def hasFrequency(self, frequency):
        print(self.frequency_count)
        return self.frequency_count[frequency] > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)