from fastapi import Depends, APIRouter, Body, HTTPException, status
from models.events import Event, EventUpdate
from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from auth.authenticate import authenticate

event_router = APIRouter(
    tags=["Events"]
)

event_database = Database(Event)

events = []

# 모든 이벤트 출력
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# 특정 이벤트 출력
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 ID 는 존재하지 않습니다"
        )
    return event


# 이벤트 생성
@event_router.post("/new")
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await event_database.save(body)
    return {
        "message": "새로운 이벤트가 생성되었습니다"
    }

# 이벤트 수정
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="허가되지 않은 작업입니다"
        )    
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 ID 는 존재하지 않습니다"
        )
    return updated_event


# 단일 이벤트 삭제
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 ID 는 존재하지 않습니다"
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="허가되지 않은 작업입니다(삭제)"
        )

    return {
        "message": "지정한 이벤트가 삭제되었습니다"
    }

# 전체 이벤트 삭제
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "모든 이벤트가 삭제되었습니다"
    }