# Identity Resolution

Identity resolution in Tracardi is a process that unifies multiple profiles created from different sessions and devices
into a single, comprehensive profile. This technique ensures that all interactions and behaviors of a user across
various touch points are accurately combined to provide a complete view of the customer.

## Data Collection

Data collection involves gathering events and interactions from various devices. One set of events may be collected on
one device, and another on different devices, resulting in different Profile IDs for the same user. Data collection
itself is not responsible for merging these profiles.

## Identity Resolution Process

Identity resolution includes several key processes:

- **[Tracking](tracking.md)**: The process of maintaining a consistent single Profile ID across all customer
  interactions on a single
  device. It is the responsibility of the device/client to keep the Profile ID unchanged.

- **[Merging Profiles](merging.md)**: Tracardi merges the existing profiles collected on different devices or from
  different channels into a single unified profile.

- **Maintaining Multiple IDs**: The resulting unified profile may retain multiple profile IDs to identify the same
  profile created on different devices or browsers. Tracardi always returns a Profile ID. Note that the profile ID sent
  in the tracking payload may be different in the Tracardi response. For more details,
  see [why my profile ID in the response from Tracardi is different than the one I have sent](merging.md#why-my-profile-id-in-the-response-from-tracardi-is-different-then-the-one-i-have-sent).