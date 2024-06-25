# seedy.py
from datetime import datetime

from app import db, create_app as app
from app.models import User, Event, Attendance

# Create the database tables
# db.create_all()

# Seed data
if __name__ == '__main__':
    with app().app_context():
        print("Clearing db...")
        Attendance.query.delete()
        Event.query.delete()
        User.query.delete()

        # users = [
        #     User(name='alice', email='alice@gmail.com', password='password123'),
        #     User(name='bob', email='bob@gmail.com', password='password123'),
        #     User(name='charlie', email='charlie@gmail.com', password='password123'),
        #     User(name='dave', email='dave@gmail.com', password='password123')
        # ]
        #
        # db.session.add_all(users)
        # db.session.commit()

        events = [
            Event(

                name="Music Concert",
                description="A great music concert featuring famous bands.",
                date=datetime.strptime("2024-06-20T19:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="7:00 PM",
                image="https://images.unsplash.com/photo-1506157786151-b8491531f063?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bXVzaWMlMjBmZXN0aXZhbHxlbnwwfHwwfHx8MA%3D%3D",
                location="New York",

                price=2000
            ),
            Event(

                name="Art Exhibition",
                description="Exhibition showcasing local artists.",
                date=datetime.strptime("2024-06-25T10:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="10:00 AM",
                image="https://images.unsplash.com/photo-1685304120514-3ae627e4845f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGFydCUyMGV4aGliaXRpb25zJTIwaW4lMjB1c2F8ZW58MHx8MHx8fDA%3D",
                location="Paris",

                price=1000
            ),
            Event(

                name="Food Festival",
                description="A festival with various food stalls.",
                date=datetime.strptime("2024-07-01T12:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="12:00 PM",
                image="https://images.unsplash.com/photo-1629642621587-9947ce328799?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZvb2QlMjBkaXNwbGF5JTIwaW4lMjBqYXBhbnxlbnwwfHwwfHx8MA%3D%3D",
                location="Tokyo",

                price=4000
            ),
            Event(

                name="Tech Conference",
                description="A conference with tech talks and workshops.",
                date=datetime.strptime("2024-07-05T09:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="9:00 AM",
                image="https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGRldmVsb3BlciUyMCUyMGNvbmZlcmVuY2UlMjBpbiUyMHNpbGljb25lJTIwdmFsbGV5fGVufDB8fDB8fHww",
                location="San Francisco",

                price=100
            ),
            Event(

                name="Book Fair",
                description="A fair with a variety of books for sale.",
                date=datetime.strptime("2024-07-10T11:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="11:00 AM",
                image="https://images.unsplash.com/photo-1491841573634-28140fc7ced7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGxvbmRvbiUyMEJvb2slMjBGYWlyfGVufDB8fDB8fHww",
                location="London",

                price=3000
            ),
            Event(

                name="Film Festival",
                description="A festival showcasing independent films.",
                date=datetime.strptime("2024-07-15T18:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="6:00 PM",
                image="https://images.unsplash.com/photo-1503638454472-b9c1ed258357?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGZpbG0lMjBmZXN0aXZhbCUyMGluJTIwY2FuYWRhfGVufDB8fDB8fHww",
                location="Los Angeles",

                price=5000
            ),
            Event(

                name="Marathon",
                description="A marathon event for charity.",
                date=datetime.strptime("2024-07-20T06:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="6:00 AM",
                image="https://images.unsplash.com/photo-1596727362302-b8d891c42ab8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bG9uZG9uJTIwbWFyYXRob258ZW58MHx8MHx8fDA%3D",
                location="Berlin",

                price=400
            ),
            Event(

                name="Science Fair",
                description="A fair showcasing science projects by students.",
                date=datetime.strptime("2024-07-25T10:00:00Z", '%Y-%m-%dT%H:%M:%SZ'),
                time="10:00 AM",
                image="https://images.unsplash.com/photo-1554475900-0a0350e3fc7b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8U2NpZW5jZXxlbnwwfHwwfHx8MA%3D%3D",
                location="Toronto",

                price=2000
            )
        ]
        db.session.add_all(events)
        db.session.commit()

print("Database seeded successfully.")
