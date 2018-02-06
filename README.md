# socrataAPI
API Documentation: https://dev.socrata.com/consumers/getting-started.html 

sodapy: https://github.com/xmunoz/sodapy

The [Socrata Open Data API](https://dev.socrata.com/) (SODA) is used to access goverment data from across the US and other countries. It also has data related to NGOs and non-profits. The entire list of regions that you can find data on, using Socrata API, can be found under the "Geographical Regions" [here](https://www.opendatanetwork.com/). The NYC Open Data is entirely on Socrata, and Socrata maintains that it has multiple other open data sets, so if you need to work with government data, Socrata could be one of the starting points for it.

SODA is a RESTful API, and uses HTTP methods to work with data. More information on these HTTP words (GET, POST, PUT, DELETE) [here](https://dev.socrata.com/docs/verbs.html).

The Socrata API can process requests without an application token, but according to its documentation, these will be throttled (blocked) often. On the other hand, registering for an application (and receiving an application/secret key) [here](https://opendata.socrata.com/login) allows upto 1000 requests per rolling hour. They can increase this limit upon request. More information on Application tokens and sample code [here](https://dev.socrata.com/docs/app-tokens.html). The response code if your request is throttled is 429. 

The Socrata API uses SoQL as it’s querying language, and though it is very similar to SQL, more details on the clauses can be found [here](https://dev.socrata.com/docs/queries/). The Socrata API documentation is pretty thorough, and all the NYC Open Data has an API endpoint that can be used with it. The [API endpoint](https://dev.socrata.com/docs/endpoints.html) is different for each dataset, and this is what uniquely identifies each dataset to Socrata. Our various filters and parameters can be applied to the endpoint to get back the necessary data from the complete dataset.

Below, I query the Socrata API, with explanations for each query. The Python queries for each of these are made using the sodapy Python wrapper. You can find SDKs for other programming languages [here](https://dev.socrata.com/libraries/).

### Query 1

Dataset: [New Driver Application Status](https://data.cityofnewyork.us/Transportation/New-Driver-Application-Status/dpec-ucu7)

Query: GET https&#58;<i></i>//data.cityofnewyork.us/resource/xtra-f75s.json?$$app_token=YOUR_APP_TOKEN

Response: 
```json
{
"app_date": "2018-01-17T00:00:00.000",
"app_no": "5845489",
"defensive_driving": "Needed",
"driver_exam": "Needed",
"drug_test": "Needed",
"fru_interview_scheduled": "Not Applicable",
"lastupdate": "2018-01-30T12:00:21.000",
"medical_clearance_form": "Needed",
"other_requirements": "Fingerprints needed", 
"status": "Incomplete", 
"type": "HDR", 
"wav_course": "Needed"
}
```

### Query 2

Dataset: [NYPD Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95)

Query: GET https&#58;//<i></i>data\.cityofnewyork.us/resource/qiz3-axqb.json?$$app_token=YOUR_APP_TOKEN&borough=QUEENS&$where=number_of_persons_injured > 3&$order=number_of_persons_injured

Response: 
```json
{"borough": "QUEENS",
"contributing_factor_vehicle_1": "Unspecified",
"contributing_factor_vehicle_2": "Unspecified",
"contributing_factor_vehicle_3": "Unspecified",
"date": "2018-01-23T00:00:00.000",
"latitude": "40.720535",
"location":
	{"type": "Point",
	"coordinates": [-73.88885,40.720535]
	},
"longitude": "-73.88885",
"number_of_cyclist_injured": "0",
"number_of_cyclist_killed": "0",
"number_of_motorist_injured": "4",
"number_of_motorist_killed": "0",
"number_of_pedestrians_injured": "0",
"number_of_pedestrians_killed": "0",
"number_of_persons_injured": "4",
"number_of_persons_killed": "0",
"off_street_name": "69 LANE",
"on_street_name": "ELIOT AVENUE ", 
"time": "23:19", 
"unique_key": "3833544", 
"vehicle_type_code1": "PASSENGER VEHICLE", 
"vehicle_type_code2": "CONV", 
"vehicle_type_code_3": "SPORT UTILITY / STATION WAGON",
"zip_code": "11379"
}
```

### Query 3

Dataset: [311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

Query: GET https&#58;//<i></i>data\.cityofnewyork.us/resource/fhrw-4uyv.json?$$app_token=YOUR_APP_TOKEN&$select=created_date,complaint_type,descriptor,incident_address,borough&$where=created_date between '2017-12-31T20:00:00' and '2017-12-31T23:59:59' 

Response: 
```json
{
"borough": "MANHATTAN",
"complaint_type": "Noise – Residential", 
"created_date": "2017-12-31T20:00:05.000", 
"descriptor": "Loud Music/Party", 
"incident_address": "191V WEST 151 STREET"
}
