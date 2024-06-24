# Event Processing

**Steps in Tracardi Event Processing:**

1. **Data Validation:**
    - **Purpose:** Ensure that the incoming data conforms to expected formats and types.
    - **Process:** Utilize a JSON schema to define the structure and data types of the event. This validation step helps
      in maintaining data integrity and consistency by rejecting events that do not meet the predefined criteria.

2. **Event Reshaping:**
    - **Purpose:** Transform the incoming data to fit your system's needs, especially when you don't control the source
      data format.
    - **Process:** Define the event source and type, then reshape the data by specifying keys and values. This allows
      you to modify the event data structure to align with your internal requirements.

3. **Event Mapping:**
    - **Purpose:** Organize and move data within the event to appropriate locations.
    - **Process:** Differentiate between indexed (traits) and non-indexed (properties) data. Map data from properties to
      traits. For example, map an email property to an email trait, which can be used as a filter filed. This step
      ensures data is correctly categorized and indexed for efficient retrieval.

4. **Identification Checkpoint:**
    - **Purpose:** Determine if incoming data should trigger the merging of profiles.
    - **Process:** Set rules for merging data based on certain criteria, such as matching email addresses. This is
      useful for consolidating duplicate profiles into a single customer profile, ensuring a unified view of customer
      data.

5. **Event to Profile Mapping:**
    - **Purpose:** Transfer relevant event data to the customer profile.
    - **Process:** Define how data from specific events (e.g., profile creation) is copied to profile traits. This step
      updates the customer profile with new information from events, ensuring profiles are continuously enriched and
      up-to-date.

6. **Workflow:**
    - **Purpose:** Trigger automated workflows based on specific events.
    - **Process:** Specify event types, sources, and workflows to be activated when an event occurs. You can also set
      conditions based on customer consents to restrict workflow triggering. This step enables automated responses and
      actions, enhancing efficiency and personalization in customer interactions.

By following these six steps, Tracardi ensures that data is accurately validated, transformed, organized, merged,
mapped, and used to trigger workflows, thereby maintaining robust data management and improving customer profile
accuracy.