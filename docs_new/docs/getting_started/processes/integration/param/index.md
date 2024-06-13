# Parametrized URL

If your web page has a tracking Javascript installed you can use parametrized URL to track the user clicks from outside
the webpage.

For example this can be useful when you would like to identify the user that clicked a link that you included in the
email.

If you already have the customer's profile because the e-mail was sent from Tracardi, you may
want to keep the information about the profile when the user clicks on the link. To do this, you need to enable the
static Profile ID in the event source that collects data and add the profile ID to the page's URL.

!!! Note

    It's important to note that this profile tracking will only work if the tracking script is on the page you redirect the user to. If the page doesn't have this script, you can refer to the documentation for information on [Redirected Links](../redirect/index.md) Bridge.

## Example

For example, by adding the `__tr_pid` and `__tr_src` as parameters to the URL, which contain the current profile ID and
source ID, the system will create a session for the profile that is referenced by `__tr_id` (if it exists in Tracardi).
There are some conditions for this to work. If the system already has a profile saved in the browser's local storage, it
will try to merge the
previous history of events on that page with the new profile ID and its history. If the user is visiting your page for
the first time, there shouldn't be any merging.

Remember that if a session number is provided, the event will be associated with the corresponding profile. If only a
profile ID is given, a new session will be created for that profile.