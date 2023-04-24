import json
import random
import datetime


def random_value(minimum, maximum):
    return float("{0:.3f}".format(random.uniform(minimum, maximum)))


def generate_json(dic_option, DMC, date):
    if dic_option == 1:
        data = {
            "TTNR": 4189866339,
            "Parameter": [
                {"Key": "ADC_BG0", "Value": random_value(100, 200)},
                {"Key": "PHQ_OFFSET", "Value": random_value(-10, 10)},
                {"Key": "DMC_GUT", "Value": DMC}
            ],
            "ArrayParameter": [
                {"Key": "R1BA30RW", "Value": [random_value(0, 10), random_value(10, 20), random_value(20, 30)]},
                {"Key": "R1DA30RW", "Value": [random_value(0, -10), random_value(-10, -20), random_value(-20, -30)]},
                {"Key": "I1BA30RW",
                 "Value": [random_value(-100, 100), random_value(-100, 100), random_value(-100, 100)]}
            ],
            "fileName": DMC + "_ks.xml",
            "fileCreationDate": date
        }
    elif dic_option == 2:
        data = {
            "TTNR": 4270190723,
            "Parameter": [
                {"Key": "ADC_BG0", "Value": random_value(100, 200)},
                {"Key": "PHQ_OFFSET", "Value": random_value(-10, 10)},
                {"Key": "DMC_GUT", "Value": DMC}
            ],
            "fileName": DMC + "_hs.xml",
            "fileCreationDate": date
        }
    elif dic_option == 3:
        data = {
            "TTNR": 4015597692,
            "Parameter": [
                {"Key": "ADP3_DMIV", "Value": random_value(10, 80)},
                {"Key": "RCS_WERK", "Value": random_value(-10, 5)},
                {"Key": "DMC_GUT", "Value": DMC}
            ],
            "ArrayParameter": [
                {"Key": "R1BA30RW", "Value": [random_value(0, 10), random_value(10, 20), random_value(20, 30)]},
                {"Key": "R1DA30RW", "Value": [random_value(0, -10), random_value(-10, -20), random_value(-20, -30)]},
                {"Key": "I1BA30RW",
                 "Value": [random_value(-100, 100), random_value(-100, 100), random_value(-100, 100)]}
            ],
            "fileName": DMC + "_xs.xml",
            "fileCreationDate": date
        }
    elif dic_option == 4:
        data = {
            "TTNR": 4191518501,
            "Parameter": [
                {"Key": "ADP3_DMIV", "Value": random_value(10, 80)},
                {"Key": "RCS_WERK", "Value": random_value(-10, 5)},
                {"Key": "DMC_GUT", "Value": DMC}
            ],
            "fileName": DMC + "_vs.xml",
            "fileCreationDate": date
        }
    return data


start_time = datetime.datetime(2018, 5, 6, 00, 00, 00)
start_DMC = 14500

count = 0

for count in range(0, 10):
    DMC = str(start_DMC + count)
    date = str(start_time + datetime.timedelta(0, 4 * count))
    type_dic = random.randint(1, 4)

    if type_dic == 1:
        filename = 'filesToTest/' + DMC + '_ks.json'
    elif type_dic == 2:
        filename = 'filesToTest/' + DMC + '_hs.json'
    elif type_dic == 3:
        filename = 'filesToTest/' + DMC + '_xs.json'
    elif type_dic == 4:
        filename = 'filesToTest/' + DMC + '_vs.json'

    with open(filename, 'w') as outfile:
        data = generate_json(type_dic, DMC, date)
        json.dump(data, outfile)
