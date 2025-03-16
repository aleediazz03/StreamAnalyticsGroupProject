### HELLO!! ###
WELCOME TO OUR RIDESHARING DATA FEED GENERATION PROJECT!!


This project focuses on designing and implementing a real-time analytics pipeline for ride-hailing services like Uber, Cabify, and Lyft. 
These platforms rely on real-time data processing to efficiently match passengers with drivers, monitor ongoing trips, and optimize pricing strategies. 
The goal is to simulate a real-world scenario where vast amounts of streaming data—such as ride requests, driver availability, trip statuses, 
and system alerts—are continuously ingested, processed, and analyzed to generate meaningful insights. 
Milestone 1: Data Feed Generation is the first step in this process, where a data generator is developed to simulate realistic ride-hailing events. 
This milestone involves selecting two key data feeds (e.g., passenger requests, ride statuses, driver availability, or surge pricing alerts), 
defining an AVRO schema for structured event representation, and producing event data in both JSON and AVRO formats. 
The schema design ensures that the generated data is useful for real-time analytics in later stages of the project. 
This foundational work sets the stage for subsequent milestones, where the data will be ingested, processed, and visualized in a real-time dashboard.


##### IMPORTANT NOTES #####

-- Project is divided into three separate files
    -- schemas.py contains the schemas for the different data feeds
    -- functions.py contains all helper functions used in the code such as functions to generate data and serialize data
    -- main.py here the main application is run, here all the functions are called
-- Whenever a change is made to a schema in the schemas.py file, the file must be run in order for the json files to be updated
    -- WHY? Well, this improves security, it makes sure there is an extra step before changing the json objects. (However, this data security aspect can still be improved)
-- Make sure to have installed the required packages
    -- faker, fastavro
