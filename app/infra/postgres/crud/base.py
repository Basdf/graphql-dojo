from typing import Any, Generic

from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.schemas.general import DBModelType


class CRUDBase(Generic[DBModelType]):
    def __init__(self, *, model: DBModelType) -> None:
        self.model = model

    async def create(
        self,
        entity: dict[str, Any],
    ) -> dict[str, Any]:
        async with get_session() as session:
            model = self.model(**entity)
            session.add(model)
            return model

    async def create_all(self, entities: list[dict[str, Any]]) -> list[dict[str, Any]]:
        async with get_session() as session:
            models = [self.model(**entity) for entity in entities]
            session.add_all(models)
            return models

    async def get_all(
        self,
        selected_fields: list[str],
        payload: dict[str, Any] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> list[DBModelType]:
        if payload is None:
            payload = {}
        async with get_session() as session:
            select_query: Select = select(self.model)
            select_query = select_query.filter_by(**payload)
            select_query = select_query.offset(skip).limit(limit)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().all()
