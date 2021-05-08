# -*- coding: utf-8 -*-

from geocoding_amap import geocodeamap
import xlrd
from xlutils.copy import copy


# 一列地址
def write_xls(filename, sheet, col, city):  # 这里的文件类型为.xls
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_index(sheet)
    wgswb = copy(wb)
    wgsws = wgswb.get_sheet(sheet)
    wgsws.write(0, ws.ncols, "location")
    wgsws.write(0, ws.ncols + 1, "wgslng")
    wgsws.write(0, ws.ncols + 2, "wgslat")
    adds = ws.col_values(col)
    for i in range(1, len(adds)):
        try:
            print(i)
            wgs = geocodeamap.Geocodeamap(address=adds[i], city=city).wgs()
            #print(wgs)
            wgsws.write(i, ws.ncols, wgs[0])
            wgsws.write(i, ws.ncols + 1, wgs[1])
            wgsws.write(i, ws.ncols + 2, wgs[2])
        except:
            print(adds[i])
            pass
    try:
        wgswb.save(filename)
    except TypeError:
        wgswb.save(filename.replace('.xlsx','.xls'))
    print('good!')


# 两列构成地址
def write_xls1(filename, sheet, col1, col2, city):  # 这里的文件类型为.xls
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_index(sheet)
    wgswb = copy(wb)
    wgsws = wgswb.get_sheet(sheet)
    wgsws.write(0, ws.ncols, "location")
    wgsws.write(0, ws.ncols + 1, "wgslng")
    wgsws.write(0, ws.ncols + 2, "wgslat")
    adds1 = ws.col_values(col1)
    adds2 = ws.col_values(col2)
    adds = list(zip(adds1, adds2))
    for i in range(1, 2):
    # for i in range(1, len(adds)):
        try:
            print(i)
            wgs = geocodeamap.Geocodeamap(address=adds[i], city=city).wgs()
            # print(wgs)
            wgsws.write(i, ws.ncols, wgs[0])
            wgsws.write(i, ws.ncols + 1, wgs[1])
            wgsws.write(i, ws.ncols + 2, wgs[2])
        except:
            print(adds[i])
            pass
    try:
        wgswb.save(filename)
    except TypeError:
        wgswb.save(filename.replace('.xlsx','.xls'))
    print('good!')


# 指定城市
def write_xls2(filename, sheet, col1, city):  # 这里的文件类型为.xls
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_index(sheet)
    wgswb = copy(wb)
    wgsws = wgswb.get_sheet(sheet)
    wgsws.write(0, ws.ncols, "location")
    wgsws.write(0, ws.ncols + 1, "wgslng")
    wgsws.write(0, ws.ncols + 2, "wgslat")
    adds = ws.col_values(col1)
    citys = ws.col_values(city)
    # for i in range(1, 2):
    for i in range(1, len(adds)):
        try:
            print(i)
            wgs = geocodeamap.Geocodeamap(address=adds[i], city=citys[i]).wgs()
            # print(wgs)
            wgsws.write(i, ws.ncols, wgs[0])
            wgsws.write(i, ws.ncols + 1, wgs[1])
            wgsws.write(i, ws.ncols + 2, wgs[2])
        except:
            print(adds[i])
            pass
    try:
        wgswb.save(filename)
    except TypeError:
        wgswb.save(filename.replace('.xlsx','.xls'))
    print('good!')


if __name__=='__main__':
    # file = 'c:\\users\\lj\\desktop\\四川行政区.xls'
    # # write_xls1(file, 1, 3, 2, '')
    # write_xls2(file, 1, 3, 1)
    file1 = "c:\\users\\lj\\desktop\\luoma.xls"
    write_xls2(file1, 0, 1, 2)