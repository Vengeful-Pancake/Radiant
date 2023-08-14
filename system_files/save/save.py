import json

def SAVE(data,value,file):
    if data == "":
        with open('system_files\\save\\'+file, 'w') as d:
            json.dump(value,d)
    else:
        with open('system_files\\save\\'+file) as d:
            DATA_MANAGEMENT = json.load(d)
            for keys , values in DATA_MANAGEMENT.items():
                if keys == data:
                    DATA_MANAGEMENT[keys] = value
        with open('system_files\\save\\'+file, 'w+') as d:
            json.dump(DATA_MANAGEMENT,d)
        
def LOAD(data,file):
    with open('system_files\\save\\'+file) as d:
        DATA_MANAGEMENT = json.load(d)
        for keys , values in DATA_MANAGEMENT.items():
            if keys == data:
                return values