"""
LTA Bus Arrival API

Notes

    - Register for an AccountKey at https://www.mytransport.sg/content/mytransport/home/dataMall.html

Version History

    v1      API.GetArrvals will return the JSON response and print the next arrival timings

"""

import json
from API_LTA_BusArrivals import BusArrivals

API = BusArrivals( AccountKey = "" ) # Insert your Account Key here

print("Example: Aft Jln Buloh Perindu")

r = API.GetArrivals(BusStopID="93059")

print("Dumping JSON response", json.dumps(r.json(), indent=4, sort_keys=True))

"""

Example response:

Example: Aft Jln Buloh Perindu
Printing Arrival Timings for Bus Stop ID 93059
Bus 10 Arriving in 0 minutes
Bus 12 Arriving in 0 minutes
Bus 14 Arriving in 0 minutes
Bus 155 Arriving in 0 minutes
Bus 32 Arriving in 0 minutes
Bus 40 Arriving in 0 minutes
Dumping JSON response {
    "BusStopCode": "93059",
    "Services": [
        {
            "NextBus": {
                "DestinationCode": "16009",
                "EstimatedArrival": "2018-12-30T19:01:16+08:00",
                "Feature": "WAB",
                "Latitude": "1.3192633333333332",
                "Load": "SEA",
                "Longitude": "103.95515266666666",
                "OriginCode": "75009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "16009",
                "EstimatedArrival": "2018-12-30T19:16:36+08:00",
                "Feature": "",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "75009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "",
                "EstimatedArrival": "",
                "Feature": "",
                "Latitude": "",
                "Load": "",
                "Longitude": "",
                "OriginCode": "",
                "Type": "",
                "VisitNumber": ""
            },
            "Operator": "SBST",
            "ServiceNo": "10"
        },
        {
            "NextBus": {
                "DestinationCode": "10499",
                "EstimatedArrival": "2018-12-30T18:55:52+08:00",
                "Feature": "WAB",
                "Latitude": "1.3196348333333334",
                "Load": "SEA",
                "Longitude": "103.9357105",
                "OriginCode": "77009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "10499",
                "EstimatedArrival": "2018-12-30T19:13:19+08:00",
                "Feature": "WAB",
                "Latitude": "1.3478124999999999",
                "Load": "SEA",
                "Longitude": "103.95771083333334",
                "OriginCode": "77009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "10499",
                "EstimatedArrival": "2018-12-30T19:22:20+08:00",
                "Feature": "WAB",
                "Latitude": "1.363617",
                "Load": "SEA",
                "Longitude": "103.96415",
                "OriginCode": "77009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "GAS",
            "ServiceNo": "12"
        },
        {
            "NextBus": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2018-12-30T18:58:14+08:00",
                "Feature": "WAB",
                "Latitude": "1.3169703333333334",
                "Load": "SEA",
                "Longitude": "103.94773266666667",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2018-12-30T19:10:20+08:00",
                "Feature": "WAB",
                "Latitude": "1.3264181666666666",
                "Load": "SEA",
                "Longitude": "103.9403665",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2018-12-30T19:24:37+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "14"
        },
        {
            "NextBus": {
                "DestinationCode": "52009",
                "EstimatedArrival": "2018-12-30T18:52:30+08:00",
                "Feature": "WAB",
                "Latitude": "1.3107425",
                "Load": "SEA",
                "Longitude": "103.93279216666667",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "52009",
                "EstimatedArrival": "2018-12-30T19:05:20+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "52009",
                "EstimatedArrival": "2018-12-30T19:22:20+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "155"
        },
        {
            "NextBus": {
                "DestinationCode": "11379",
                "EstimatedArrival": "2018-12-30T18:53:00+08:00",
                "Feature": "WAB",
                "Latitude": "1.3207955",
                "Load": "SEA",
                "Longitude": "103.9178895",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "11379",
                "EstimatedArrival": "2018-12-30T18:59:25+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "11379",
                "EstimatedArrival": "2018-12-30T19:13:35+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "32"
        },
        {
            "NextBus": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2018-12-30T18:50:00+08:00",
                "Feature": "WAB",
                "Latitude": "1.3141648333333333",
                "Load": "SEA",
                "Longitude": "103.92295433333334",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2018-12-30T19:08:58+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2018-12-30T19:25:58+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "40"
        }
    ],
    "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusArrivalv2/@Element"
}

"""