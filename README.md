# socrataAPI
API Documentation: https://dev.socrata.com/consumers/getting-started.html 

sodapy: https://github.com/xmunoz/sodapy

The [Socrata Open Data API](https://dev.socrata.com/) (SODA) is used to access goverment data from across the US and other countries. It also has data related to NGOs and non-profits. The entire list of regions that you can find data on, using Socrata API, can be found under the "Geographical Regions" [here](https://www.opendatanetwork.com/). The NYC Open Data is entirely on Socrata, and Socrata maintains that it has multiple other open data sets, so if you need to work with government data, Socrata could be one of the starting points for it.

SODA is a RESTful API, and uses HTTP methods to work with data. More information on these HTTP words (GET, POST, PUT, DELETE) [here](https://dev.socrata.com/docs/verbs.html).

The Socrata API can process requests without an application token, but according to its documentation, these will be throttled (blocked) often. On the other hand, registering for an application (and receiving an application/secret key) [here](https://opendata.socrata.com/login) allows upto 1000 requests per rolling hour. They can increase this limit upon request. More information on Application tokens and sample code [here](https://dev.socrata.com/docs/app-tokens.html). The response code if your request is throttled is 429. 

The Socrata API uses SoQL as it’s querying language, and though it is very similar to SQL, more details on the clauses can be found [here](https://dev.socrata.com/docs/queries/). The Socrata API documentation is pretty thorough, and all the NYC Open Data sets have an API endpoint that can be used with it. The [API endpoint](https://dev.socrata.com/docs/endpoints.html) is different for each dataset, and this is what uniquely identifies each dataset to Socrata. Our various filters and parameters can be applied to the endpoint to get back the necessary data from the complete dataset.

Below, I query the Socrata API, with explanations for each query and response. The Python queries for each of these are made using the sodapy Python wrapper. You can find SDKs for other programming languages [here](https://dev.socrata.com/libraries/). 

I used [Hurl.it](https://www.hurl.it/) to test all my queries and look through the responses. If you're going to use the urllib or requests library to run API requests, instead of the sodapy wrapper, this website is a good place to test your HTTP request url before adding it to code.

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
The parameter used here is $$app_token and it’s appended to the API endpoint by adding a ‘?’ before it. The response tells you when the application for a new user was filed, what is the application number, and the details provided or required by the application.

### Query 2

Dataset: [NYPD Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95)

I’ll be using a parameter along with a SoQL query in my URL request to get information on collisions that happened in Queens and the number of people injured was greater than 3.

Query: GET https&#58;//<i></i>data\.cityofnewyork.us/resource/qiz3-axqb.json?$$app_token=YOUR_APP_TOKEN&borough=QUEENS&$where=number_of_persons_injured > 3&$order=number_of_persons_injured

Again, I’m passing my app_token by parameter, and I filter the queries with “borough=QUEENS” in my URL. 

The $where is a SoQL parameter that allows me to add a range to my data. If I were to use “&number_of_persons_injured > 3” without the “$where” I get a '400 Bad Request' as response. Also, if I don’t specify the value of the parameter <i>exactly</i> as given in the data (Queens vs. QUEENS), I again get a '400 Bad Request' response.

I also order this (using SoQL command $order) by the number of people injured, so I get an ascending order of results. However, you can't really see in the example response. 

One thing to note about the SODA API is that spaces are allowed in the query, following a SoQL query. The request will return an error if the spaces (number_of_persons_injured > 3) are omitted.

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
As we can see, there is a lot of meta-data about the location and the type of vehicles involved, which can help us create a mapping based on location, or vehicle based visualization for this data. We can also use date and time to filter this data to observe accidents at night, or on a particular day.

### Query 3

Dataset: [311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

Along the lines of the idea mentioned at the end of the previous query, I’ll be using a range here to display complaints that were lodged between a particular time period: New Years’ Eve, 2017 (31st Dec 2017) between 8:00pm and 11:59pm.

Query: GET https&#58;//<i></i>data\.cityofnewyork.us/resource/fhrw-4uyv.json?$$app_token=YOUR_APP_TOKEN&$select=created_date,complaint_type,descriptor,incident_address,borough&$where=created_date between '2017-12-31T20:00:00' and '2017-12-31T23:59:59' 

I’m using the $select SoQL query to display only certain columns of the data. However, along with the $where SoQL query, I’m adding a SoQL function, “between .. and ..”, to set the range on the time and date for the 311 complaints. A list of all SoQL functions can be found [here](https://dev.socrata.com/docs/functions/#,). The date format used is specified as the floating timestamp and more information about Socrata API datatypes is [here](https://dev.socrata.com/docs/datatypes/#,).

Response: 
```json
{
"borough": "MANHATTAN",
"complaint_type": "Noise – Residential", 
"created_date": "2017-12-31T20:00:05.000", 
"descriptor": "Loud Music/Party", 
"incident_address": "191V WEST 151 STREET"
}
```
Again, this can be combined with $order or location to make different uses of the data. I can choose to group the data according to complaint_type, to see how many types of complaints where registered as well (implemented in the python code as the last query). 
