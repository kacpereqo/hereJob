from typing import Any

from pydantic import BaseModel


class EmploymentType(BaseModel):
    salaryTo: int
    salaryFrom: int
    currency: str
    type: str
    
class Multilocation(BaseModel):
    city: str
    slug: str
    street: str
    latitude: float
    longitude: float


class justJoinItDTO(BaseModel):
    slug: str
    title: str
    requiredSkills: list[str]
    niceToHaveSkills: list[str] | None
    workplaceType: str
    workingTime: str
    experienceLevel: str
    employmentTypes: list[EmploymentType]
    categoryId: int
    multilocation: list[Multilocation]
    city: str
    street: str
    latitude: str
    longitude: str
    companyName: str
    companyLogoThumbUrl: str
    publishedAt: str
    remoteInterview: bool
    openToHireUkrainians: bool

    def __init__(self, **data: Any):
        super().__init__(**data)



