import requests

url = 'http://localhost:3000/widgets'

response = requests.get('https://raw.githubusercontent.com/IT3038C/IT3038C.github.io/main/examples/week-10-widgets.json')
data = response.json()

widgets = [f"{widget['name']} is {widget['color']}." for widget in data]

print("Widget List:\n" + "\n".join(widgets))
