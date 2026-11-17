from fastapi import FastAPI

from api.routes import router

# Create the app and attach the endpoints defined in api/routes.py.
app = FastAPI()
app.include_router(router)
