from motor import motor_asyncio


client = motor_asyncio.AsyncIOMotorClient("")
db = client.get_database("small_business")

