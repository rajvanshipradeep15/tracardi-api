from typing import List, Dict, Any

from app.api.auth.permissions import Permissions
from tracardi.config import *
from fastapi import APIRouter, Depends
from tracardi.domain.settings import SystemSettings
from tracardi.service.setup.setup_envs import list_system_envs, get_system_envs

router = APIRouter(
    dependencies=[Depends(Permissions(roles=["admin", "developer"]))]
)


@router.get("/system/settings", tags=["system"],
            include_in_schema=tracardi.expose_gui_api,
            response_model=List[SystemSettings])
async def get_system_settings() -> List[SystemSettings]:
    """
    Lists all system settings
    """
    return list_system_envs()


@router.get("/system/envs", tags=["system"],
            include_in_schema=tracardi.expose_gui_api,
            response_model=Dict[str, Any])
async def get_system_envs() -> Dict[str, Any]:
    """
    Lists all system settings as key value
    """
    return get_system_envs()
