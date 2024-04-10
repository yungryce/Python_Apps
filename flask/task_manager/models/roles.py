#!/usr/bin/python
from enum import Enum


class UserRole(Enum):
    ADMIN = "Admin"
    USER = "User"
    DEVELOPER = "Developer"

# Mapping dictionary
ROLE_MAP = {
    "Admin": UserRole.ADMIN,
    "User": UserRole.USER,
    "Developer": UserRole.DEVELOPER,
}

def get_user_role(role: str) -> UserRole:
    if role in ROLE_MAP:
        return ROLE_MAP[role]
    else:
        raise ValueError(f"{role} is not a valid UserRole")
