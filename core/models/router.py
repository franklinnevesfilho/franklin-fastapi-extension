from fastapi import FastAPI
from fastapi.routing import APIRouter


"""
Router Module

This module contains all the necessary decorators and functions needed to set up the API routes.
"""


_all_routers = []


def register_routes(app: FastAPI):
    """
    Register all the routers with the FastAPI app
    :param app: The FastAPI app
    :return: None
    """
    for router in _all_routers:
        app.include_router(router)


def Router(cls):
    instance = cls()
    router = APIRouter()

    for attr_name in dir(instance):
        attr = getattr(instance, attr_name)
        if hasattr(attr, 'route_info'):
            path, method = attr.route_info
            router.add_api_route(path, attr, methods=[method])

    _all_routers.append(router)

    return cls


def route(path: str, method: str):
    """
    A generic route that stores the route info on the method
    :param path:
    :param method:
    :return:
    """
    def decorator(func: callable):
        func.route_info = (path, method)
        return func
    return decorator


def GET(path: str):
    return route(path, "GET")


def PUT(path: str):
    return route(path, "PUT")


def POST(path: str):
    return route(path, "POST")


def DELETE(path: str):
    return route(path, "DELETE")


def PATCH(path: str):
    return route(path, "PATCH")
