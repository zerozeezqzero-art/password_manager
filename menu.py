from class_obj import Password_Manager
from pass_gen import Generation

def Menu(Classobject_manager):
		while True:
			try:
				choice = int(input(
				"1 - ➕ Добавить пароль\n"
				"2 - ➖ Удалить пароль\n"
				"3 - 👁️  Вывести список паролей\n"
				"4 - ⚙️  Сгенерировать пароль длинной от 8 до 14\n"
				"5 -  Добавить пароль buldak\n"
				))
				if choice == 1:
					append_pass = input("Введите пароль который хотите добавить\n")
					Classobject_manager.add_pass(append_pass)
				if choice == 2:
					del_pass = input("Введите пароль который вы хотите удалить\n")
					Classobject_manager.del_pass(del_pass)
				if choice == 3:
						data = Classobject_manager.read_pass()
						print("ваши пароли - ",*data,sep="\n")
				if choice == 4:
						generated_password = Generation()
						choice1 = int(input(f"Сгенерированный пароль - {generated_password}\n1 - Добавить\n2 - Не добавлять\n"))
						if choice1 == 1:
							Classobject_manager.add_pass(generated_password)
				if choice == 5:
					Classobject_manager.buldak()
			except ValueError:
				print("❌ НЕКОРРЕКТНЫЙ ВВОД!")