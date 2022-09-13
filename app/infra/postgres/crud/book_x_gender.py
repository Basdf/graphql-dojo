from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.book_x_gender import BookXGender


class CRUDBookXGender(CRUDBase[BookXGender]):
    ...


crud_book_x_gender = CRUDBookXGender(model=BookXGender)
