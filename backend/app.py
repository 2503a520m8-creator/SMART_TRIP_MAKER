from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def home():
    return {
        "message": "Smart Trip Maker API is running",
        "status": "success"
    }

@app.get('/health')
def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}

@app.post('/api/trips')
def create_trip():
    data = request.get_json(silent=True) or {}

    required_fields = [
        'full_name',
        'email',
        'destination',
        'start_date',
        'end_date',
        'travelers',
        'budget',
        'hotel_preference'
    ]

    missing_fields = [field for field in required_fields if not data.get(field)]
    if missing_fields:
        return jsonify({
            "status": "error",
            "message": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    trip = {
        "full_name": data.get('full_name'),
        "email": data.get('email'),
        "destination": data.get('destination'),
        "start_date": data.get('start_date'),
        "end_date": data.get('end_date'),
        "travelers": int(data.get('travelers')),
        "budget": float(data.get('budget')),
        "hotel_preference": data.get('hotel_preference'),
        "created_at": datetime.utcnow().isoformat() + "Z"
    }

    return jsonify({
        "status": "success",
        "message": "Trip request received successfully",
        "trip": trip
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
