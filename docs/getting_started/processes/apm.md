# Automatic Profile Merging

Automatic Profile Merging (APM) is the process of merging user profiles. This feature ensures that all data related to a
user is consolidated into a single profile. The APM functionality is designed to automatically merge profiles when
specific predefined fields, known as merging keys, contain matching data. AMP is a background process.

## How It Works

1. **Merging Keys**:
    - Tracardi uses predefined fields as merging keys to identify profiles that should be merged. These fields typically
      include:
        - Email addresses (`data.contact.email.main`, `data.contact.email.business`, `data.contact.email.private`)
        - Phone
          numbers (`data.contact.phone.main`, `data.contact.phone.business`, `data.contact.phone.whatsapp`, `data.contact.phone.mobile`)

2. **Profile Monitoring**:
    - The system continuously monitors changes in the profile fields designated as merging keys. When a change is
      detected, it generates a unique ID for each phone number and email.

3. **Hashing and Privacy**:
    - These unique IDs are hashed using a secure key to ensure privacy and security. The `AUTO_PROFILE_MERGING` key is
      used as a salt before hashing the identifiers.

4. **Profile IDs Management**:
    - The generated IDs are stored in the 'profile IDs' field with specific prefixes to indicate their type:
        - `emm-` for main email
        - `emb-` for business email
        - `emp-` for private email
        - `phm-` for main phone
        - `phw-` for WhatsApp phone
        - `phb-` for business phone
        - `pho-` for mobile phone

5. **Merging Process**:
    - Profiles flagged for merging (it happens when a change in a merging key is noticed) are processed by a background
      worker. This worker consolidates the profiles, moving the profile IDs from the individual profiles into the `ids`
      field of the merged profile. A new primary ID is selected from the available `ids`, and this new ID is returned in
      the Tracardi response.

6. **Profile Consistency**:
    - If a device does not update the Profile ID to the new merged value, the system will still correctly identify the
      profile by using the old ID. This is possible because profile identification uses both the primary ID and
      the `ids` field.

## Enabling Auto Profile Merging

To activate APM in Tracardi, follow these steps:

1. **Add Environment Parameter**:
    - Add the `AUTO_PROFILE_MERGING` environment parameter with a key of at least 20 characters when starting the
      Tracardi API (include it in the Docker command). This key is used for hashing emails and phone numbers.
2. **Enable Unique ID Generation**:
    - Enabling the `AUTO_PROFILE_MERGING` parameter also automatically enables the generation and storage of unique IDs
      for every email address processed by the system.

