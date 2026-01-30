import os
from menu import Menu
from class_obj import Password_Manager
from pass_gen import Generation
Manager = Password_Manager()
inp_pass = input("Введите пароль для входа: ")
if Manager.check(inp_pass):
	print("Доступ разрешён!")
	f = open("C:/Users/zeroz/Desktop/PYTHON/mega_manager_password/pass.txt","a",encoding="UTF-8") 
	os.system('attrib +h "C:/Users/zeroz/Desktop/PYTHON/mega_manager_password/pass.txt"')
	f.close()
	Menu(Manager) 
else:
	print("Неверный пароль!")