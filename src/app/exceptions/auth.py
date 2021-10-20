from fastapi import HTTPException,status
    
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

unauthorize_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Unauthorized'
)