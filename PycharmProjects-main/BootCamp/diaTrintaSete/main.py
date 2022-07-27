import requests as re
import datetime as dt
USERNAME = "douglaslusan"
TOKEN = "hd8oas7tdgoh3o74er"
pixela_ENDPOINT = "https://pixe.la/v1/users"
graph_id = "graph1"

today = dt.datetime.now()



user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}
# response = re.post(url=pixela_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
	"id":graph_id,
	"name":"Developing Graph",
	"unit":"hour",
	"type":"int",
	"color":"ajisai",
}

headers = {
	"X-USER-TOKEN": TOKEN
}

# response = re.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

pixel_data = {
	"date": today.strftime("%Y%m%d"),
	"quantity": "2",
}

# response = re.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
