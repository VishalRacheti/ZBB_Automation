import requests
from requests.auth import HTTPBasicAuth
import json

# Replace these variables with your Jira server details and credentials
jira_server = 'https://gpatil614.atlassian.net'
username = 'gpatil614@gmail.com'
api_token = 'ATATT3xFfGF0-nQUhSWBs31sn9Z2TbAOjmPqaR5idu66vytJpjxoABQFunVuUj2W28Vb7I4qIyfaGYtsxgTCJq4-wjTyVx80o10mGli-qGlPxoqrX8a5Y2TWckW74x7KDjOCi7wNBOB7l6C_k_44zqj3dtwGjGlDzlDElmVM5X81RRzLT8iZius=413BDE41'

# Replace this JQL query with the one that suits your needs
project_key = 'SCRUM'
year = 2025
month = 2  # February
jql_query = f'project = SCRUM AND type = Bug AND created >= "{year}-{month:02d}-01" AND created <= "{year}-{month:02d}-28"'

# Create the API endpoint URL
url = f'{jira_server}/rest/api/2/search'

# Set up the query parameters
query_params = {
    'jql': jql_query,
    'maxResults': 0  # Set maxResults to 0 to get only the total count
}

# Set up the headers for the request
headers = {
    'Content-Type': 'application/json'
}


response = requests.get(url, headers=headers, params=query_params, auth=HTTPBasicAuth(username, api_token))


if response.status_code == 200:
    response_data = response.json()
    defect_count = response_data['total']
    print(f'Total number of TestCases for {project_key} in {month}/{year}: {defect_count}')
    print(f'Total number of defects for {project_key} in Feb /{year}: {defect_count}')
else:
    print(f'Failed to fetch data. Status code: {response.status_code}, Response: {response.text}')
