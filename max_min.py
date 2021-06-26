class My_number:
    arr_number = []
    def __init__(self, number):
         self.arr_number = [int(i) for i in str(number)]

    def max_number(self):
        return max(self.arr_number)

    def min_number(self):
        return min(self.arr_number)
        

my_number = My_number(1023)

print(f'Max : {my_number.max_number()}')
print(f'Min : {my_number.min_number()}')