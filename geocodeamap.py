# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:02:56 2018
"""

# 官方API: http://lbs.amap.com/api/webservice/guide/api/convert
# 坐标体系说明：http://lbs.amap.com/faq/top/coordinate/3
# GCJ02->WGS84 Java版本：http://www.cnblogs.com/xinghuangroup/p/5787306.html
# 验证坐标转换正确性的地址：http://www.gpsspg.com/maps.htm
# 以下内容为原创，转载请注明出处。

import math
import requests


class Geocodeamap():
    """利用高德API地理编码与纠偏"""
    def __init__(self, address, city):
        """初始化地理编码属性"""
        self.address = address
        self.city = city

    def geocode(self):
        """高德地理编码"""
        address=self.address
        city=self.city
        parameters={'address':address,
                    'key':'f9832c6b699055c6d86a9b9247717f43',
                    'city': city}
        base = 'http://restapi.amap.com/v3/geocode/geo'
        try:
            response=requests.get(base,parameters)
            answer=response.json()
            location=answer['geocodes'][0]['location']
            location=location.split(',')
            return location
        except:
            return address*2

    def wgs(self):
        '''对地理编码进行纠偏'''
        location =self.geocode()
        try:
            lng=float(location[0])
            lat=float(location[1])
            a=6278245.0# 克拉索夫斯基椭球参数长半轴a
            ee=0.00669342162296594323#克拉索夫斯基椭球参数第一偏心率平方
            pi=3.14159265358979324#圆周率
            # 以下为转换公式
            x = lng - 105.0
            y = lat - 35.0
            # 经度
            dlng = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
            dlng += (20.0 * math.sin(6.0 * x * pi) + 20.0 * math.sin(2.0 * x * pi)) * 2.0 / 3.0
            dlng += (20.0 * math.sin(x * pi) + 40.0 * math.sin(x / 3.0 * pi)) * 2.0 / 3.0
            dlng += (150.0 * math.sin(x / 12.0 * pi) + 300.0 * math.sin(x / 30.0 * pi)) * 2.0 / 3.0
            # 纬度
            dlat = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
            dlat += (20.0 * math.sin(6.0 * x * pi) + 20.0 * math.sin(2.0 * x * pi)) * 2.0 / 3.0
            dlat += (20.0 * math.sin(y * pi) + 40.0 * math.sin(y / 3.0 * pi)) * 2.0 / 3.0
            dlat += (160.0 * math.sin(y / 12.0 * pi) + 320 * math.sin(y * pi / 30.0)) * 2.0 / 3.0
            radlat = lat / 180.0 * pi
            magic = math.sin(radlat)
            magic = 1 - ee * magic * magic
            sqrtmagic = math.sqrt(magic)
            dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
            dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
            wgslng = lng - dlng
            wgslat = lat - dlat
            return [location[0]+','+location[1], wgslng,wgslat]
        except:
            return location


if __name__=="__main__":
    places = ['龙门山镇', '新兴镇', '隆丰镇', '',]   # '四川省江油县',
    for i in range(len(places)):
        print(i)
        locs = Geocodeamap(address=places[i], city='成都市').wgs()
        print(locs)
    print('welldone!')