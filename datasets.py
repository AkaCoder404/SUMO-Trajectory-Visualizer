import os
import requests

# Dataset URLs (source)
SOURCE_TDRIVE = "https://www.microsoft.com/en-us/research/publication/t-drive-trajectory-data-sample/"
SOURCE_PORTOCITY = "https://archive.ics.uci.edu/dataset/339/taxi+service+trajectory+prediction+challenge+ecml+pkdd+2015"
SOURCE_GEOLIFE = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=52367"
SOURCE_FOURSQUARE = "https://sites.google.com/site/yangdingqi/home/foursquare-dataset"
SOURCE_SANFRANCISCO = "https://ieee-dataport.org/open-access/crawdad-epflmobility"

# 
TDRIVE = "https://1drv.ms/u/s!AsMG2OU-eID5gXbRS_7fXyftZX1D?e=eSbum2"
PORTOCITY = "https://1drv.ms/u/s!AsMG2OU-eID5gXdT3O-rs-i1votR?e=UmHJFY"
GEOLIFE = "https://www.microsoft.com/en-us/download/details.aspx?id=52367"
GAWALLA = "https://snap.stanford.edu/data/loc-gowalla.html"
TLC = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
TLC_2018 = ""
NYC_BIKE = "https://citibikenyc.com/system-data"


# Baidu Drive (China)
BAIDU_TDRIVE = ""
BAIDU_PORTOCITY = ""
BAIDU_GEOLIFE = ""
BAIDU_FORSQUARE = ""


def check_file_exists(filename):
    return os.path.exists(filename)

def download_file(url, filename):
    print("Downloading file")
    response = requests.get(url)
    print(response)
    
    
def unzip_file(filename):
    pass

class Datasets:
    """
    Class 
    """
    def __init__(self, download_dir="data"):
        self.version = "0.0.1"
        self.download_dir = download_dir
        
        # Make sure download directory exists
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        
    def load(self, dataset):
        if dataset == "tdrive":
            return self.get_tdrive()

    def get_tdrive(self):
        """
        Download and extract T-Drive dataset
        File: x.txt
        Each line in x.txt represents a trajectory of a single taxi.
        Columns:
            Taxi ID
            Timestamp
            Longitude
            Latitude
            
        Separator: space
        """
            
    def get_portocity(self):
        """
        Download and extract Porto City dataset
        Columns:
            TRIP_ID: Trip ID
            CALL_TYPE: Type of call
                C: Central call
                B: Stand call
                A: Street hail
            ORIGIN_CALL: Origin call
            ORIGIN_STAND: Origin stand
            TAXI_ID: Taxi ID
            TIMESTAMP: Timestamp
            DAY_TYPE: Day type
                A: Otherwise (i.e. a normal day, workday or weekend).
                B: If this trip started on a holiday or any other special day (i.e. extending holidays, floating holidays, etc.).
                C: If the trip started on a day before a type-B day;
            MISSING_DATA: Missing data
                TRUE: Missing data
                FALSE: Data is present
            POLYLINE: Polyline of the route, represented as a list of coordinates, 15s apart
                String: [[lon, lat], [lon, lat], ...]
                
        Map boundaries:
            Northwest corner: 41.167, -8.700
            Southeast corner: 41.092, -8.583
        """
            
    
        