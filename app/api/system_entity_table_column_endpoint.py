from typing import Optional

from fastapi import APIRouter, Depends, Response

from tracardi.domain.event_source import EventSource
from tracardi.exceptions.log_handler import get_logger

from tracardi.service.storage.mysql.service.system_entity_table_column_service import SystemEntityTableColumnService

from tracardi.service.storage.mysql.mapping.system_entity_table_column_mapping import map_to_system_entity_table_column

from tracardi.domain.system_entity_table_column import SystemEntityTableColumn
from .auth.permissions import Permissions
from tracardi.config import tracardi
from ..service.grouping import get_grouped_result

logger = get_logger(__name__)

router = APIRouter(
    dependencies=[Depends(Permissions(roles=["admin", "developer"]))]
)

@router.get("/system-entity-table-column",
            tags=["system-entity-table-column"],
            include_in_schema=tracardi.expose_gui_api)
async def list_system_entity_table_columns(query: str = None):
    """
    Lists all system entity table columns.
    """

    records = await SystemEntityTableColumnService().load_all(query, limit=500)

    return get_grouped_result("System Entity Table Columns", records, map_to_system_entity_table_column)

@router.get("/system-entity-table-column/{id}", tags=["system-entity-table-column"],
            response_model=Optional[EventSource],
            include_in_schema=tracardi.expose_gui_api)
async def load_system_entity_table_column(id: str, response: Response):
    """
    Returns system entity table column with given ID (str)
    """

    record = await SystemEntityTableColumnService().load_by_id(id)

    if not record.exists():
        response.status_code = 404
        return None

    return record.map_to_object(map_to_system_entity_table_column)


@router.post("/system-entity-table-column", tags=["system-entity-table-column"],
             include_in_schema=tracardi.expose_gui_api)
async def save_system_entity_table_column(system_entity_property: SystemEntityTableColumn):
    """
    Adds new system entity table column in database
    """
    return await SystemEntityTableColumnService().insert(system_entity_property)

@router.delete("/system-entity-table-column/{id}", tags=["system-entity-table-column"],
               include_in_schema=tracardi.expose_gui_api)
async def delete_system_entity_table_column(id: str):
    """
    Deletes system entity table column with given ID (str).
    Return False if it is available in draft or production. True if all the instances where deleted
    """

    return await SystemEntityTableColumnService().delete_by_id(id)

