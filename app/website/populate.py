from models import Event, db, User, Client, Coupon, Recommendation
from main import app

def populate_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create clients
        client_a = Client(client_id=1, schema={"attributes": {"risk": "risk_level", "odds": "probability"}})
        client_b = Client(client_id=2, schema={"attributes": {"risk_level": "danger", "percent": "success_rate"}})

        # Create users
        user1 = User(username="user_1", client=client_a)
        user2 = User(username="user_2", client=client_b)

        # Create coupons
        coupon1 = Coupon(
            coupon_id=101,
            coupon_name="BlackJack_Basic",
            client=client_a,
            attributes={"risk_level": 45, "probability": 75}
        )
        coupon2 = Coupon(
            coupon_id=102,
            coupon_name="BlackJack_Special",
            client=client_b,
            attributes={"danger": 30, "odds": 85}
        )

        # Create recommendations
        rec1 = Recommendation(
            recommendation_set=[
                {"coupon_id": 101, "risk": 45, "odds": 75},
                {"coupon_id": 103, "risk": 50, "odds": 80}
            ],
            user=user1
        )
        rec2 = Recommendation(
            recommendation_set=[
                {"coupon_id": 102, "risk_level": 30, "percent": 85},
                {"coupon_id": 104, "risk_level": 25, "percent": 90}
            ],
            user=user2
        )
        event1 = Event(
            event_id=1,
            event_name="Event 1",
            event_type="Slots",
            event_group="GenZ"
        )
        event2 = Event(
            event_id=2,
            event_name="Event 2",
            event_type="Blackjack",
            event_group="GenX"
        )
        db.session.add_all([client_a, client_b, user1, user2, coupon1, coupon2, rec1, rec2 , event1 , event2])
        db.session.commit()
        print("Database populated successfully!")

if __name__ == "__main__":
    populate_database()