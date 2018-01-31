#######
# Date created: 01/30/2018
# Using Socrata v2.1 and sodapy-1.4.5
#######

# sodapy: https://github.com/xmunoz/sodapy
# sodapy depends heavily on requests to make its calls.
# sodapy_credentials used to store app and secret tokens
from sodapy import Socrata
from socrata_credentials import app_token

# How to instantiate client: https://github.com/Mohitsharma44/talk_cusp_api/blob/master/wifi_hotspots.ipynb
# Username and password can also be provided as arguments if the app requires authentication.
client = Socrata(domain = "data.cityofnewyork.us", app_token = app_token)

# QUERY 1
# Do NOT follow the method applied in the above github code. sodapy automatically appends certain words to the URL in the GET method. This MAY or MAY NOT be true for other domains.
# The API endpoint for this data is: https://data.cityofnewyork.us/resource/xtra-f75s.json  Use only the identifier before '.json' here
# The HTTP query is: GET https://data.cityofnewyork.us/resource/xtra-f75s.json?$$app_token=YOUR_APP_TOKEN
# Since the client is created with the app token, it need not be passed here again.
# Content_type can be modified for other types of data formats (geo-json, csv, xml)
driver_data = client.get("xtra-f75s", content_type = "json", limit = 10)
print(driver_data)

# QUERY 2
# The API endpoint for this data is: https://data.cityofnewyork.us/resource/qiz3-axqb.json
# The HTTP query is: GET https://data.cityofnewyork.us/resource/qiz3-axqb.json?$$app_token=YOUR_APP_TOKEN&borough=QUEENS&$where=number_of_persons_injured > 3&$order=number_of_persons_injured
# Data columns can be directly used as arguments. The same goes for SoQL queries.
collision_data = client.get("qiz3-axqb", borough = "QUEENS", where = "number_of_persons_injured > 3", order = "number_of_persons_injured", limit = 10)
print(collision_data)

# QUERY 3
# The api endpoint for this data is: https://data.cityofnewyork.us/resource/fhrw-4uyv.json
# The HTTP query is: GET https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$$app_token=YOUR_APP_TOKEN&$select=created_date,complaint_type,descriptor,incident_address,borough&$where=created_date between '2017-12-31T20:00:00' and '2017-12-31T23:59:59'
# Functions can be passed under the SoQL query as argument
complaints_data = client.get("fhrw-4uyv", select="created_date, complaint_type, descriptor, incident_address, borough", where = "created_date between '2017-12-31T20:00:00' and '2017-12-31T23:59:59'", limit = 10)
print(complaints_data)

# QUERY 4
# Aggregating data from above query based on complaint type.
data = client.get("fhrw-4uyv", select="complaint_type, COUNT(complaint_type)", where = "created_date between '2017-12-31T20:00:00' and '2017-12-31T23:59:59'", group = "complaint_type")
print(data)

# Not closing the client doesn't throw an error, but it is recommended.
client.close()