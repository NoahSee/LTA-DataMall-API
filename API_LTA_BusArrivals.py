import requests
import json
import datetime
import pytz

def Unpack_ServiceNoDict (dict):

    ServiceNo   = dict["ServiceNo"]
    ArrivalTime = datetime.datetime.fromisoformat(dict["NextBus"]["EstimatedArrival"]).replace(tzinfo=None)
    CurrentTime = datetime.datetime.now()

    # Determine waiting time in minutes
    WaitingTime = ArrivalTime - CurrentTime
    WaitingTime = round(WaitingTime.seconds/60) if (WaitingTime < datetime.timedelta(minutes=1)) else 0
    print("Bus {} Arriving in {} minutes".format(ServiceNo,WaitingTime))

    return

class BusArrivals:

    def __init__(self, AccountKey=None):
        if not AccountKey: raise Exception("A valid AccountKey is required. Please register with LTA DataMall to obtain one.")
        self.AccountKey = AccountKey

    def GetArrivals (self, BusStopID=None):

        if BusStopID:

            headers = {
                'AccountKey'    : self.AccountKey,
                'accept'        : 'application/json'
            }

            url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={}".format(BusStopID)

            r = requests.get(url, headers = headers)

            if r.status_code == 200:
                print("Printing Arrival Timings for Bus Stop ID {}".format(BusStopID))
                data = r.json()["Services"]
                for i in data:
                    Unpack_ServiceNoDict(i)
                return r

