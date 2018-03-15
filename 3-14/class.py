class H(object):
	height = 0
	"""docstring for H"""
	def __init__(self):
		pass		

val = H()
vel = H()
vel.height = 6
print(val.height)
print(vel.height)
val.height = 10
print(val.height)
print(vel.height)
# Passing Val by reference to Vil
vil = val
print(vil.height)
vil.height = 8
print(vil.height)
print(val.height)

