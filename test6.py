import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

# Replace these variables with your Jira server details and credentials
jira_server = 'https://gpatil614.atlassian.net'
username = 'gpatil614@gmail.com'
api_token = 'ATATT3xFfGF0-nQUhSWBs31sn9Z2TbAOjmPqaR5idu66vytJpjxoABQFunVuUj2W28Vb7I4qIyfaGYtsxgTCJq4-wjTyVx80o10mGli-qGlPxoqrX8a5Y2TWckW74x7KDjOCi7wNBOB7l6C_k_44zqj3dtwGjGlDzlDElmVM5X81RRzLT8iZius=413BDE41'

# Define the list of projects you want to check
projects = ['SCRUM', 'VP']  # Replace with your project keys

# Define the year and month you want to check
year = 2025
month = 2  # February

# Initialize an empty list to store the results
results = []

for project_key in projects:
    # Create the JQL query
    jql_query = f'project = {project_key} AND issuetype = Bug AND created >= "{year}-{month:02d}-01" AND created <= "{year}-{month:02d}-28"'

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

    # Make the request to the Jira API
    response = requests.get(url, headers=headers, params=query_params, auth=HTTPBasicAuth(username, api_token))

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        defect_count = response_data['total']
        print(f'Total number of defects for {project_key} in {month}/{year}: {defect_count}')

        # Add the result to the list
        results.append({
            'Project': project_key,
            'Month': month,
            'Year': year,
            'Defect Count': defect_count
        })
    else:
        print(f'Failed to fetch data for {project_key}. Status code: {response.status_code}, Response: {response.text}')

# Store the results in an Excel file
df = pd.DataFrame(results)
excel_filename = f'defect_count_multiple_projects_{year}_{month:02d}.xlsx'
df.to_excel(excel_filename, index=False)
print(f'Data saved to {excel_filename}')
