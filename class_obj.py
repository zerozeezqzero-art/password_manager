from pass_gen import Generation
class Password_Manager:
	def __init__(self):
		self.path =  "C:/Users/zeroz/Desktop/PYTHON/mega_manager_password/pass.txt"
		self.password = "dudoser"
	def check(self, inp_pass):
		return self.password == inp_pass
	def read_pass(self):
		with open(self.path, "r", encoding="UTF-8") as readdata:
			return [x.strip() for x in readdata.readlines()]
	def add_pass(self, new_pass):
		with open(self.path, "a", encoding="UTF-8") as writedata:
			return writedata.write(new_pass + "\n")
	def del_pass(self, del_pass):
		deleted = False
		save_lines = []
		with open(self.path, "r+", encoding="UTF-8") as readdata:
			for passw in readdata:
				if passw.strip() != del_pass:
					save_lines.append(passw)
				else:
					deleted = True
		with open(self.path, "w", encoding="UTF-8") as writedata:
			writedata.writelines(save_lines)
		if deleted:
			print("Пароль успешно удален")
		else:
			print("Пароль не найден")
	def buldak(self):
		with open(self.path,"a",encoding="UTF-8") as writedata:
			return writedata.write("buldak\n")
