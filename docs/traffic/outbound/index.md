# Outbound traffic

Tracardi can sync profiles with external systems. To do this use destinations.

Destination is a set of credentials that point to an external system where the profile data will be sent when if
changed. Destination require some resource, e.g. a API endpoint, queue service, etc. This is here you set all the
required information on the credentials and the location of the external system. Not all resources are available as
destinations.

Depending on the system version, the list of available destinations may change. The easiest way to check the available
ones is to go to the `resources/extensions` tab and filter out `type/destinations`. To use one of them you need to
install.

Typical destination would be:

* Kafka
* Apache Pulasr
* Rabbitmq
* Remote API
* Mautic

Destinations are an extension point in tracardi meaning you can easily code your own destination and add it to the system core.