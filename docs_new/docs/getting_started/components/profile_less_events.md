# Profile-less events

Profile-less events in Tracardi are events that are not associated with any user profile. These events are useful for
tracking interactions and occurrences that do not need to be linked to a specific user, such as anonymous user actions
or system-generated events. Here’s a detailed overview of profile-less events in Tracardi:

### Characteristics of Profile-less Events

1. **No User Association**: These events do not contain information that links them to a specific user profile.
2. **Anonymity**: Useful for tracking actions from users who have not logged in or who are interacting with the system
   anonymously.
3. **System Events**: Can also be used for system-generated events where user context is irrelevant.

### Use Cases for Profile-less Events

- **Anonymous Interactions**: Tracking page views, clicks, or other interactions from external systems that do not have
  the information about profile id.
- **System Monitoring**: Capturing events related to system performance, errors, or other technical occurrences that do
  not need to be tied to a user.

### Implementing Profile-less Events

When creating or handling events in Tracardi, you can specify whether an event should be profile-less. Here are the main
considerations:

1. **Event Payload**:
    - Ensure the event payload does not include profile-related information or set appropriate flags to indicate the
      event is profile-less.

### Example Configuration

Here’s an example of a profile-less event payload:

```json
{
  "type": "page-view",
  "properties": {
    "url": "https://example.com",
    "title": "Example Page"
  },
  "profile": null
}
```

In this example, the `profile` field is set to `null`, indicating that the event does not relate to any user profile.

### Considerations

- **Limited Personalization**: Since these events are not linked to user profiles, they cannot be used for personalized
  interactions or targeted actions.
- **Aggregated Insights**: While useful for aggregate data analysis, these events do not provide insights at the
  individual user level.

### Summary

Profile-less events in Tracardi are designed to handle interactions and occurrences that lack user identification. They
are often generated in use cases where the user cannot be identified. However, profile-less events can be converted to
events with profiles if the event payload contains identifiable information, such as an email address, which can be used
to reference the correct profile ID.