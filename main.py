nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


# 1. Решение посредством List Comprehension
list_comprehension = [result for element in nested_list for result in element]
print(list_comprehension)


# 2. Решение посредством итерации
class List_flatting_iterator():

	def __init__(self, my_list):
		self.my_list = my_list

	def create_flat_list(self, current_list, new_list):
		"""Обработка списка с любым уровнем вложенности"""
		for element in current_list:
			if type(element) != list:
				new_list.append(element)
			else:
				self.create_flat_list(element, new_list)
		return new_list

	def __iter__(self):
		self.count = -1
		return self

	def __next__(self):
		new_list = []
		self.count += 1
		flat_list = self.create_flat_list(self.my_list, new_list)
		if self.count == len (flat_list):
			raise StopIteration
		return flat_list[self.count]

for item in List_flatting_iterator(nested_list):
	print(item)


# 3. Решение посредством генерации
def list_flatting_generator(my_list):
	for element in my_list:
		if type(element) != list:
			yield element
		else:
			for item in list_flatting_generator(element):
				yield item

for item in list_flatting_generator(nested_list):
	print(item)

