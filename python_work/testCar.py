#coding=utf-8
'''
作为Car.py的测试文件
'''
from Car import *
my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(23)
my_new_car.update_odometer(18)
my_new_car.read_odometer()

print(my_new_car.get_descriptive_name())
