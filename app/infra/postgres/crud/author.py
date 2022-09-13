from typing import Optional

from sqlalchemy import update
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.infra.postgres.crud.gender import crud_gender
from app.infra.postgres.models.author import Author
from app.schemas.pydantic.author import CreateAuthor, SearchAuthor, UpdateAuthor


class CRUDAuthor:
    async def create_author(self, entity: CreateAuthor) -> Author:
        async with get_session() as session:
            author = Author(**entity.dict(exclude={"genders"}))
            genders = [
                await crud_gender.get_or_create(name=gender.name)
                for gender in entity.genders
            ]
            author.genders = genders
            session.add(author)
            return author

    async def create_all_author(self, entities: list[CreateAuthor]) -> list[Author]:
        async with get_session() as session:
            authors: list[Author] = []
            for entity in entities:
                author = Author(**entity.dict(exclude={"genders"}))
                genders = [
                    await crud_gender.get_or_create(name=gender.name)
                    for gender in entity.genders
                ]
                author.genders = genders
                authors.append(author)
            session.add_all(authors)
            return authors

    async def get_authors(
        self,
        payload: Optional[SearchAuthor] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Author]:
        async with get_session() as session:
            select_query: Select = select(Author)
            if payload:
                select_query = select_query.filter_by(**payload.dict(exclude_none=True))
            select_query = select_query.offset(skip).limit(limit)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().all()

    async def update_author(
        self,
        id: int,
        payload: UpdateAuthor,
    ) -> Author:
        async with get_session() as session:
            select_query = (
                update(Author)
                .where(Author.id == id)
                .values(**payload.dict(exclude_none=True))
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(select_query)
            author: Author = await session.get(Author, id)
            return author

    async def delete_author(self, id: int) -> None:
        async with get_session() as session:
            author: Author = await session.get(Author, id)
            if author:
                await session.delete(author)


crud_author = CRUDAuthor()
