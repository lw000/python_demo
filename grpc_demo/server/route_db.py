'''
Created on 2017年12月29日

@author: Administrator
'''

import sys
import json

sys.path.append('./')
sys.path.append('../')
sys.path.append('../proto')

import chat_pb2

def read_route_database():
    '''Reads the route guide database.
  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  '''
    feature_list = []
    with open('../proto/route_guide_db.json') as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = chat_pb2.Feature(
                name=item['name'],
                location=chat_pb2.Point(
                    latitude=item['location']['latitude'],
                    longitude=item['location']['longitude']))
            feature_list.append(feature)
    return feature_list


if __name__ == '__main__':
    pass
