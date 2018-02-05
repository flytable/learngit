#coding=utf-8
class Restaurant(object):

	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)
		
	def open_restaurant(self):
		print("restaurant shopping")
		
	def set_number_served(self,number_served):
		"""设置就餐人数"""
		self.number_served = number_served
		print(u"目前餐馆可以服务人数为：" + str(self.number_served))
		
	def increment_number_served(self,maybe_number_served):
		self.number_served += maybe_number_served
		print(u"餐馆预计能够再多接待的人数：" + str(maybe_number_served))
		print(u"餐馆预计能够服务的人数总和为：" + str(self.number_served))
		
class IceCreamStand(Restaurant):
	'''食物冰激凌'''
	def __init__(self,restaurant_name,cuisine_type):	#注意初始化方法的正确写法
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
		self.flavors=['apple','watermellon','banana']
			
	def visible_flavors(self):
		print (u"冰激凌的口味种类有：" + str(self.flavors))	#注意这里要类型转换
			
# ~ restaurant = Restaurant('xiangcai','xiha')
# ~ restaurant.describe_restaurant()
# ~ restaurant.set_number_served(20)
# ~ restaurant.increment_number_served(30)
# ~ restaurant.open_restaurant()
IceCream1 = IceCreamStand('xiangcai','xiha')
IceCream1.visible_flavors()
