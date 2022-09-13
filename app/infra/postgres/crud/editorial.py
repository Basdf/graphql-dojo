from typing import Optional

from sqlalchemy import update
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.infra.postgres.models.editorial import Editorial
from app.schemas.pydantic.editorial import (
    CreateEditorial,
    SearchEditorial,
    UpdateEditorial,
)


class CRUDEditorial:
    async def create_editorial(self, entity: CreateEditorial) -> Editorial:
        async with get_session() as session:
            editorial = Editorial(**entity.dict())
            session.add(editorial)
            return editorial

    async def create_all_editorial(
        self, entities: list[CreateEditorial]
    ) -> list[Editorial]:
        async with get_session() as session:
            editorials: list[Editorial] = [
                Editorial(**entity.dict()) for entity in entities
            ]
            session.add_all(editorials)
            return editorials

    async def get_editorials(
        self,
        payload: Optional[SearchEditorial] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Editorial]:
        async with get_session() as session:
            select_query: Select = select(Editorial)
            if payload:
                select_query = select_query.filter_by(**payload.dict(exclude_none=True))
            select_query = select_query.offset(skip).limit(limit)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().all()

    async def update_editorial(
        self,
        id: int,
        payload: UpdateEditorial,
    ) -> Editorial:
        async with get_session() as session:
            select_query = (
                update(Editorial)
                .where(Editorial.id == id)
                .values(**payload.dict(exclude_none=True))
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(select_query)
            editorial: Editorial = await session.get(Editorial, id)
            return editorial

    async def delete_editorial(self, id: int) -> None:
        async with get_session() as session:
            editorial: Editorial = await session.get(Editorial, id)
            if editorial:
                await session.delete(editorial)


crud_editorial = CRUDEditorial()
