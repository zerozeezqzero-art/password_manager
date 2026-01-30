import os
from menu import Menu
from class_obj import Password_Manager
from pass_gen import Generation
Manager = Password_Manager(path="path",password="password")
inp_pass = input("Введите пароль для входа: ")
if Manager.check(inp_pass):
	print("Доступ разрешён!")
	f = open("path","a",encoding="UTF-8") 
	os.system('attrib +h "path"')
	f.close()
	Menu(Manager) 
else:
	print("Неверный пароль!")