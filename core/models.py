from bson import ObjectId
from typing import Optional, List, Any
from pydantic import BaseModel


class Contract:
    """ Contract DB object """
    _id: ObjectId
    address: str
    chain: str
    abi: list


class Page:
    """ Contract DB object """
    _id: ObjectId
    contract: ObjectId
    creator: str
    config: list
    name: Optional[str]
    description: Optional[str]


class FunctionInputField(BaseModel):
    """ Model of the single smart contract function """
    id: str
    name: Optional[str]  # custom set field name
    description: Optional[str]  # custom set field description
    type: str
    hidden: bool

    value: Optional[Any]  # prefilled value
    multiply_by: Optional[str]  # optional multiply action to perform with the field before tx execution


class Function(BaseModel):
    """ Model of the single smart contract function """
    id: str
    name: Optional[str]  # custom set function name
    description: Optional[str]  # custom set function description
    inputs: List[FunctionInputField]


class Chain(BaseModel):
    """ Chain object """
    id: str
    name: str


class ChainsListAPIResponse(BaseModel):
    data: List[Chain]


class PageAPIResponseModel(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    config: List[Optional[Function]]


class UpdatePageRequestBody(BaseModel):
    """ Request json body for page update """
    page_id: str
    config: List[Optional[Function]]
