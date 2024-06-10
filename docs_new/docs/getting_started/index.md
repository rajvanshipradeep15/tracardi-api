# Tracardi Getting Started

## What is Tracardi

Tracardi is a Customer Data Platform (CDP) designed to collect, analyze, and act on customer data. It provides tools for
managing and leveraging customer information to improve engagement and drive business growth. Here’s a detailed
explanation of Tracardi and its purposes:
What is Tracardi?

Tracardi is an open-source Customer Data Platform (CDP) that consolidates customer data from various sources, processes
this data, and enables businesses to create personalized customer experiences. It integrates seamlessly with websites,
applications, and other platforms to gather user interactions, profile data, and behavioral data.
Purpose of Installing Tracardi

The primary purposes of installing Tracardi include:

* **Data Collection and Integration**:
  Unified Data Repository: Tracardi collects data from multiple touchpoints such as websites, mobile apps, and CRM
  systems, storing it in a unified repository.
  Real-Time Data Processing: It processes data in real-time, allowing businesses to respond to customer actions as they
  happen.

* **Customer Profiling**:
  360-Degree View: Tracardi builds comprehensive customer profiles by combining data from various sources, giving a
  360-degree view of each customer.
  Identity Resolution: It resolves customer identities across different channels, ensuring accurate and consistent data.

* **Personalization and Engagement**:
  Tailored Experiences: Tracardi enables personalized marketing and communication by leveraging detailed customer
  profiles and behaviors.
  Automated Workflows: It supports the creation of automated workflows to trigger personalized messages, offers, and
  content based on customer actions.

* **Analytics and Insights**:
  Behavioral Analysis: Tracardi analyzes customer behavior to identify patterns, preferences, and trends.
  Segmentation: It segments customers into different groups based on various criteria, allowing targeted marketing
  efforts.

* **Data Orchestration**:
  Integration with External Systems: Tracardi can route processed data to external systems like CRM, marketing
  automation platforms, and data warehouses.
  Data Enrichment: It enhances raw data with additional context and information, improving its value for
  decision-making.


## Getting Started

To start collecting data in Tracardi, you need to set up the system, integrate it with your website or application, and configure event sources and event tracking. Here's a step-by-step guide to get you started:


### 1. Install Tracardi

You need to have Tracardi installed and running. This can be done using Docker, Helm, or directly from the source code. Ensure that all necessary components, such as the backend, frontend, and optional modules, are installed.
### 2. Configure Event Sources

Event sources are the points where data enters Tracardi. You need to define these sources in the Tracardi system to start collecting data from them.

    Creating an Event Source: Go to the Tracardi GUI, navigate to Inbound Traffic, and add a new event source. You'll need to provide details such as the name, type, and URL of the event source.

### 3. Integrate Tracardi JavaScript Snippet

To collect data from your website, you need to integrate the Tracardi JavaScript snippet into your web pages.

    Add the JavaScript Snippet:

    html

    <script>
        !function(e){"object"==typeof exports&&"undefined"!=typeof module..
    </script>
    <script>
        const options = {
            tracker: {
                url: {
                    script: 'http://your-tracardi-url/tracker',
                    api: 'http://your-tracardi-url'
                },
                source: {
                    id: "<your-event-source-id>"
                }
            }
        }
    </script>

    Replace your-tracardi-url with the URL of your Tracardi API server and your-event-source-id with the ID of your event source.

### 4. Send Events via JavaScript

Define and send events from your web pages using JavaScript. Events can represent various user actions such as page views, clicks, form submissions, etc.

    Example of Sending Events:

    javascript

    window.tracker.track("page-view", {"url": window.location.href, "title": document.title});
    window.tracker.track("button-click", {"button-id": "subscribe-button"});

### 5. Verify Integration

After adding the JavaScript code and sending events, verify that the data is being collected properly in Tracardi.

    Check Event Data: Navigate to the Tracardi GUI and check the Events section to see if the events from your web pages are being captured.

### 6. Configure Workflows

Workflows define how events are processed in Tracardi. You can set up workflows to analyze and act on the collected data.

    Create Workflows: Go to the Processing section, create a new workflow, and define the nodes and actions based on your requirements.

Additional Features and Configurations

    Link Tracking: Track user interactions with links using the Inbound Traffic/Event Redirects feature.
    Real-time Processing: Send events immediately by setting the fire parameter to true in your JavaScript code.
    Event Context: Extend event information by defining context data such as browser metadata and system variables.

* **[Tracardi Core Definitions](core_definitions.md)**: Core terms used in Tracardi.
* **[Installation](../installation)**: How to install Tracardi
* **[Data collection](data_collection.md)**: How data is collected in Tracardi
* [Tracking and Identity resolution](tracking.md)
  * [Event tracking](../events/event_tracking.md)
  * [Profile merging](../profiles/profile_merging.md)
* [Profile segmentation](../profiles/profile_segmentation.md)
