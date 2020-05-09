import requests

url = 'https://notify-api.line.me/api/notify'
token = 'cGeGSZTb9DnXt6NezCaIgWISaE0sGEeurDJsEWwKlqx'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'This is Line Notify !'
r = requests.post(url, headers=headers , data = {'message':msg})
print(r.text)