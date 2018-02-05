#coding=utf-8
class Car(object):
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		"""将里程表读数设置为指定的值"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Don't roll back the odometer!")
			
	def increment_odometer(self,miles):
		self.odometer_reading += miles
	
class Electriccar(Car):		#代表继承自car类创建一个electriccar类
	"""电动汽车的独特之处"""
	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super(Electriccar,self).__init__(make,model,year)
		self.battery_size = 70
		
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kwh battery.")
		
my_tesla = Electriccar('tesla','models',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ my_new_car.update_odometer(23)
# ~ my_new_car.update_odometer(18)
# ~ my_new_car.read_odometer()

# ~ print(my_new_car.get_descriptive_name())

