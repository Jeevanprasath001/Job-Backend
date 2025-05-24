from pydantic import BaseModel, EmailStr
from typing import Optional
from typing import List, Optional

# JobFilter model for filtering jobs
class JobFilter(BaseModel):
    job_title: Optional[str] = None
    skillset: Optional[str] = None
    city: Optional[str] = None
    min_experience: Optional[float] = None
    work_mode: Optional[str] = None

# Employee models
class EmployeeRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    confirm_password: str

class EmployeeLogin(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordWithOTP(BaseModel):
    email: EmailStr
    otp: int
    new_password: str

# Job Application Model
class JobApplication(BaseModel):
    name: str
    email: EmailStr
    job_title: str
    company: str
    resume: Optional[str] = None  # File name after saving
class ProfileData(BaseModel):
    avatar: Optional[str] = None
    firstName: str
    lastName: str
    email: str
    mobileNumber: str
    gender: str
    currentLocation: str
    highestQualification: Optional[str] = None
    university: Optional[str] = None
    primarySkills: List[str]
    projectDetails: Optional[str] = None
    noticePeriod: Optional[str] = None
    preferredSalary: Optional[str] = None
    resumeFileName: Optional[str] = None
    address: Optional[str] = None
    physicallyChallenged: Optional[str] = None
    preferredLocation: Optional[str] = None
    currentCTC: Optional[str] = None
    visa: Optional[str] = None