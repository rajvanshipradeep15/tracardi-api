This plugin allows users to show a question popup with two possible answers. The answer clicked by the user will be sent back to Tracardi as a new event type. The plugin takes any payload as input and returns the given payload on port payload without any changes. 

The plugin has a configuration form with several fields. The UIX Source field requires a URL where UIX elements are located, usually http://localhost:8686. The API URL field is the URL of the API that the event will be sent to. The Popup Title and Popup Content fields provide the title and content for the popup, respectively. The Left and Right Button Text fields provide the text to be displayed on the left and right buttons, respectively. The Horizontal and Vertical Position fields select the horizontal and vertical positions for the popup to be displayed. The Event Type field is the type of event to be sent back to the given API URL. The Save Event field allows users to save the event that is sent back from the popup. The Popup Lifetime field provides the number of seconds for the popup to be displayed. The Dark Theme field allows users to switch the popup into dark mode. 

The plugin also has an advanced configuration section which allows users to configure the plugin using a JSON object. This object includes fields for the API URL, UIX Source, Popup Title, Content, Left and Right Button Text, Horizontal and Vertical Position, Event Type, Save Event, Popup Lifetime, and Dark Theme.