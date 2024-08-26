from flask import Flask, request, jsonify
import uuid  # Import uuid for generating unique identifiers

app = Flask(__name__)

# Store user information and data in memory
user_data = []
sms_messages = []
call_logs = []
gps_location = {"latitude": 0.0, "longitude": 0.0}
calendar_events = []
stored_files = []
browsing_history = []
social_media_status = {"whatsapp": False, "facebook": False, "instagram": False}

@app.route('/')
def index():
    # Capture user information
    user_info = {
        'username': str(uuid.uuid4()),  # Generate a unique username
        'ip_address': request.remote_addr,  # User's IP address
        'user_agent': request.user_agent.string  # User's browser user agent
    }
    
    # Store the information
    user_data.append(user_info)
    
    # Optionally return a message or JSON response
    return jsonify({'message': 'User information captured', 'data': user_info})

@app.route('/fetch_sms', methods=['GET'])
def fetch_sms():
    return jsonify(sms_messages)

@app.route('/fetch_call_logs', methods=['GET'])
def fetch_call_logs():
    return jsonify(call_logs)

@app.route('/fetch_location', methods=['GET'])
def fetch_location():
    return jsonify(gps_location)

@app.route('/access_camera', methods=['GET'])
def access_camera():
    return jsonify({'message': 'Camera access initiated (mockup)'})

@app.route('/record_audio', methods=['GET'])
def record_audio():
    return jsonify({'message': 'Audio recording initiated (mockup)'})

@app.route('/incoming_call_notification', methods=['POST'])
def incoming_call_notification():
    data = request.get_json()
    call_logs.append({'type': 'incoming', 'number': data.get('number')})
    return jsonify({'message': 'Incoming call logged'})

@app.route('/outgoing_call_notification', methods=['POST'])
def outgoing_call_notification():
    data = request.get_json()
    call_logs.append({'type': 'outgoing', 'number': data.get('number')})
    return jsonify({'message': 'Outgoing call logged'})

@app.route('/fetch_calendar', methods=['GET'])
def fetch_calendar():
    return jsonify(calendar_events)

@app.route('/fetch_files', methods=['GET'])
def fetch_files():
    return jsonify(stored_files)

@app.route('/access_social_media', methods=['GET'])
def access_social_media():
    return jsonify(social_media_status)

@app.route('/fetch_browsing_history', methods=['GET'])
def fetch_browsing_history():
    return jsonify(browsing_history)

@app.route('/screenshot', methods=['GET'])
def screenshot():
    return jsonify({'message': 'Screenshot taken (mockup)'})

@app.route('/screen_record', methods=['GET'])
def screen_record():
    return jsonify({'message': 'Screen recording initiated (mockup)'})

@app.route('/fetch_user_data', methods=['GET'])
def fetch_user_data():
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
