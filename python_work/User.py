#coding=utf-8
class User():
	
	def __init__(self,first_name,last_name,login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts
		
	def describe_user(self):		#用户描述
		print("user's name is " + str(self.first_name)+str(self.last_name))
		
	def greet_user(self):		#跟用户打招呼
		print("hello,"+str(self.first_name)+str(self.last_name))
		
	def increment_login_attempts(self):	#用户登录记录属性
		self.login_attempts = self.login_attempts + 1
	
	def reset_login_attempts(self):		#重置用户登录记录
		self.login_attempts = 0
		
user1 = User('Lebrawn','James',5)
user1.describe_user()
user1.greet_user()

'''测试User类的自增加登录方法和重置方法'''
user1.increment_login_attempts()
user1.increment_login_attempts()
print user1.login_attempts

user1.reset_login_attempts()
print user1.login_attempts
		
