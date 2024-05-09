from fastapi import APIRouter
from fastapi_restful.cbv import cbv


router = APIRouter(prefix='/nyan')


@cbv(router)
class NyanRouter:
    @router.get("/")
    def nyan(self):
        return 'nyan'
    
    @router.get("/meow")
    def meow(self):
        return 'meow'
