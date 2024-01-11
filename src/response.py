"""response.py"""
from pydantic import BaseModel


class ResponseModel(BaseModel):
    """
    Response shape
    """

    question: str
