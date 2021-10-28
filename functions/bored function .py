
def get_activity():
    response = requests.get('https://www.boredapi.com/api/activity')
    json_data = json.loads(response.text)
    activity = json_data['activity']
    return (activity)
