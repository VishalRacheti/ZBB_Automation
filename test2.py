import requests
from requests.auth import HTTPBasicAuth
import json

# Replace with your Jira credentials and server URL
jira_server = 'https://gpatil614.atlassian.net'
jira_username = 'gpatil614@gmail.com'
jira_token = 'ATATT3xFfGF0-nQUhSWBs31sn9Z2TbAOjmPqaR5idu66vytJpjxoABQFunVuUj2W28Vb7I4qIyfaGYtsxgTCJq4-wjTyVx80o10mGli-qGlPxoqrX8a5Y2TWckW74x7KDjOCi7wNBOB7l6C_k_44zqj3dtwGjGlDzlDElmVM5X81RRzLT8iZius=413BDE41'  # You might need an API token instead of a password

# Jira JQL query to find defects
jql = 'project = SCRUM AND type = Bug'

# Jira REST API endpoint
search_url = f'{jira_server}/rest/api/2/search'

# Headers for the HTTP request
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Payload with the JQL query
payload = json.dumps({
    'jql': jql,
    'fields': ['id']  # We only need the issue ids
})

# Make the HTTP request
response = requests.post(
    search_url,
    headers=headers,
    data=payload,
    auth=HTTPBasicAuth(jira_username, jira_token)
)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    defect_count = len(result['issues'])
    print(f'Total Defects: {defect_count}')
else:
    print(f'Failed to fetch defects. Status code: {response.status_code}, Response: {response.text}')
