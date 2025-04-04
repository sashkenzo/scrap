from bs4 import BeautifulSoup
import os
product_id_last = ''
directory = os.getcwd() #Ваша нынешняя директория
subdirectory = '/test' #папка в директории где ваши файлы

with open('.venv/tags.csv', 'w', newline='') as f: # Создаем файл csv
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
            with open('.venv/tags.csv', 'a', newline='') as file: # Дописываем наши строки
                file.write(tag_splitter(tag_splited,2)[3]+','+tag_splitter(tag_splited, 3)[3]+','+tag_splitter(tag_splited, 7)[3]+','+tag_splitter(tag_splited,8)[3]+','+tag_splitter(tag_splited,9)[3]+','+tag_splitter(tag_splited,11)[3]+','+tag2[0].get_text()+','+tag2[1].get_text()+','+tag2[3].get_text()+'\n')
    except:
        pass
    return product_id_last

for filename in os.listdir(directory+subdirectory): #Загрузка всех файлов с индексом .html
    if filename.endswith('.html'):
        fname = os.path.join(directory+subdirectory, filename)
        product_id_last=file_parser(fname,product_id_last)



