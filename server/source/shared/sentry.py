import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration


# sentry_sdk.init(
#     dsn="",
#     integrations=[FastApiIntegration()],
#     traces_sample_rate=1.0
# )