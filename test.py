from jira import JIRA

# Replace with your Jira credentials and server URL
jira_server = 'https://your-jira-server.com'
jira_username = 'your-username'
jira_password = 'your-password'

# Connect to Jira
jira = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))

# Define JQL to find defects (adjust as needed)
jql = 'project = YOUR_PROJECT AND issuetype = Defect AND status != Closed'

# Search for issues
issues = jira.search_issues(jql)

# Count defects
defect_count = len(issues)

print(f'Total Defects: {defect_count}')
