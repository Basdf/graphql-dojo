from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.sql.selectable import Select

from app.core.db import get_session
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.gender import Gender


class CRUDGender(CRUDBase[Gender]):
    async def get_or_create(self, name: str) -> Gender:
        async with get_session() as session:
            select_query: Select = select(self.model)
            select_query.filter(self.model.name == name)
            records: ChunkedIteratorResult = await session.execute(select_query)
            return records.scalars().first()


crud_gender = CRUDGender(model=Gender)
