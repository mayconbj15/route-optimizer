import googlemaps
from datetime import datetime

# TODO: Parametrizar o mode 
# TODO: Parametrizar se vai usar distância ou tempo 
# TODO: Receber a entrada dos destinos da interface 

def create_data(adresses):
    data = []
    for address in adresses:
        data.append(address)
        

    return data

def create_distance_matrix(addresses, unit):
    # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
    max_elements = 100
    num_addresses = len(addresses) # 16 in this example.
    # Maximum number of rows that can be computed per request (6 in this example).
    max_rows = max_elements // num_addresses
    # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
    q, r = divmod(num_addresses, max_rows)
    dest_addresses = addresses
    distance_matrix = []
    
    gmaps = getGMaps()
   
    # Send q requests, returning max_rows rows per request.
    for i in range(q):
        origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
        response = send_request(gmaps, origin_addresses, dest_addresses)
        distance_matrix += build_distance_matrix(response, unit)

    # Get the remaining remaining r rows, if necessary.
    if r > 0:
        origin_addresses = addresses[q * max_rows: q * max_rows + r]
        response = send_request(gmaps, origin_addresses, dest_addresses)
        distance_matrix += build_distance_matrix(response, unit)
    
    return distance_matrix

def build_distance_matrix(response, unit):
    distance_matrix = []
    for row in response['rows']:
        row_list = [row['elements'][j][unit]['value'] for j in range(len(row['elements']))]
        distance_matrix.append(row_list)
    return distance_matrix

def getGMaps():
    with open('apikey.txt') as f:
        api_key = f.readline()
        f.close

    return googlemaps.Client(key=api_key)
                    

def send_request(gmaps, origin_addresses, dest_addresses):
    now = datetime.now()
    directions_result = gmaps.distance_matrix(origins=origin_addresses,
                                        destinations=dest_addresses,
                                        mode="driving",
                                        departure_time=now)
    
    return directions_result

def main(adresses, unit):
    """Entry point of the program"""
    # Create the data.
    #print(unit)
    data = create_data(adresses)
    distance_matrix = create_distance_matrix(data, unit)
    #print(distance_matrix)

    return distance_matrix


if __name__ == '__main__':
  main(None)