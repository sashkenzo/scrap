from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import time

product_id_last = ''
directory = os.getcwd() #Ваша нынешняя директория
subdirectory = '/halftest' #папка в директории где ваши файлы
csv_file_name = 'tags.csv'

with open(csv_file_name, 'w', newline='') as f: # Создаем файл csv
    f.write('name,url,sku,productID,category,brand,,,\n')

def file_parser(file_name,product_id_last): #Движок поиска именна того что указано в задание
    def tag_splitter(tag_splited, tag_number):
        return tag_splited[tag_number].split('"')

    HTMLFileToBeOpened = open(file_name, "r")
    contents = HTMLFileToBeOpened.read()

    BeautifulSoupText = BeautifulSoup(contents, 'html.parser')

    tag=BeautifulSoupText.find_all('script')[2] # наши файлы находятся во 2 тэги скрипт
    tag2=BeautifulSoupText.find_all('td' and 'b')
    tag_splited=tag.get_text().split(',')
    try:
        product = tag_splitter(tag_splited, 8)[3]
        if(product != product_id_last): #проверка на повтор
            product_id_last = product
            with open(csv_file_name, 'a', newline='') as file: # Дописываем наши строки
                file.write(tag_splitter(tag_splited,2)[3]+','+tag_splitter(tag_splited, 3)[3]+','+tag_splitter(tag_splited, 7)[3]+','+tag_splitter(tag_splited,8)[3]+','+tag_splitter(tag_splited,9)[3]+','+tag_splitter(tag_splited,11)[3]+','+tag2[0].get_text()+','+tag2[1].get_text()+','+tag2[3].get_text()+'\n')
    except:
        pass
    return product_id_last

for i in tqdm(range(len(os.listdir(directory+subdirectory))-1)):#Загрузка всех файлов с индексом .html
    if os.listdir(directory + subdirectory)[i].endswith('.html'):
        fname = os.path.join(directory + subdirectory, os.listdir(directory + subdirectory)[i])
        product_id_last = file_parser(fname, product_id_last)
    time.sleep(0.1)

print("Complete.")


