import fastapi
from fastapi.middleware.cors import CORSMiddleware

from core import routers


# App initialization and configuration
app = fastapi.FastAPI(title='depage API', description='Visit us at <a href="https://depage.app">depage.app</a>!')
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# Adding all routes
app.include_router(routers.info_router)
app.include_router(routers.page_router)
