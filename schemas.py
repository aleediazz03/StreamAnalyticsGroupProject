import json


driver_schema = {
    "namespace": "ridehailing.driver",
    "type": "record",
    "name": "DriverEvent",
    "fields": [
        {"name": "driver_id", "type": "string"},
        {"name": "gender", "type": ["null", "string"], "default": None},
        {"name": "age", "type": ["null", "int"], "default": None},
        {"name": "rating", "type": ["null", "float"], "default": None},
        {"name": "ride_id", "type": ["null", "string"], "default": None},
        {"name": "timestamp", "type": "long"},
        {"name": "vehicle", "type": {
          "type": "enum",
          "name": "VehicleType",
          "symbols": ["STANDARD", "SHARED", "VAN", "PREMIUM"]
        }},
        {
            "name": "location",
            "type": {
                "type": "record",
                "name": "Location",
                "fields": [
                    {"name": "latitude", "type": "double"},
                    {"name": "longitude", "type": "double"}
                ]
            }
        },
        {
            "name": "status",
            "type": {
                "type": "enum",
                "name": "DriverStatus",
                "symbols": ["AVAILABLE", "ACCEPTED", "ONGOING", "COMPLETED"]
            }
        }
    ]
}

with open("schemas_json/driver_schema.json", "w") as f:
    json.dump(driver_schema, f)  # Save to file

passenger_schema = {
    "namespace": "ridehailing.passenger",
    "type": "record",
    "name": "passengerEvent",
    "fields": [ 
        {"name": "ride_id", "type": "string"},
        {"name": "passenger_id", "type": "string"},
        {"name": "passenger_name", "type": "string"},
        {"name": "gender", "type": ["null", "string"], "default": None},
        {"name": "age", "type": ["null", "int"], "default": None},
        {"name": "timestamp", "type": "long"},
        {
            "name": "pickup_location",
            "type": {
                "type": "record",
                "name": "pickupLocation",
                "fields": [
                    {"name": "latitude", "type": "double"},
                    {"name": "longitude", "type": "double"}
                ]
            }
        },
        {
            "name": "dropoff_location",
            "type": {
                "type": "record",
                "name": "dropoffLocation",
                "fields": [
                    {"name": "latitude", "type": "double"},
                    {"name": "longitude", "type": "double"}
                ]
            }
        },
        {
            "name": "event_type",
            "type": {
                "type": "enum",
                "name": "RequestType",
                "symbols": ["REQUEST", "CANCELLATION"]
            }
         },
         {
            "name": "vehicle_type",
            "type": {
                "type": "enum",
                "name": "vehicleType",
                "symbols": ["STANDARD", "SHARED", "VAN", "PREMIUM"]
            }
        }
    ]
}

with open("schemas_json/passenger_schema.json", "w") as f:
    json.dump(passenger_schema, f)  # Save to file


# Define the AVRO schema for Dynamic Pricing Events
pricing_schema = {
    "namespace": "ridehailing.pricing",
    "type": "record",
    "name": "PricingEvent",
    "fields": [
        {"name": "ride_id", "type": "string"}, 
        {"name": "multiplier", "type": "double"},  
        {"name": "timestamp", "type": "long"}, 
        {"name": "reason", "type": {
            "type": "enum",
            "name": "Reason",
            "symbols": ["HIGH_DEMAND", "LOW_SUPPLY", "EVENT", "WEATHER", "OTHER"]
        }}, 
        {"name": "duration", "type": "int"},  # How long the surge lasts (seconds)
        {"name": "weather", "type": {
            "type": "enum",
            "name": "Weather",
            "symbols": ["CLEAR", "RAIN", "STORM", "SNOW", "HOT", "COLD", "WINDY"]
        }, "default": "CLEAR"}  # Weather condition affecting price
    ]
}

with open("schemas_json/pricing_schema.json", "w") as f:
    json.dump(pricing_schema, f)  # Save to file