def считать_информацию_из_txt(путь_к_файлу):
    with open(путь_к_файлу, encoding='utf-8') as файл:
        return файл.read()

if __name__ == '__main__':
    print(считать_информацию_из_txt('сорс для примера по классам.txt'))