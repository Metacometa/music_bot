import random

def fix_list(records):
    records = records.replace('[', '')
    records = records.replace(']', '')
    records = records.replace('(', '')
    records = records.replace(')', '')
    records = records.replace("'", '')
    records = records.replace("\"", '')
    x = 1
    while x < len(records):
        if (records[x - 1] != ',') and (records[x] == ','):
            records = records[:x] + '' + records[x + 1:]
        x = x + 1
    x = 1
    while x < len(records):
        if records[x - 1] == ',':
            records = records[:x] + records[x + 1:]
        x = x + 1
    records = records.replace(',', '\n')
    return records

def get_song(arg):
    return arg[5:]

def get_random_joke(message):
    f = open('unemployed_jokes.txt', 'r', encoding='utf-16')
    s = f.readlines()
    n = random.randrange(0,len(s))
    print(str(s))
    records = s[n]
    records = records.replace('[', '')
    records = records.replace(']', '')
    records = records.replace('(', '')
    records = records.replace(')', '')
    records = records.replace("'", '')
    records = records.replace("\"", '')
    records = records.replace('n', '')
    f.close()
    return records