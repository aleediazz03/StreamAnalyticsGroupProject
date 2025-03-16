import random
import time
from fastavro import writer, parse_schema

#############################################
########### DRIVER EVENT FUNCTION ###########
#############################################
def generate_driver_event(fake):
    status = random.choice(["AVAILABLE", "ACCEPTED", "ONGOING", "COMPLETED"])

    # Assign ride_id only if the driver is not available
    ride_id = None if status == "AVAILABLE" else fake.uuid4()

    # Optional fields; using random.choice to sometimes return None.
    gender = random.choice([None, "Male", "Female"])
    age = random.choice([None, random.randint(20, 70)])
    rating = random.choice([None, round(random.uniform(3.0, 5.0), 2)])

    event = {
        "driver_id": fake.uuid4(),
        "gender": gender,
        "age": age,
        "rating": rating,
        "ride_id": ride_id,
        "timestamp": int(time.time() * 1000),
        "vehicle": random.choice(["STANDARD", "SHARED", "VAN", "PREMIUM"]),
        "location": {
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude())
        },
        "status": status
    }
    return event


################################################
########### PASSENGER EVENT FUNCTION ###########
################################################
def generate_passenger_event(fake):

    # Optional fields; using random.choice to sometimes return None.
    gender = random.choice([None, "Male", "Female"])
    age = random.choice([None, random.randint(20, 70)])

    event = {
        # For now ride_ids will be randomly generated although in future,
        # Some logic is required to connect passengers and drivers
        "ride_id": fake.uuid4(),
        "passenger_id": fake.uuid4(),
        "passenger_name": fake.name(),
        "gender": gender,
        "age": age,
        "timestamp": int(time.time() * 1000),
        "pickup_location": {
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude())
        },
        "dropoff_location": {
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude())
        },
        "event_type": random.choice(['REQUEST', 'CANCELLATION']),
        "vehicle_type": random.choice(["STANDARD", "SHARED", "VAN", "PREMIUM"]),
    }
    return event


##############################################
########### GENERATE PAYMENT EVENT ###########
##############################################
def generate_pricing_event(fake):
    event = {
        "ride_id": fake.uuid4(),
        "multiplier": round(random.uniform(1.0, 3.0), 2),
        "timestamp": int(time.time() * 1000),
        "reason": random.choice(["HIGH_DEMAND", "LOW_SUPPLY", "EVENT", "WEATHER", "OTHER"]),
        "duration": random.randint(5, 30),
        "weather": random.choice(["CLEAR", "RAIN", "STORM", "SNOW", "HOT", "COLD", "WINDY"])
    }
    return event


#################################################
########### SERIALIZE EVENTS FUNCTION ###########
#################################################
def serialize_events(schema, events, filename):
    parsed_schema = parse_schema(schema)
    with open(filename, "wb") as out:
        writer(out, parsed_schema, events)
