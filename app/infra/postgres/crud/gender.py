from typing import Optional

from sqlalchemy import update
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.infra.postgres.models.gender import Gender
from app.schemas.pydantic.gender import CreateGender, SearchGender, UpdateGender


class CRUDGender:
    async def create_gender(self, entity: CreateGender) -> Gender:
        async with get_session() as session:
            gender = Gender(**entity.dict())
            session.add(gender)
            return gender

    async def create_all_gender(self, entities: list[CreateGender]) -> list[Gender]:
        async with get_session() as session:
            genders: list[Gender] = [Gender(**entity.dict()) for entity in entities]
            session.add_all(genders)
            return genders

    async def get_genders(
        self,
        payload: Optional[SearchGender] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Gender]:
        async with get_session() as session:
            select_query: Select = select(Gender)
            if payload:
                select_query = select_query.filter_by(**payload.dict(exclude_none=True))
            select_query = select_query.offset(skip).limit(limit)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().all()

    async def update_gender(
        self,
        id: int,
        payload: UpdateGender,
    ) -> Gender:
        async with get_session() as session:
            select_query = (
                update(Gender)
                .where(Gender.id == id)
                .values(**payload.dict(exclude_none=True))
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(select_query)
            gender: Gender = await session.get(Gender, id)
            return gender

    async def delete_gender(self, id: int) -> None:
        async with get_session() as session:
            gender: Gender = await session.get(Gender, id)
            if gender:
                await session.delete(gender)

    async def get_or_create(self, name: str) -> Gender:
        async with get_session() as session:
            select_query: Select = select(Gender)
            select_query = select_query.filter(Gender.name == name)
            records: ChunkedIteratorResult = await session.execute(select_query)
            gender = records.scalar()
            if gender:
                return gender
            gender = Gender(name=name)
            session.add(gender)
            return gender


crud_gender = CRUDGender()
