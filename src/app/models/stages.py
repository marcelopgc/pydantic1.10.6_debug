from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from app.handlers import document_analysis


class BaseClass(BaseModel):
    handler: Optional[str]


class ChildClass(BaseClass):
    handler: str = Field(document_analysis.__name__)
