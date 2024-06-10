# Tracardi Event Flow

The data flow in Tracardi goes through the following stages:

| Stage                 | Description                                                                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Source validation`   | Tracardi must have event source defined and enabled in the system.                                                                                                                                   |
| `Event mapping`       | Tracardi can validate the event data schema, map event and reshape its schema if needed.                                                                                                             |
| `Identity resolution` | At this point the profile is identified if it exists in the system or a new anonymous profile is created. Tracardi checks if the profile can be merged with other profiles that seems to be the same |
| `Event reshaping`     | Tracardi can change the event schema if needed.                                                                                                                                                      |
| `Event collection`    | Tracardi saves the event.                                                                                                                                                                            |
| `Event routing`       | Tracardi reads a rule that defines which workflow must precess event.                                                                                                                                |
| `Processing`          | Tracardi runs a workflow that processed event data, enhances the data,routes                                                                                                                         |
|                       | it to external systems, etc.                                                                                                                                                                         |
| `Data orchestration`  | Data is send to the defined external systems                                                                                                                                                         |


## Details

1. Source Validation

   Description: Tracardi must have the event source defined and enabled in the system.
   Detail: Ensures that the incoming event is from a recognized and active event source. The event source identifier is
   checked against the registered event sources in Tracardi.

2. Event Mapping

   Description: Tracardi can validate the event data schema, map the event, and reshape its schema if needed.
   Detail: The event's data is validated to ensure it meets the expected schema. If necessary, the event data is mapped
   to build events traits, potentially renaming fields or converting data formats for consistency and
   usability.

3. Identity Resolution

   Description: Identifies the profile if it exists in the system or creates a new anonymous profile. Tracardi checks if
   the profile can be merged with other profiles that seem to be the same.
   Detail: Tracardi attempts to resolve the identity of the event's originator. If a matching profile exists, it is
   retrieved; otherwise, a new anonymous profile is created. The system also looks for potential merges with existing
   profiles based on predefined keys such as email addresses.

4. Event Reshaping

   Description: Tracardi can change the event schema if needed.
   Detail: The event data may be further transformed to match specific workflow requirements or to enhance the data
   before processing. This could involve adding, removing, or modifying event attributes.

5. Event Collection

   Description: Tracardi saves the event.
   Detail: The validated and possibly reshaped event data is stored in Tracardi's database. This ensures that the event
   is available for historical analysis and future reference.

6. Event Routing

   Description: Tracardi reads a rule that defines which workflow must be triggered by the event.
   Detail: Based on predefined routing rules, Tracardi determines which workflow should handle the event. These rules
   consider the event type, source, and possibly other conditions.

7. Processing

   Description: Tracardi runs a workflow that processes event data, enhances the data, and routes it to external
   systems, etc.
   Detail: The selected workflow is executed, performing a series of actions defined in the workflow nodes. These
   actions could include data enhancement, transformation, or interaction with other systems.

8. Data Orchestration

   Description: Data is sent to the defined external systems.
   Detail: As part of the workflow, Tracardi orchestrates the sending of processed data to external systems or services.
   This ensures that the relevant external systems are updated with the latest event data for further processing or
   action.

---
Questions that this documentation answers:

* What stages does data flow through in Tracardi?
* How does Tracardi route events to the appropriate workflow?
* What is the role of segmentation in Tracardi?
* How does Tracardi handle profile merging?
* What is event reshaping in Tracardi?
* How does Tracardi determine which workflow to use when processing an event?
* How does segmentation in Tracardi differ from traditional market segmentation techniques?
* Can Tracardi be used to send data to multiple external systems simultaneously? If so, how?
* How does Tracardi validate event data?
* What are some examples of tasks that can be performed by actions in Tracardi workflows?
* How does Tracardi segment profiles?
* How to merge profiles from different channels?
