# Flask-RAT-Simulator

## Overview
This Flask application captures user information when they access the root endpoint and provides various functionalities related to user data.

## Features
- Capture user information (IP address, user agent)
- Fetch SMS messages, call logs, GPS location, and browsing history
- Log incoming and outgoing calls
- Mock access to camera and audio recording

## Installation
1. Clone the repository: https://github.com/johnbosco-anto/Flask-RAT-Simulator

2. Navigate to the project directory : cd flask-user-data-capture

3. Install dependencies : pip install -r requirements.txt


## Usage
1. Run the application: python app.py

2. Access the application in your browser at `http://localhost:5000/`.

## API Endpoints
- `GET /`: Capture user information
- `GET /fetch_sms`: Retrieve SMS messages
- `GET /fetch_call_logs`: Retrieve call logs
- `GET /fetch_location`: Retrieve GPS location
- `POST /incoming_call_notification`: Log incoming calls
- `POST /outgoing_call_notification`: Log outgoing calls




