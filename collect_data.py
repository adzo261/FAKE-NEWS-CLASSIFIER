import os
import json
import csv
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open('data.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([['title', 'text', 'label']])

directory = 'Datasets/FakeNewsNet-master/Data/BuzzFeed/RealNewsContent'

c = 1


def write_data_from_FAKENEWSNET(directory, sources):
    global c
    for source in sources:
        for folder in ['Fake', 'Real']:
            temp_directory = directory + source+'/'+folder+'NewsContent'
            for f in os.listdir(os.path.join(BASE_DIR, temp_directory)):
                with open(os.path.join(temp_directory, f)) as f, open('data.csv', 'a') as csv_file:
                    data = json.load(f)
                    writer = csv.writer(csv_file)
                    c += 1
                    title, text = str(data['title'].encode(
                        'ascii', 'ignore'), 'utf-8'), str(data['text'].encode(
                            'ascii', 'ignore'), 'utf-8')
                    title = re.sub(r'\W+', ' ', title)
                    text = re.sub(r'\W+', ' ', text)
                    writer.writerows([[title, text, folder[0]]])


def write_data_from_HORNE2017(directory, sources):
    global c
    for source in sources:
        for folder in ['Fake', 'Real']:
            temp_directory = directory + source+' Political News Dataset'+'/'+folder
            for f in os.listdir(os.path.join(BASE_DIR, temp_directory)):
                with open(os.path.join(temp_directory+'_titles', f), encoding="utf8", errors='ignore') as ft, open(os.path.join(temp_directory, f), encoding="utf8", errors='ignore') as f, open('data.csv', 'a') as csv_file:
                    # print(f.name, ft.name)
                    print(c, f.name)
                    c += 1
                    writer = csv.writer(csv_file)
                    title, text = ft.read(), f.read()
                    title = re.sub(r'\W+', ' ', title)
                    text = re.sub(r'\W+', ' ', text)
                    writer.writerows([[title, text, folder[0]]])


def shape():
    with open('data.csv', "r") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
        print(len(data))


write_data_from_HORNE2017(
    'Datasets/Horne2017_FakeNewsData/Public Data/', ('Buzzfeed', 'Random'))
write_data_from_FAKENEWSNET(
    'Datasets/FakeNewsNet-master/Data/', ('BuzzFeed', 'PolitiFact'))
shape()
