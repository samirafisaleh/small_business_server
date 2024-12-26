

import time 
from fastapi import FastAPI, Request

from source.routers import (
    business,
    cart,
    cartitem,
    invoice,
    item
)
from source.shared import sentry

app = FastAPI(
    title="Small Business",
    description="",
    version="0.1.0"
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    return response 


################################################
# Middleware
################################################


app.include_router(business.router, prefix="/business")
app.include_router(cart.router, prefix="/cart")
app.include_router(cartitem.router, prefix="/cartitem")
app.include_router(invoice.router, prefix="/invoice")
app.include_router(item.router, prefix="/item")