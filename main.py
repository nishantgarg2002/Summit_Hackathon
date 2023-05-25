import csv

# Function to read user data from CSV file
def read_user_data(file_path):
    user_data = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data[row['id']] = {
                'password': row['password'],
                'country': row['country'],
                'device': row['device'],
                'ip': row['ip']
            }
    return user_data

# Function to write user data to CSV file
def write_user_data(file_path, user_data):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'password', 'country', 'device', 'ip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for id, data in user_data.items():
            writer.writerow({'id': id, 'password': data['password'], 'country': data['country'], 'device': data['device'], 'ip': data['ip']})

# Function to authenticate user
def authenticate_user(user_data, id, password, country, device, ip):
    if id not in user_data or user_data[id]['password'] != password:
        # Invalid id or password
        print("Access denied")
        # Send message to account owner for login denied
        send_message(id, "Login denied")
    else:
        # User is authenticated
        if country != user_data[id]['country']:
            # Suspicious activity - Login from a new country
            print("Anomaly detected: Suspicious activity - Login from a new country")
            # Send message to the user for suspicious activity
            send_message(id, "Suspicious activity: Login from a new country")
        elif device != user_data[id]['device']:
            # Suspicious activity - Login from a new device
            print("Anomaly detected: Suspicious activity - Login from a new device")
            # Send message to the user for suspicious activity
            send_message(id, "Suspicious activity: Login from a new device")
        elif ip != user_data[id]['ip']:
            # Suspicious activity - Login from a new IP
            print("Anomaly detected: Suspicious activity - Login from a new IP")
            # Send message to the user for suspicious activity
            send_message(id, "Suspicious activity: Login from a new IP")
        else:
            # Session authenticated
            print("Session authenticated")
            # Update user's session data
            user_data[id]['country'] = country
            user_data[id]['device'] = device
            user_data[id]['ip'] = ip
            # Save updated user data to the CSV file
            write_user_data('user_data.csv', user_data)
            # User can continue with their session and make transactions

# Function to send message
def send_message(id, message):
    # Code to send message to the account owner or user
    print("Message sent to", id, ":", message)

# Test the functionality
user_data = read_user_data('user_data.csv')
