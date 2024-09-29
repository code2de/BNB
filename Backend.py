from flask import Flask, request, jsonify
from datetime import datetime, timedelta
app = Flask(__name__)
resources = {
    'study_rooms': [],
    'lab_equipment': [],
    'sports_facilities': []

def send_notification(user_id, message):
    print(f"Notification to {user_id}: {message}")
@app.route('/availability/<resource_type>', methods=['GET'])
def check_availability(resource_type):
    return jsonify(resources.get(resource_type, []))
@app.route('/reserve', methods=['POST'])
def reserve_resource():
    data = request.json
    resource_type = data['resource_type']
    user_id = data['user_id']
    start_time = datetime.fromisoformat(data['start_time'])
    end_time = datetime.fromisoformat(data['end_time'])
    reservation = {
        'user_id': user_id,
        'start_time': start_time,
        'end_time': end_time
    }
    resources[resource_type].append(reservation)
    send_notification(user_id, f"Reserved {resource_type} from {start_time} to {end_time}.")
    
    return jsonify({'status': 'success', 'reservation': reservation})
@app.route('/reminders', methods=['GET'])
def get_reminders():
    return jsonify({'message': 'No reminders set up yet!'})

if __name__ == '__main__':
    app.run(debug=True)
1
