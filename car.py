class Car(object):
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f"model_name: {self.model_name}  mileage: {self.mileage}")
        print("Go to drive. Axcel on!!")

    def breakes(self):
        print(f"model_name: {self.model_name}  manufacturer: {self.manufacturer}")
        print("Stop the car.")


if __name__ == '__main__':
    nsx = Car('NSX', 9.5, 'Honda')
    nsx.gas()
    nsx.breakes()
    print(type(nsx))
