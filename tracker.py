import socket
import requests

def get_location_by_ip(ip):
    try:

        url = f"http://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()
        
        if 'loc' in data:
            loc = data['loc'].split(',')
            latitude, longitude = loc[0], loc[1]
            print(f"IP: {ip}")
            print(f"Location: Latitude: {latitude}, Longitude: {longitude}")
            print(f"City: {data.get('city', 'N/A')}, Region: {data.get('region', 'N/A')}, Country: {data.get('country', 'N/A')}")
        else:
            print("Location data not found.")
    except Exception as e:
        print(f"Error: {e}")

def get_ip_address():
  
    ip = requests.get('https://api.ipify.org').text  
    return ip

ip = get_ip_address()
print(f"Your public IP address: {ip}")
get_location_by_ip(ip)
