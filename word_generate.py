from interval import Interval
import pandas as pd


def locate(x, a):
    intervals = [Interval(min, max, closed=True) for min, max in a]
    for i, interval in enumerate(intervals):
        if x in interval:
            return i
    return -1


def generate_business_word(data):
    string = ""
    string += str(data['business_id'])
    string += '*'
    string += data['cuisine']
    string += 'st' + str(int(data['stars']))

    a = [[0, 12], [13, 35], [36, 85], [86, 246],
         [247, 8350]]  # >90, >50, >20, >10, others
    string += 'rc' + str(locate(data['review_count'], a))

    string += 'os' + str(0 if data['OutdoorSeating'] == 'FALSE' else 1)
    string += 'ba' + str(0 if data['BusinessAcceptsCreditCards'] ==
                         'FALSE' else 1)
    string += 'rd' + str(0 if data['RestaurantsDelivery'] == 'FALSE' else 1)
    string += 'rr' + str(0 if data['RestaurantsReservations'] ==
                         'FALSE' else 1)
    string += 'wf' + str(0 if data['WiFi'] == 'No' else
                         (1 if data['WiFi'] == 'Yes' else 2))
    string += 'al' + str(0 if data['Alcohol'] == 'Full_Bar' else
                         (1 if data['Alcohol'] == 'Beer&Wine' else
                          (2 if data['Alcohol'] == 'No' else 3)))
    return string


def generate_user_word(data):
    string = ""
    #string = str(data['user_id'])
    string += 'h'+ str(data['history'])

    string += 'st' + str(int(data['average_stars']))
    string += 'yoe' + str(data['years_of_elite'])

    a = [(9, 27), (28, 58), (59, 118), (119, 260), (261, 10022)]
    string += 'rc' + str(locate(data['review'], a))

    a = [(0, 28), (29, 72), (73, 183), (184, 619), (620, 74829)]
    string += 'uf' + str(locate(data['useful'], a))

    a = [(0, 9), (10, 26), (27, 76), (77, 333), (334, 63148)]
    string += 'cl' + str(locate(data['cool'], a))

    a = [(0, 7), (8, 21), (22, 60), (61, 243), (243, 49785)]
    string += 'fn' + str(locate(data['funny'], a))

    a = [(0, 574), (575, 1750), (1751, 3934), (3935, 8907), (8908, 229534)]
    string += 'fr' + str(locate(data['friends'], a))


    return string
