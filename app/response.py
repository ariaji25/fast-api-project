from fastapi import status, HTTPException, Response

def response(res : Response, data):
    res.status_code = data.status_code
    return data

def httpResponse(func, res : Response, *args, **kwargs):
    """ 
        The 'func' parameters is a function with BaseResponse return value or
        Class that extend to BaseModel class from pydantic
    """
    try:
        return response(res, func(*args, **kwargs))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def authorizeHttpResponse(res : Response, authorized, *args, **kwargs):
    if authorized:
        return httpResponse(res, *args, **kwargs)
    else:
        raise httpResponse(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED")