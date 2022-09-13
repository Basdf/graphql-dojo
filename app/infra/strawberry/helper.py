import contextlib
from typing import Any

from sqlalchemy.inspection import inspect
from strawberry.types import Info

from app.schemas.general import SearchSchemaType


def get_dict_strawberry_input(input: SearchSchemaType):
    return {key: value for key, value in input.__dict__.items() if value is not None}


def get_only_selected_fields(db_baseclass_name, info: Info) -> list[str]:
    db_relations_fields: dict[str, Any] = inspect(
        db_baseclass_name
    ).relationships.keys()
    return [
        field.name
        for field in info.selected_fields[0].selections
        if field.name not in db_relations_fields
    ]


def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        with contextlib.suppress(Exception):
            data_dict[column.name] = getattr(model_data_object, column.name)
    return data_dict
