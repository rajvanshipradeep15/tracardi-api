Tracardi is a tracking and profiling system that allows users to integrate their web page or other systems with Tracardi by calling the Tracardi endpoint. The endpoint requires a tracker payload, which is a JSON data that consists of the source ID, session ID, profile ID, context, properties, events, and options. The source ID must match the source ID that is defined in Tracardi, otherwise the system will return an "Unauthorized Access" response. The session ID is a UUID generated and saved on the client's side, while the profile ID is generated on the server side. The events are a collection of event objects that consist of type, properties, context, and options. 

Tracardi uses two IDs to identify customers: the profile ID and the session ID. Both of these IDs need to be included in every tracker payload when sending data to Tracardi. The session ID can be generated on the client side using a UUID4 ID, while the profile ID is generated by Tracardi's backend and is not available when a customer visits the page for the first time. To obtain the profile ID, the recommended approach is to send the tracker payload without setting the profile ID, and only generate the session ID. Tracardi will then return the generated profile ID, which needs to be saved on the client side. 

It is important to synchronize the profile ID returned in the response with the profile ID saved on the client side. If the profile ID in the response is different from the one sent, it means that the client should update its profile ID and include the new one in the next call to avoid potential synchronization issues. It is also possible to keep the profile unchanged but change the session ID by providing the profile ID while generating a new session ID. This will result in a new session being created, while the profile remains unchanged, and the system generates a new visit for the user. However, it is not recommended to send the same session ID with all the tracking payloads, as it will not be possible to change the visits associated with the profile.