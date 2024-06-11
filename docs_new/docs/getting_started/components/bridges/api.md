REST API Bridge in Tracardi

The REST API Bridge in Tracardi is designed to facilitate data collection via HTTP requests. It is one of the primary
bridges used for structured data collection, providing a straightforward method for integrating external systems with
Tracardi.
How the REST API Bridge Works

1. Endpoint and Method

The REST API Bridge uses a standard endpoint /track and the HTTP POST method to collect data. This endpoint is
configured to receive event data from external systems.

Example Endpoint:

arduino

POST http://your-tracardi-url/track

2. Data Structure

Data sent to the REST API Bridge must be structured in JSON format. This JSON payload includes various event properties
that Tracardi will process.

Example Payload:

json

{
"type": "page-view",
"properties": {
"url": "https://example.com",
"title": "Homepage"
},
"session": {
"id": "session-id"
},
"profile": {
"id": "profile-id"
}
}

3. Configuration and Setup

The REST API Bridge does not require additional configuration beyond setting up the event source in Tracardi. Here’s how
to set it up:

    Create an Event Source:
        Navigate to the Inbound Traffic section in the Tracardi GUI.
        Click on Add New Source.
        Provide a name, type, and channel for the event source.
        Select the REST API Bridge as the method of data collection.

    Integration with External Systems:
        Configure your external system to send HTTP POST requests to the /track endpoint of your Tracardi instance.
        Ensure the payload follows the JSON structure required by Tracardi.

4. Event Processing

Once the data is received by the /track endpoint, Tracardi processes the event through several stages:

    Validation:
        Tracardi validates the incoming data to ensure it conforms to the expected schema and contains all required fields.

    Mapping:
        The system maps the event data to the appropriate fields within Tracardi, reshaping the schema if necessary.

    Identity Resolution:
        Tracardi identifies the profile associated with the event, either by matching the profile ID or creating a new anonymous profile.

    Event Storage:
        The event is saved to the Tracardi database, allowing for subsequent processing and analysis.

    Workflow Execution:
        Tracardi routes the event to the relevant workflows based on predefined rules, enabling automation and data processing.

5. Example Integration

To illustrate, here’s how you might configure an external application to send data to Tracardi using the REST API
Bridge:

Example cURL Command:

bash

curl -X POST http://your-tracardi-url/track \
-H "Content-Type: application/json" \
-d '{
"type": "purchase",
"properties": {
"product": "Laptop",
"price": 1200.00
},
"session": {
"id": "session-12345"
},
"profile": {
"id": "profile-67890"
}
}'

6. Benefits of Using REST API Bridge

   Simplicity: Easy to set up and use with minimal configuration.
   Flexibility: Can be integrated with various systems and platforms that support HTTP POST requests.
   Real-Time Data Collection: Enables real-time data ingestion and processing.
   Scalability: Suitable for collecting data from high-traffic applications.

Summary

The REST API Bridge in Tracardi is a powerful tool for integrating external systems via HTTP POST requests. It allows
for structured data collection, seamless integration, and real-time processing, making it a versatile solution for a
wide range of data collection needs. By configuring the REST API Bridge, you can ensure efficient and effective data
flow into Tracardi, enabling comprehensive data analysis and personalized customer experiences.