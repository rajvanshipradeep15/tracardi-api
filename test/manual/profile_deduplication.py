import asyncio

from api.track.event_server_endpoint import track
from tracardi.context import ServerContext, Context
from test.utils import get_test_tenant
from tracardi.domain.payload.tracker_payload import TrackerPayload
from tracardi.service.merging.facade import deduplicate_profile, merge_profiles_by_id
from tracardi.service.storage.elastic.interface.event import refresh_event_db
from tracardi.service.storage.elastic.interface.session import refresh_session_db, load_session_from_db
from tracardi.service.track_event import track_event
from tracardi.service.tracking.storage.profile_storage import load_profile

from datetime import datetime, timedelta
from uuid import uuid4
from test.utils import Endpoint

from test.api.endpoints.test_event_source_endpoint import _create_event_source
from tracardi.domain.profile import Profile
from tracardi.exceptions.exception import DuplicatedRecordException
from tracardi.service.storage.driver.elastic import profile as profile_db
from tracardi.service.storage.elastic_client import ElasticClient
from tracardi.service.storage.factory import storage_manager
from tracardi.service.storage.index import Resource

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

    # Trows error duplicate record
        profile = await load_profile(profile_id)
        assert profile.id == profile_id

        profile = await load_profile('a')

        await merge_profiles_by_id(profile)

        # profile = await deduplicate_profile('a')
        # print(profile)
        # await profile_db.refresh()
    #
    # record = await load_profile(profile.id)
    # assert record is not None
    # assert record.get_meta_data() is not None


asyncio.run(should_deduplicate_profile())
