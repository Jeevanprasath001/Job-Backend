# from passlib.context import CryptContext

# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)
from passlib.context import CryptContext

# Initialize the password hashing context with Argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Function to hash the password
def hash_password(password: str) -> str:
    """
    Hashes the password using Argon2.
    
    :param password: The plain text password
    :return: Hashed password
    """
    return pwd_context.hash(password)

# Function to verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against the hashed password.
    
    :param plain_password: The plain text password
    :param hashed_password: The hashed password
    :return: True if the password matches, otherwise False
    """
    return pwd_context.verify(plain_password, hashed_password)
