def change_string(ch):
    ch.append('four')
    print(ch)
    return ch

def greet(locals):
    for local in locals:     # 此式子等于  for local in locals.key():
        print(local)

def my_hello_world(
        my_para,

        this_parm
):
    print("hello world")



class Car:
    def __init__(self,name,price,out_time):
        self.name=name
        self.price=price
        self.out_time=out_time

    def show_info(self):
        print(self.name)

    def test(self,**te):
        print(te)

class Ele_car(Car):
    def __init__(self, name, price, out_time,battery_size):
        super().__init__(name, price, out_time)
        self.battery_size=battery_size

    def show_battery_size(self):
        print(f"电池容量={self.battery_size}")
        print(f"name={self.name}")

    def show_info(self):
        print(self.price)        