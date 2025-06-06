from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


class ListRow(BaseModel):
    id: Optional[int] = None
    read_code: str
    amount: float
    item_code: Optional[str] = None
    sales_code: Optional[str] = None
    desc_item: Optional[str] = None
    date_expiry: Optional[datetime] = None
    purchase_cost: Optional[float] = None
    items_pack: Optional[float] = None
    desc_dep: Optional[str] = None
    stock: Optional[float] = None
    weight: Optional[float] = None
    sales_price: Optional[float] = None
    measurement: Optional[str] = None
    sale_by_weight: Optional[bool] = None
    state: Optional[str] = None
    supplier: Optional[str] = None
    item_supplier: Optional[str] = None
    is_deleted: bool


class RaccolteDevice(BaseModel):
    id_list: Optional[int] = None
    code_list: Optional[str] = None
    type_list: str
    desc_list: Optional[str] = None
    id_user: int
    name_user: Optional[str] = None
    state_list: int
    created_at: Optional[datetime] = None
    last_modified: Optional[datetime] = None
    date_list: datetime
    id_store: Optional[int] = None
    point_of_sale_id: Optional[int] = None
    closing_date: Optional[datetime] = None
    rows_list: Optional[List[ListRow]] = None


class RichiestaParametriList(BaseModel):
    days: Optional[int] = None
    user_id: Optional[int] = None
