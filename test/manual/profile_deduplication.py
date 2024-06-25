from time import sleep

import asyncio

from tracardi.context import ServerContext, Context
from test.utils import get_test_tenant
from tracardi.domain.payload.tracker_payload import TrackerPayload
from tracardi.service.merging.facade import compute_one_profile_in_db
from tracardi.service.track_event import track_event
from tracardi.service.tracking.storage.profile_storage import load_profile

from datetime import datetime, timedelta
from uuid import uuid4
from test.utils import Endpoint

from test.api.endpoints.test_event_source_endpoint import _create_event_source


endpoint = Endpoint()
month = datetime.now().month
year = datetime.now().year
prev_month = (datetime.now() - timedelta(days=32)).month


async def should_deduplicate_profile():
    with ServerContext(Context(production=False, tenant=get_test_tenant())):
        profile_id = str(uuid4())
        source_id = str(uuid4())
        session_id = str(uuid4())

        status = _create_event_source(source_id, "rest").status_code

        assert status == 200

        tracker_payload = TrackerPayload(**{
            "source": {
                "id": source_id
            },
            "profile": {
                "id": profile_id,
                "ids": ['a', 'b', 'c']
            },
            "session": {
                "id": session_id
            },
            "events": [
                {"type": "pytest1", "properties": {}}
            ]
        })

        response = await track_event(
            tracker_payload,
            '0.0.0.0',
            allowed_bridges=['rest']
        )

        print(response)

        # Duplicate profile

        tracker_payload = TrackerPayload(**{
            "source": {
                "id": source_id
            },
            "profile": {
                "id": str(uuid4()),
                "ids": ['a', 'b', 'c']
            },
            "session": {
                "id": session_id
            },
            "events": [
                {"type": "pytest2", "properties": {}}
            ]
        })

        response = await track_event(
            tracker_payload,
            '0.0.0.0',
            allowed_bridges=['rest']
        )

        srv_profile_id = response['profile']['id']

        print(response)

        sleep(5)

        # Trows error duplicate record
        profile = await load_profile(profile_id)
        assert profile.id == profile_id

        profile = await load_profile('a')

        profile, del_ids = await compute_one_profile_in_db(profile)

        print(del_ids)

        # profile = await deduplicate_profile('a')
        # print(profile)
        # await profile_db.refresh()
    #
    # record = await load_profile(profile.id)
    # assert record is not None
    # assert record.get_meta_data() is not None


asyncio.run(should_deduplicate_profile())
