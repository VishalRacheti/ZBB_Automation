from jira import JIRA
from datetime import datetime

jira_server ='https://gpatil614.atlassian.net'
jira_username = 'gpatil614@gmail.com'
jira_api_token = 'ATATT3xFfGF0-nQUhSWBs31sn9Z2TbAOjmPqaR5idu66vytJpjxoABQFunVuUj2W28Vb7I4qIyfaGYtsxgTCJq4-wjTyVx80o10mGli-qGlPxoqrX8a5Y2TWckW74x7KDjOCi7wNBOB7l6C_k_44zqj3dtwGjGlDzlDElmVM5X81RRzLT8iZius=413BDE41'

jira = JIRA(server=jira_server, basic_auth=(jira_username, jira_api_token))

project_key = 'My Scrum Project'



year = 2025
month = 2

start_date = datetime (year, month , 1). strftime ('%Y-%m-%d')
end_date = datetime(year, month + 1, 1) .strftime ('%Y-%m-%d' ) if month < 12 else datetime (year + 1, 1, 1). strftime ('&Y-Sin-%d')


jql = f'project = (project_key) AND created >= "{start_date}" AND created < "{end_date}"'


issues_count = jira.search_issues(jql, maxResults=0).total

print(f"Number of issues created in {datetime(year, month, 1).strftime('%B %Y')} for project {project_key}: {issues_count}")