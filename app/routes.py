from flask import request, jsonify, session, current_app as app, make_response
from flask_bcrypt import Bcrypt
from flask_session import Session
from app import db
from app.models import Event, User, Attendance, get_uuid

bcrypt = Bcrypt(app)
server_session = Session(app)


@app.route('/@me', methods=['GET'])
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"})

    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route('/register', methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 401

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(id=get_uuid(), name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })


@app.route('/login', methods=['POST'])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route('/logout', methods=['POST'])
def logout_user():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200


@app.route('/event', methods=['POST'])
def create_event():
    data = request.json
    image = data.get('image')
    name = data.get('name')
    location = data.get('location')
    description = data.get('description')
    price = data.get('price')
    date = data.get('date')
    time = data.get('time')

    event = Event(image=image, name=name, location=location, price=price, date=date, time=time,
                  description=description)
    db.session.add(event)
    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "Added event successfully",
        "data": event.to_dict()
    }), 201


@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_data = [event.to_dict() for event in events]
    return jsonify({
        "status": "Success",
        "message": "Events fetched successfully",
        "data": events_data
    })


@app.route('/events/<int:id>', methods=['GET'])
def get_event_detail(id):
    event = Event.query.filter_by(id=id).first()
    print(event)
    if event:
        event_dict = event.to_dict()
        response = make_response(jsonify(event_dict), 200)
        return response

    return jsonify({'error': 'Event not found'}), 404

    # return jsonify({'data': event}), 200


@app.route('/attendances', methods=['POST'])
def create_attendance():
    data = request.get_json()
    eventid = data['eventid']
    userid = data['userid']
    attendance = data['attendance']

    # Check if the attendance already exists
    existing_attendance = Attendance.query.filter_by(eventid=eventid, userid=userid).first()
    if existing_attendance:
        return jsonify({"error": "Already attending this event"}), 400

    new_attendance = Attendance(
        eventid=eventid,
        userid=userid,
        attendance=attendance
    )
    db.session.add(new_attendance)
    db.session.commit()

    attendance_dict = new_attendance.to_dict()
    return jsonify({
        "status": "Success",
        "message": "Added attendance successfully",
        "data": attendance_dict
    }), 201


@app.route('/attendances', methods=['GET'])
def get_attendances():
    attendances = Attendance.query.all()
    attendances_data = [attendance.to_dict() for attendance in attendances]
    return jsonify({
        "status": "Success",
        "message": "Attendances fetched successfully",
        "data": attendances_data
    })
