
# coding: utf-8

# ### Fetching list of members from a slack channel

# ### References : 
# * [Here](https://hackernoon.com/how-to-create-a-slack-bot-that-messages-all-members-of-a-workspace-in-8-minutes-32a5b52838be)

from slackclient import SlackClient
import pandas as pd

SLACK_BOT_TOKEN = 'xxxx'
slack_client = SlackClient(SLACK_BOT_TOKEN)

users = slack_client.api_call("users.list",channel="#yyy")
df = pd.DataFrame(columns=['id','name','email','phone'])

row = []
i = 0
for u in users['members']:
    row.append(u['id'])
    row.append(u['profile']['display_name'])
    if 'email' in u['profile']:
        row.append(u['profile']['email'])
    else:
        row.append('n/a')
    if 'phone' in u['profile']:
        row.append(u['profile']['phone'])
    else:
        row.append('n/a')
    df.loc[i] = row
    i+=1
    print(row)
    row = []

df.to_csv('users_list.csv',index=False)