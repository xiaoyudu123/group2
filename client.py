import requests

def get_data_from_server():
    url = 'http://localhost:5000/data'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Received data from server:")
        print(f"Data: {data['data']}")
    else:
        print("Failed to retrieve data")

if __name__ == '__main__':
    get_data_from_server()
