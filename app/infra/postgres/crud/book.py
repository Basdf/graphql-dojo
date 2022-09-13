from typing import Optional

from sqlalchemy import update
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.infra.postgres.crud.gender import crud_gender
from app.infra.postgres.models.book import Book
from app.schemas.pydantic.book import CreateBook, SearchBook, UpdateBook


class CRUDBook:
    async def create_book(self, entity: CreateBook) -> Book:
        async with get_session() as session:
            book = Book(**entity.dict(exclude={"genders"}))
            genders = [
                await crud_gender.get_or_create(name=gender.name)
                for gender in entity.genders
            ]
            book.genders = genders
            session.add(book)
            return book

    async def create_all_book(self, entities: list[CreateBook]) -> list[Book]:
        async with get_session() as session:
            books: list[Book] = []
            for entity in entities:
                book = Book(**entity.dict(exclude={"genders"}))
                genders = [
                    await crud_gender.get_or_create(name=gender.name)
                    for gender in entity.genders
                ]
                book.genders = genders
                books.append(book)
            session.add_all(books)
            return books

    async def get_books(
        self,
        payload: Optional[SearchBook] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Book]:
        async with get_session() as session:
            select_query: Select = select(Book)
            if payload:
                select_query = select_query.filter_by(**payload.dict(exclude_none=True))
            select_query = select_query.offset(skip).limit(limit)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().all()

    async def update_book(
        self,
        id: int,
        payload: UpdateBook,
    ) -> Book:
        async with get_session() as session:
            select_query = (
                update(Book)
                .where(Book.id == id)
                .values(**payload.dict(exclude_none=True))
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(select_query)
            book: Book = await session.get(Book, id)
            return book

    async def delete_book(self, id: int) -> None:
        async with get_session() as session:
            book: Book = await session.get(Book, id)
            if book:
                await session.delete(book)


crud_book = CRUDBook()
