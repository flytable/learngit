#coding=utf-8
class Car(object):
	"""һ��ģ�������ļ򵥳���"""
	def __init__(self, make, model, year):
		"""��ʼ����������������"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""�����������������Ϣ"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""��ӡһ��ָ��������̵���Ϣ"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		"""����̱��������Ϊָ����ֵ"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Don't roll back the odometer!")
			
	def increment_odometer(self,miles):
		self.odometer_reading += miles
	
class Electriccar(Car):		#����̳���car�ഴ��һ��electriccar��
	"""�綯�����Ķ���֮��"""
	def __init__(self,make,model,year):
		"""��ʼ�����������"""
		super(Electriccar,self).__init__(make,model,year)
		self.battery_size = 70
		
	def describe_battery(self):
		"""��ӡһ��������ƿ��������Ϣ"""
		print("This car has a " + str(self.battery_size) + "-kwh battery.")
		
my_tesla = Electriccar('tesla','models',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ my_new_car.update_odometer(23)
# ~ my_new_car.update_odometer(18)
# ~ my_new_car.read_odometer()

# ~ print(my_new_car.get_descriptive_name())

