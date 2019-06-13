from interval import Interval


def locate(x, a):
    intervals = [Interval(min, max, closed=True) for min, max in a]
    for i, interval in enumerate(intervals):
        if x in interval:
            return i
    return -1


def generate_business_word(data):
    string = ""
    #string = str(data['business_id'])
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
    string += 'st' + str(int(data['average_stars']))
    string += 'yoe' + str(data['years_of_elite'])
    a = [(9, 13), (14, 22), (23, 39), (40, 88), (89, 13278)]
    string += 'rc' + str(locate(data['review'], a))
    a = [(0, 1), (2, 4), (5, 13), (14, 46), (47, 154202)]
    string += 'uf' + str(locate(data['useful'], a))
    a = [(0, 0), (0, 1), (2, 3), (4, 13), (14, 148658)]
    string += 'cl' + str(locate(data['cool'], a))
    a = [(0, 0), (0, 1), (2, 3), (4, 12), (13, 130207)]
    string += 'fn' + str(locate(data['funny'], a))
    a = [(0, 4), (5, 46), (47, 550), (551, 2254), (2255, 292798)]
    string += 'fr' + str(locate(data['friends'], a))

    return string