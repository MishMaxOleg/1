import sys
from colorama import Fore, init
init()
vtex = (Fore.LIGHTCYAN_EX + "Введите текст:")
verror = (Fore.LIGHTRED_EX + "Ошибка!")
vhelp = (Fore.GREEN + "help")
a = print("(Справочник по командам) "+ f"{vhelp}: ")
print (''' 
            "stop" - Завершает выполнение программы. ("Введите текст:")
      ''')

v = str(input("Введите mode(w,a): "))
if v=="w":
  v = 'w'
elif v=="a":
  v = 'a'
else:
  print(f"{verror}")
#'w' - Предыдущие записи будут стерты и вы начнете писать сначало.
#'a' - Начнете дописывать текущий документ.
file = open('text.txt',v,encoding="utf8") #ЕСЛИ НУЖНО РАБОТАТЬ С ДРУГИМ ФАЙЛОМ - 
                                          #'text.txt' - замени на название своего Файла с .txt
while True:
  text = str(input(f"{vtex} "))
  if text.lower() == "stop":
     break
  text1 = input("Переход на новую строчку(+/-): ")
  if text1 == "+": 
    file.write(text.replace("stop","") + "\n")  
  elif text1 == "-": 
    file.write(text.replace("stop","") + " ")  
  else:
      print(f"{verror}") 
  print("AddContent!")
file.close()  