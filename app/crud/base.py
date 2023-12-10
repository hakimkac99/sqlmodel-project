from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from sqlmodel import Session, SQLModel, select

TableModelType = TypeVar("TableModelType", bound=SQLModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[TableModelType, ReadSchemaType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[TableModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        """
        self.model = model

    async def read_by_id(self, session: Session, id: Any) -> Optional[ReadSchemaType]:
        return await session.get(self.model, id)

    async def read_multi(self, session: Session, *, offset: int = 0, limit: int = 100) -> List[ReadSchemaType]:
        statement = select(self.model).offset(offset).limit(limit)
        result = await session.exec(statement)
        return result.unique().all()

    async def create(self, session: Session, *, obj_in: CreateSchemaType) -> ReadSchemaType:
        db_obj = self.model.from_orm(obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self, session: Session, *, db_obj: ReadSchemaType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ReadSchemaType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, session: Session, *, id: int) -> ReadSchemaType:
        db_obj = await session.get(self.model, id)
        await session.delete(db_obj)
        await session.commit()
        return db_obj
