from pydantic import BaseModel
from typing import List, Optional


class Answer(BaseModel):
    mcq: bool
    choice: int | None = None
    text: str | None = None


class Answers(BaseModel):
    questionnaire_id: str
    answers: List[Answer]


class Question(BaseModel):
    mcq: bool
    question: str
    correct: int | None = None
    text: str | None = None
    options: Optional[List[str | int]] = None


class Questionaire(BaseModel):
    title: str
    questions: List[Question]
