import os
import json
import csv
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv.field_size_limit(sys.maxsize)

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
                    writer.writerows(
                        [[title, text, 1 if folder[0] == 'F' else 0]])


def write_data_from_HORNE2017(directory, sources):
    global c
    for source in sources:
        for folder in ['Fake', 'Real']:
            temp_directory = directory + source+' Political News Dataset'+'/'+folder
            for f in os.listdir(os.path.join(BASE_DIR, temp_directory)):
                with open(os.path.join(temp_directory+'_titles', f), encoding="utf8", errors='ignore') as ft, open(os.path.join(temp_directory, f), encoding="utf8", errors='ignore') as f, open('data.csv', 'a') as csv_file:
                    c += 1
                    writer = csv.writer(csv_file)
                    title, text = ft.read(), f.read()
                    title = re.sub(r'\W+', ' ', title)
                    text = re.sub(r'\W+', ' ', text)
                    writer.writerows(
                        [[title, text, 1 if folder[0] == 'F' else 0]])


def write_data_from_FakeNews():
    with open(os.path.join(BASE_DIR, 'Datasets/FakeNews/train.csv'), "r") as f, open('data.csv', "a") as ff:
        reader = csv.reader(f, delimiter=",")
        writer = csv.writer(ff)
        next(reader)
        for row in reader:
            content = list(re.sub(r'\W+', ' ', row[i]) for i in [1, 3, 4])
            writer.writerows(
                [[content[0], content[1], content[2]]])


def shape():
    with open('data.csv', "r") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
        print(len(data))


write_data_from_HORNE2017(
    'Datasets/Horne2017_FakeNewsData/Public Data/', ('Buzzfeed', 'Random'))
write_data_from_FAKENEWSNET(
    'Datasets/FakeNewsNet-master/Data/', ('BuzzFeed', 'PolitiFact'))
write_data_from_FakeNews()
shape()
