from aiohttp.web import (
    middleware,
    json_response,
    Request,
    HTTPException
)


@middleware
async def error_handler(request: Request, handler):
    try:
        response = await handler(request)

        if response.status == 404:
            return json_response({'error': 'Not Found'}, status=404)
        
        return response
    except HTTPException as e:
        return json_response({'error': e.reason}, status=e.status)
    except Exception as e:
        return json_response({'error': 'Internal Server Error'}, status=500)

