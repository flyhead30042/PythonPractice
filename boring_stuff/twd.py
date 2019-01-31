import pyproj
from pyproj import Proj
import gpxpy
import gpxpy.gpx
from gpxpy.gpx import GPXWaypoint
import os.path
import pandas as pd
import numpy as np

# crs_twd67 = Proj("+proj=tmerc +lat_0=0 +lon_0=121 +k=0.9999 +x_0=250000 +y_0=0 +ellps=aust_SA +units=m +no_defs")
crs_twd67 = Proj("+proj=tmerc +ellps=GRS67 +towgs84=-752,-358,-179,-.0000011698,.0000018398,.0000009822,.00002329 +lon_0=121 +x_0=250000 +k=0.9999 +to +proj=tmerc +datum=WGS84 +lon_0=121 +x_0=250000 +k=0.9999")
crs_twd97 = Proj("+proj=tmerc +lat_0=0 +lon_0=121 +k=0.9999 +x_0=250000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")
crs_wgs84 = Proj("+proj=longlat +datum=WGS84 +no_defs")
crs_google900913 = Proj("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs")


''' Normalize the point to 13 digits'''
def normalize(x, y):
    if Normalization.prefix_x != None and len(Normalization.prefix_x) >0:
        x = Normalization.prefix_x + x
    if Normalization.post_x != None and len(Normalization.post_x) >0:
        x = x + Normalization.post_x
    if Normalization.prefix_y != None and len(Normalization.prefix_y) >0:
        y = Normalization.prefix_y + y
    if Normalization.post_y != None and len(Normalization.post_y) >0:
        y = y + Normalization.post_y
    return x, y


'''
    _crs: coordination system including twd67, twd97, wgs84
    _point_file: source point file, CSV format supporting column of x, y, name  
    to_gpx(): read point file, convert to wgs84 and generate gpx file
'''
class _twd(object):
    def __init__(self, _crs, _point_file):
        self.crs = _crs
        self.point_file = _point_file


    def to_gpx(self):
        if self.point_file != None and os.path.isfile(self.point_file):
            st = os.stat(self.point_file)
            print("{0:s}, size {1:d}".format(self.point_file, st.st_size))

            df = pd.read_csv(self.point_file, sep=",", header = None, names=["x", "y", "name"], dtype={"x":np.object, "y":np.object, "name":np.object})
            #
            # with open(self.point_file, "r", encoding='utf8') as f:
            #     rows = list(csv.reader(f))

            gpx = gpxpy.gpx.GPX()

            for index, r in df.iterrows():
                if len(r) != 0:
                    x1, y1, name = r['x'].strip(), r['y'].strip(), r['name'].strip()
                    print("x1={},y1={}, name={}".format(x1, y1, name))

                    x1, y1 = normalize(x1, y1)
                    print("{},{}, name={}".format(x1, y1, name))

                    '''
                        In fact, the ll supported by all GPS tool (ex. Map Generation Tool) is based wgs84 rather than twd67
                        Can't correctly shows the ll if only change change coordination format
                    '''
                    x3, y3  = pyproj.transform(crs_twd67, crs_wgs84, x1, y1)
                    print("{:5.8f},{:5.8f}, name={}".format(y3, x3, name))

                    # wp = GPXWaypoint(longitude=x3, latitude=y3, name=name, elevation="0.0", time=datetime.now(),
                    #                  symbol="Waypoint")

                    wp = GPXWaypoint(longitude=x3, latitude=y3, name=name, elevation="0.0", time=np.datetime64("now").astype(object),
                                     symbol="Waypoint")
                    gpx.waypoints.append(wp)

            # print(gpx.to_xml())

            name = os.path.splitext(self.point_file)[0] + ".gpx"  # rename the source file with .gpx extension
            path = os.path.abspath(self.point_file)
            gpx_file = os.path.join(path, name)

            print("writing xml to {}".format(gpx_file))
            with open(gpx_file, "w+", encoding='utf8') as f:
                f.write(gpx.to_xml(version="1.1"))
            print("done")


class twd67(_twd):
    def __init__(self, file):
        _twd.__init__(self, crs_twd67, file)

class twd97(_twd):
    def __init__(self, file):
        _twd.__init__(self, crs_twd97, file)


'''
    A static class indicating the prefix and postfix
    Note don't remove anyone of attributes. Assign "" or None if they are not needed
'''
class Normalization(object):
    prefix_x = "3"
    prefix_y = "27"
    post_x = "50"
    post_y = "50"


if __name__ == "__main__":
    f_name= "D:/workspace/citest\PythonPractice\data/tw67_to_gpx/finalexame.csv"
    twd = twd67(f_name)
    twd.to_gpx()



