import os
import json
import subprocess


class connectSSH():
    def __init__(self):
        self.action = None
        self.json = None


    # Изменить данные в json
    def updateLoginAndPass(self):
        print("\n")
        
        for index, data in enumerate(self.json[self.ip]):
            print(str(index) + ") " +
                  data["login"])
            
        index = input("Выберите индекс данных: ")

        # Проверка на целое число и есть ли оно в диапазоне индексов 
        if not index.isdigit() or int(index) > len(self.json):
            print("Неверный индекс\n")
        else:
            login = input("Логин: ")
            password = input("Пароль: ")

            self.json[self.ip][int(index)]["login"] = login
            self.json[self.ip][int(index)]["password"] = password

            with open('ip.json', 'w') as jsonFile:
                json.dump(self.json, jsonFile, ensure_ascii=False, indent=4)


    # Добавить данные авторизации в json
    def addLoginAndPass(self):
        print("\n")

        login = input("\nВведите логин: ")
        password = input("Введите пароль: ")

        self.json[self.ip].append({
            "login": login,
            "password": password
        })

        with open('ip.json', 'w') as jsonFile:
            json.dump(self.json, jsonFile, ensure_ascii=False, indent=4)


    # Удалени данных авторизации в json
    def removeLoginAndPass(self):
        print("\n")

        for index, data in enumerate(self.json[self.ip]):
            print(str(index) + ") " +
                  data["login"])
            
        index = input("Выберите индекс данных: ")
                
        # Проверка на целое число и есть ли оно в диапазоне индексов 
        if not index.isdigit() or int(index) > len(self.json):
            print("Неверный индекс\n")
        else:
            self.json[self.ip].pop(int(index))

            with open('ip.json', 'w') as jsonFile:
                json.dump(self.json, jsonFile, ensure_ascii=False, indent=4)


    # Работа с ip
    def workIp(self):
        self.action = None

        while True:
            print("\n1) Добавить ip\n" +
                  "2) Изменить данные для ssh\n" +
                  "3) Добавить данные для входа ssh\n" +
                  "4) Удалить данные для входа ssh\n" +
                  "5) Назад")
            self.action = input("Выберите действие: ")
            
            # Добавление ip в json
            if self.action == "1":
                ip = input("\nВведите ip: ")
                
                if not ip in self.json:
                    self.json.update({ip: []})

                with open('ip.json', 'w') as jsonFile:
                    json.dump(self.json, jsonFile, ensure_ascii=False, indent=4)
            
            # Изменение данных в json
            elif self.action == "2":
                print("\n")

                for index, ip in enumerate(self.json):
                    print(str(index) + ") " + ip)

                index = input("Выберите индекс ip: ")
                
                # Проверка на целое число и есть ли оно в диапазоне индексов 
                if not index.isdigit() or int(index) > len(self.json):
                    print("Неверный индекс\n")
                else:
                    self.ip = list(self.json.keys())[int(index)]
                    self.updateLoginAndPass()

            # Добавление данных в json
            elif self.action == "3":
                print("\n")

                for index, ip in enumerate(self.json):
                    print(str(index) + ") " + ip)

                index = input("Выберите индекс ip: ")
                
                # Проверка на целое число и есть ли оно в диапазоне индексов 
                if not index.isdigit() or int(index) > len(self.json):
                    print("Неверный индекс\n")
                else:
                    self.ip = list(self.json.keys())[int(index)]
                    self.addLoginAndPass()

            # Удаление данных в json
            elif self.action == "4":
                print("\n")

                for index, ip in enumerate(self.json):
                    print(str(index) + ") " + ip)

                index = input("Выберите индекс ip: ")
                
                # Проверка на целое число и есть ли оно в диапазоне индексов 
                if not index.isdigit() or int(index) > len(self.json):
                    print("Неверный индекс\n")
                else:
                    self.ip = list(self.json.keys())[int(index)]
                    self.removeLoginAndPass()

            # Выход в главное меню
            elif self.action == "5":
                break
            else:
                print("\nНеверный код действия\n\n")


    # Подключение по ssh
    def workSSH(self):
        for index, ip in enumerate(self.json):
            print(str(index) + ") " + ip)

        indexIp = input("Выберите индекс ip: ")

        if indexIp == "" or not indexIp.isdigit() or int(indexIp) > len(self.json):
            print("Неверный индекс\n")
            pass

        self.ip = list(self.json.keys())[int(indexIp)]

        print("\n")
        for index, data in enumerate(self.json[self.ip]):
            print(str(index) + ") " +
                  self.json[self.ip][index]["login"])
        
        indexUser = input("Выберите индекс пользователя: ")

        if indexUser == "" or not indexUser.isdigit() or int(indexUser) > len(self.json[self.ip]):
            print("Неверный индекс\n")
        else:
            loginUser = self.json[self.ip][int(indexUser)]["login"]
            passwordUser = self.json[self.ip][int(indexUser)]["password"]
            subprocess.Popen(["putty", "-ssh", f"{loginUser}@{self.ip}", "-pw", f"{passwordUser}"], shell=True)


    # Главное меню
    def start(self):
        with open('ip.json', 'r') as file:
            self.json = json.load(file)

        # Главное меню
        while True:
            print("\n1) Действия с ip\n" +
                  "2) Подключение по ssh\n" +
                  "3) Выйти")
            self.action = input("Выберите действие: ")


            if self.action == "1":
                self.workIp()
            elif self.action == "2":
                self.workSSH()
            elif self.action == "3":
                break
            else:
                print("\nНеверный код действия\n\n")

# os.system("putty -ssh root@95.163.236.234 -pw ~wTWK9o%tgUk")

if __name__ == "__main__":
    connectSSH = connectSSH()
    connectSSH.start()