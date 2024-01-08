"""response.py"""
from typing import List
from pydantic import BaseModel


class QuestionModel(BaseModel):
    """
    Question shape
    """

    options: List[str]


class ResponseModel(BaseModel):
    """
    Response shape
    """

    question: QuestionModel
