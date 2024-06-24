from typing import Optional

from fastapi import APIRouter, Depends, Response

from tracardi.domain.event_source import EventSource
from tracardi.exceptions.log_handler import get_logger

from tracardi.service.storage.mysql.service.system_entity_properties_service import SystemEntityPropertiesService
from tracardi.service.storage.mysql.mapping.system_entity_property_mapping import map_to_system_entity_property

from tracardi.domain.system_entity_property import SystemEntityProperty
from .auth.permissions import Permissions
from tracardi.config import tracardi
from ..service.grouping import get_grouped_result

logger = get_logger(__name__)

router = APIRouter(
    dependencies=[Depends(Permissions(roles=["admin", "developer"]))]
)

@router.get("/system-entity-property",
            tags=["system-entity-property"],
            include_in_schema=tracardi.expose_gui_api)
async def list_system_entities_properties(query: str = None):
    """
    Lists all system properties.
    """

    records = await SystemEntityPropertiesService().load_all(query, limit=500)

    return get_grouped_result("System Entities Properties", records, map_to_system_entity_property)

@router.get("/system-entity-property/{id}", tags=["system-entity-property"],
            response_model=Optional[EventSource],
            include_in_schema=tracardi.expose_gui_api)
async def load_system_entity_property(id: str, response: Response):
    """
    Returns system entity property with given ID (str)
    """

    record = await SystemEntityPropertiesService().load_by_id(id)

    if not record.exists():
        response.status_code = 404
        return None

    return record.map_to_object(map_to_system_entity_property)


@router.post("/system-entity-property", tags=["system-entity-property"],
             include_in_schema=tracardi.expose_gui_api)
async def save_system_entity_property(system_entity_property: SystemEntityProperty):
    """
    Adds new system entity property in database
    """
    return await SystemEntityPropertiesService().insert(system_entity_property)

@router.delete("/system-entity-property/{id}", tags=["system-entity-property"],
               include_in_schema=tracardi.expose_gui_api)
async def delete_system_entity_property(id: str):
    """
    Deletes system entity property with given ID (str).
    Return False if it is available in draft or production. True if all the instances where deleted
    """

    return await SystemEntityPropertiesService().delete_by_id(id)

