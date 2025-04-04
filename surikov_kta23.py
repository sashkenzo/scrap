from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import time

product_id_last = ''
directory = os.getcwd() #Ваша нынешняя директория
subdirectory = '/.venv/test' #папка в директории где ваши файлы
csv_file_name = 'tags.csv'
log_file_name = 'tags.log'
with open(csv_file_name, 'w', newline='') as f: # Создаем файл csv
    f.write('name,url,sku,productID,category,brand,,,\n')

with open(log_file_name, 'w', newline='') as f: # Создаем файл csv
    f.write('files with error messages\n')

def file_parser(file_name,product_id_last): #Движок поиска именна того что указано в задание
    try:
        HTMLFileToBeOpened = open(file_name, "r")
        contents = HTMLFileToBeOpened.read()
        BeautifulSoupText = BeautifulSoup(contents, 'lxml')
        tag=BeautifulSoupText.find_all('script')[2] # наши файлы находятся во 2 тэги скрипт
        tag2=BeautifulSoupText.find_all('td' and 'b')
        tag_splited=tag.get_text().split('"')
        product = tag_splited[35]
        if(product != product_id_last): #проверка на повтор
            product_id_last = product
            with open(csv_file_name, 'a', newline='') as file: # Дописываем наши строки
                file.write(tag_splited[11]+','+tag_splited[15]+','+tag_splited[31]+','+tag_splited[35]+','+tag_splited [39]+','+tag_splited[49]+','+tag2[0].get_text()+','+tag2[1].get_text()+','+tag2[3].get_text()+'\n')
    except Exception as e:
        with open(log_file_name, 'a', newline='') as file:  # Логируем ошибки в файл
            file.write(file_name+'\n'+'error: '+str(e)+'\n')
    return product_id_last

for i in tqdm(range(len(os.listdir(directory+subdirectory))-1)):#Загрузка всех файлов с индексом .html
    if os.listdir(directory + subdirectory)[i].endswith('.html'):
        fname = os.path.join(directory + subdirectory, os.listdir(directory + subdirectory)[i])
        product_id_last = file_parser(fname, product_id_last)
    time.sleep(0.0001)
print("Complete.")


