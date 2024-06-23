# What are you suggestion how to scale tracardi for 50K unique visitors?

Scaling isn't just about handling more visitors; it's also important to ensure your system remains operational even if
one of the servers fails. Let's consider a scenario with 50,000 visitors a day, each generating 20 events (be average
this is a large amount of events). This totals to 1 million events per day, or about 700 events per minute. I recommend
a setup with five servers, each having 8GB of RAM, 4 CPUs, and 160GB of storage. This setup is not too costly and offers
a lot of room for future expansion.

The cost of hosting varies depending on the provider. It ranges from 86 euros per month at Hetzner to $240 a month or
more at AWS. If you have a team skilled in managing Kubernetes, Hetzner is a cost-effective choice at 86 euros. If you
don't have Kubernetes expertise, then Digital Ocean at $240 might be better. We could consider reducing costs by half,
but that would require some testing. The suggested setup should be adequate for up to 20,000 events per minute, so there
may be potential for cost savings.

I didn’t include additional storage costs in these estimates. If you need more storage, for example, an extra 1TB, it
costs 55 euros per month at Hetzner and $100 at Digital Ocean. You'll need to decide how long you want to keep the data,
as storage costs can add up, especially since it's safer to have at least three data nodes for redundancy.

All the prices mentioned are current as of April 2024.