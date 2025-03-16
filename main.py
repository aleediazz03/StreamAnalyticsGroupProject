import json
from faker import Faker

from functions import generate_driver_event, generate_passenger_event, generate_pricing_event, serialize_events

def main():
    # Retrieve the different schemas
    with open("schemas_json/driver_schema.json", "r") as f:
        driver_schema = json.load(f)

    with open("schemas_json/passenger_schema.json", "r") as f:
        passenger_schema = json.load(f)    
    
    with open("schemas_json/pricing_schema.json", "r") as f:
        pricing_schema = json.load(f)

    # Create the Faker object
    fake = Faker()

    # Generate the data (events) for the three schemas
    driver_events = [generate_driver_event(fake) for _ in range(5)]
    passenger_events = [generate_passenger_event(fake) for _ in range(5)]
    pricing_events = [generate_pricing_event(fake) for _ in range(5)]

    # Serialize the data
    serialize_events(driver_schema, driver_events, "serialized_data/driver_events.avro")
    serialize_events(passenger_schema, passenger_events, "serialized_data/passenger_events.avro")
    serialize_events(pricing_schema, pricing_events, "serialized_data/pricing_events.avro")


if __name__ == "__main__":
    main()