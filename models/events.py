from pydantic import BaseModel
from beanie import Document
from typing import Optional, List

class Event(Document):
    creator: Optional[str]
    title: str          # 이벤트 타이틀
    image: str          # 이벤트 이미지 배너의 링크
    description: str    # 이벤트 설명
    tags: List[str]     # 그룹화를 위한 이벤트 태그
    location: str       # 이벤트 위치

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Study",
                "image": "https://www.test.pri/image.png",
                "description": "간단한 설명...",
                "tags": ["python", "fastapi", "study"],
                "location": "Google Meet"
            }
        }

    class Settings:
        name = "events"

# 업데이트 처리를 위한 pydantic 모델을 동일한 파일에 추가
class EventUpdate(BaseModel):
    title: Optional[str]          # 이벤트 타이틀
    image: Optional[str]          # 이벤트 이미지 배너의 링크
    description: Optional[str]    # 이벤트 설명
    tags: Optional[List[str]]     # 그룹화를 위한 이벤트 태그
    location: Optional[str]       # 이벤트 위치

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Study",
                "image": "https://www.test.pri/image.png",
                "description": "간단한 설명...",
                "tags": ["python", "fastapi", "study"],
                "location": "Google Meet"
            }
        }    
