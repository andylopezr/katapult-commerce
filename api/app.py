from ninja import NinjaAPI
from api.controllers.auth_bearer import AuthBearer
from api.endpoints import (
    login_router,
    user_router,
    bank_router,
    vendor_router,
    account_router,
    )

api = NinjaAPI(
    auth=AuthBearer(),
    title='Vendor Manager',
    version="0.1.0",
)

api.add_router('/login', login_router)
api.add_router('/user', user_router)
api.add_router('/bank', bank_router)
api.add_router('/account', account_router)
api.add_router('/vendor', vendor_router)
