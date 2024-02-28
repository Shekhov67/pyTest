import json
class Car:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.mark = self.file_data['Mark']
        self.max_speed = self.file_data['max_speed']
    def read_data(self):
        with open(self.file_path, 'r') as cars_file:
            return json.load(cars_file)


car = Car('cls/cars.json')
print(car.file_data)