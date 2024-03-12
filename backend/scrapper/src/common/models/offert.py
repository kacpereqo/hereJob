from enum import Enum

from pydantic import BaseModel


class OffertProvider(str, Enum):
    justjoinit = "justjoinit"
    nofluffjobs = "nofluffjobs"
    pracujpl = "pracujpl"
    stackoverflow = "stackoverflow"
    remotive = "remotive"
    remoteok = "remoteok"
    github = "github"
    weworkremotely = "weworkremotely"


class salary(BaseModel):
    start: int
    end: int
    currency: str
    contract_type: str


class Location(BaseModel):
    longitude: float
    latitude: float
    country: str
    city: str
    street: str | None


class WorkMode(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    remote = "remote"


class Offert(BaseModel):
    title: str
    offert_url: str
    company: str
    required_skills: list[str]
    apply_url: str | None
    price: float
    description: str
    salary: list[salary]
    locations: list[str]
    work_mode: WorkMode
