from pydantic import EmailStr, BaseModel
from typing import List, Optional


class AnswerBase(BaseModel):
    mcq: bool
    choice: int | None = None
    text: str | None = None



class Answer(AnswerBase):
    pass


class Answers(BaseModel):
    questionnaire_id: int 
    answers: List[Answer]



class QuestionBase(BaseModel):
    mcq: bool
    question: str
    correct: int | None = None
    text: str | None = None


class Question(QuestionBase):
    choices: Optional[List[str | int]] = None


class Questionaire(BaseModel):
    title: str
    questions: List[Question]

