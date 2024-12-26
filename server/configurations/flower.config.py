import os
import dotenv

env_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), ".env"
)
dotenv.load_dotenv(env_file, override=True)


if FLOWER_ADDRESS := os.getenv("FLOWER_ADDRESS", None):
    address = FLOWER_ADDRESS
    print(f"FLOWER_ADDRESS: ".ljust(40) + str(address))
else:
    print(f"FLOWER_ADDRESS: ".ljust(40) + "(default)")
del FLOWER_ADDRESS


if FLOWER_AUTH := os.getenv("FLOWER_AUTH", None):
    auth = FLOWER_AUTH
    print(f"FLOWER_AUTH: ".ljust(40) + str(auth))
else:
    print(f"FLOWER_AUTH: ".ljust(40) + "(default)")
del FLOWER_AUTH

if FLOWER_AUTH_REFRESH := os.getenv("FLOWER_AUTH_REFRESH", None):
    FLOWER_AUTH_REFRESH = int(FLOWER_AUTH_REFRESH)
    auto_refresh = FLOWER_AUTH_REFRESH
    print(f"FLOWER_AUTH_REFRESH: ".ljust(40) + str(auto_refresh))
else:
    print(f"FLOWER_AUTH_REFRESH: ".ljust(40) + "(default)")
del FLOWER_AUTH_REFRESH

if FLOWER_BASIC_AUTH := os.getenv("FLOWER_BASIC_AUTH", None):
    basic_auth = FLOWER_BASIC_AUTH
    print(f"FLOWER_BASIC_AUTH: ".ljust(40) + str(basic_auth))
else:
    print(f"FLOWER_BASIC_AUTH: ".ljust(40) + "(default)")
del FLOWER_BASIC_AUTH

if FLOWER_BROKER_API := os.getenv("FLOWER_BROKER_API", None):
    broker_api = FLOWER_BROKER_API
    print(f"FLOWER_BROKER_API: ".ljust(40) + str(broker_api))
else:
    print(f"FLOWER_BROKER_API: ".ljust(40) + "(default)")
del FLOWER_BROKER_API

if FLOWER_CA_CERTS := os.getenv("FLOWER_CA_CERTS", None):
    ca_certs = FLOWER_CA_CERTS
    print(f"FLOWER_CA_CERTS: ".ljust(40) + str(ca_certs))
else:
    print(f"FLOWER_CA_CERTS: ".ljust(40) + "(default)")
del FLOWER_CA_CERTS

if FLOWER_CERTFILE := os.getenv("FLOWER_CERTFILE", None):
    certfile = FLOWER_CERTFILE
    print(f"FLOWER_CERTFILE: ".ljust(40) + str(certfile))
else:
    print(f"FLOWER_CERTFILE: ".ljust(40) + "(default)")
del FLOWER_CERTFILE

if FLOWER_CONF := os.getenv("FLOWER_CONF", None):
    conf = FLOWER_CONF
    print(f"FLOWER_CONF: ".ljust(40) + str(conf))
else:
    print(f"FLOWER_CONF: ".ljust(40) + "(default)")
del FLOWER_CONF

if FLOWER_DB := os.getenv("FLOWER_DB", None):
    db = FLOWER_DB
    print(f"FLOWER_DB: ".ljust(40) + str(db))
else:
    print(f"FLOWER_DB: ".ljust(40) + "(default)")
del FLOWER_DB

if FLOWER_DEBUG := os.getenv("FLOWER_DEBUG", None):
    FLOWER_DEBUG = bool(int(FLOWER_DEBUG))
    debug = FLOWER_DEBUG
    print(f"FLOWER_DEBUG: ".ljust(40) + str(debug))
else:
    print(f"FLOWER_DEBUG: ".ljust(40) + "(default)")
del FLOWER_DEBUG

if FLOWER_ENABLE_EVENTS := os.getenv("FLOWER_ENABLE_EVENTS", None):
    FLOWER_ENABLE_EVENTS = bool(int(FLOWER_ENABLE_EVENTS))
    enable_events = FLOWER_ENABLE_EVENTS
    print(f"FLOWER_ENABLE_EVENTS: ".ljust(40) + str(enable_events))
else:
    print(f"FLOWER_ENABLE_EVENTS: ".ljust(40) + "(default)")
del FLOWER_ENABLE_EVENTS

if FLOWER_FORMAT_TASK := os.getenv("FLOWER_FORMAT_TASK", None):
    format_task = FLOWER_FORMAT_TASK
    print(f"FLOWER_FORMAT_TASK: ".ljust(40) + str(format_task))
else:
    print(f"FLOWER_FORMAT_TASK: ".ljust(40) + "(default)")
del FLOWER_FORMAT_TASK

if FLOWER_INSPECT_TIMEOUT := os.getenv("FLOWER_INSPECT_TIMEOUT", None):
    inspect_timeout = FLOWER_INSPECT_TIMEOUT
    print(f"FLOWER_INSPECT_TIMEOUT: ".ljust(40) + str(inspect_timeout))
else:
    print(f"FLOWER_INSPECT_TIMEOUT: ".ljust(40) + "(default)")
del FLOWER_INSPECT_TIMEOUT

if FLOWER_KEYFILE := os.getenv("FLOWER_KEYFILE", None):
    keyfile = FLOWER_KEYFILE
    print(f"FLOWER_KEYFILE: ".ljust(40) + str(keyfile))
else:
    print(f"FLOWER_KEYFILE: ".ljust(40) + "(default)")
del FLOWER_KEYFILE

if FLOWER_MAX_WORKERS := os.getenv("FLOWER_MAX_WORKERS", None):
    FLOWER_MAX_WORKERS = int(FLOWER_MAX_WORKERS)
    max_workers = FLOWER_MAX_WORKERS
    print(f"FLOWER_MAX_WORKERS: ".ljust(40) + str(max_workers))
else:
    print(f"FLOWER_MAX_WORKERS: ".ljust(40) + "(default)")
del FLOWER_MAX_WORKERS

if FLOWER_MAX_TASKS := os.getenv("FLOWER_MAX_TASKS", None):
    FLOWER_MAX_TASKS = int(FLOWER_MAX_TASKS)
    max_tasks = FLOWER_MAX_TASKS
    print(f"FLOWER_MAX_TASKS: ".ljust(40) + str(max_tasks))
else:
    print(f"FLOWER_MAX_TASKS: ".ljust(40) + "(default)")
del FLOWER_MAX_TASKS

if FLOWER_NATURAL_TIME := os.getenv("FLOWER_NATURAL_TIME", None):
    FLOWER_NATURAL_TIME = bool(int(FLOWER_NATURAL_TIME))
    natural_time = FLOWER_NATURAL_TIME
    print(f"FLOWER_NATURAL_TIME: ".ljust(40) + str(natural_time))
else:
    print(f"FLOWER_NATURAL_TIME: ".ljust(40) + "(default)")
del FLOWER_NATURAL_TIME

if FLOWER_PERSISTENT := os.getenv("FLOWER_PERSISTENT", None):
    FLOWER_PERSISTENT = bool(int(FLOWER_PERSISTENT))
    persistent = FLOWER_PERSISTENT
    print(f"FLOWER_PERSISTENT: ".ljust(40) + str(persistent))
else:
    print(f"FLOWER_PERSISTENT: ".ljust(40) + "(default)")
del FLOWER_PERSISTENT

if FLOWER_PORT := os.getenv("FLOWER_PORT", None):
    FLOWER_PORT = int(FLOWER_PORT)
    port = FLOWER_PORT
    print(f"FLOWER_PORT: ".ljust(40) + str(port))
else:
    print(f"FLOWER_PORT: ".ljust(40) + "(default)")
del FLOWER_PORT

if FLOWER_STATE_SAVE_INTERVAL := os.getenv("FLOWER_STATE_SAVE_INTERVAL", None):
    FLOWER_STATE_SAVE_INTERVAL = int(FLOWER_STATE_SAVE_INTERVAL)
    state_save_interval = FLOWER_STATE_SAVE_INTERVAL
    print(f"FLOWER_STATE_SAVE_INTERVAL: ".ljust(40) + str(state_save_interval))
else:
    print(f"FLOWER_STATE_SAVE_INTERVAL: ".ljust(40) + "(default)")
del FLOWER_STATE_SAVE_INTERVAL


if FLOWER_XHEADERS := os.getenv("FLOWER_XHEADERS", None):
    FLOWER_XHEADERS = bool(int(FLOWER_XHEADERS))
    xheaders = FLOWER_XHEADERS
    print(f"FLOWER_XHEADERS: ".ljust(40) + str(xheaders))
else:
    print(f"FLOWER_XHEADERS: ".ljust(40) + "(default)")
del FLOWER_XHEADERS

if FLOWER_TASKS_COLUMNS := os.getenv("FLOWER_TASKS_COLUMNS", None):
    tasks_columns = FLOWER_TASKS_COLUMNS
    print(f"FLOWER_TASKS_COLUMNS: ".ljust(40) + str(tasks_columns))
else:
    print(f"FLOWER_TASKS_COLUMNS: ".ljust(40) + "(default)")
del FLOWER_TASKS_COLUMNS

if FLOWER_URL_PREFIX := os.getenv("FLOWER_URL_PREFIX", None):
    url_prefix = FLOWER_URL_PREFIX
    print(f"FLOWER_URL_PREFIX: ".ljust(40) + str(url_prefix))
else:
    print(f"FLOWER_URL_PREFIX: ".ljust(40) + "(default)")
del FLOWER_URL_PREFIX

if FLOWER_UNIX_SOCKET := os.getenv("FLOWER_UNIX_SOCKET", None):
    unix_socket = FLOWER_UNIX_SOCKET
    print(f"FLOWER_UNIX_SOCKET: ".ljust(40) + str(unix_socket))
else:
    print(f"FLOWER_UNIX_SOCKET: ".ljust(40) + "(default)")
del FLOWER_UNIX_SOCKET

if FLOWER_COOKIE_SECRET := os.getenv("FLOWER_COOKIE_SECRET", None):
    cookie_secret = FLOWER_COOKIE_SECRET
    print(f"FLOWER_COOKIE_SECRET: ".ljust(40) + str(cookie_secret))
else:
    print(f"FLOWER_COOKIE_SECRET: ".ljust(40) + "(default)")
del FLOWER_COOKIE_SECRET

if FLOWER_AUTH_PROVIDER := os.getenv("FLOWER_AUTH_PROVIDER", None):
    auth_provider = FLOWER_AUTH_PROVIDER
    print(f"FLOWER_AUTH_PROVIDER: ".ljust(40) + str(auth_provider))
else:
    print(f"FLOWER_AUTH_PROVIDER: ".ljust(40) + "(default)")
del FLOWER_AUTH_PROVIDER

if FLOWER_PURGE_OFFLINE_WORKERS := os.getenv("FLOWER_PURGE_OFFLINE_WORKERS", None):
    purge_offline_workers = FLOWER_PURGE_OFFLINE_WORKERS
    print(f"FLOWER_PURGE_OFFLINE_WORKERS: ".ljust(40) + str(purge_offline_workers))
else:
    print(f"FLOWER_PURGE_OFFLINE_WORKERS: ".ljust(40) + "(default)")
del FLOWER_PURGE_OFFLINE_WORKERS

if FLOWER_TASK_RUNTIME_METRICS_BUCKETS := os.getenv(
    "FLOWER_TASK_RUNTIME_METRICS_BUCKETS", None
):
    task_runtime_metric_buckets = FLOWER_TASK_RUNTIME_METRICS_BUCKETS
    print(
        f"FLOWER_TASK_RUNTIME_METRICS_BUCKETS: ".ljust(40)
        + str(task_runtime_metric_buckets)
    )
else:
    print(f"FLOWER_TASK_RUNTIME_METRICS_BUCKETS: ".ljust(40) + "(default)")
del FLOWER_TASK_RUNTIME_METRICS_BUCKETS

if FLOWER_OAUTH2_KEY := os.getenv("FLOWER_OAUTH2_KEY", None):
    oauth2_key = FLOWER_OAUTH2_KEY
    print(f"FLOWER_OAUTH2_KEY: ".ljust(40) + str(oauth2_key))
else:
    print(f"FLOWER_OAUTH2_KEY: ".ljust(40) + "(default)")
del FLOWER_OAUTH2_KEY

if FLOWER_OAUTH2_SECRET := os.getenv("FLOWER_OAUTH2_SECRET", None):
    oauth2_secret = FLOWER_OAUTH2_SECRET
    print(f"FLOWER_OAUTH2_SECRET: ".ljust(40) + str(oauth2_secret))
else:
    print(f"FLOWER_OAUTH2_SECRET: ".ljust(40) + "(default)")
del FLOWER_OAUTH2_SECRET

if FLOWER_REDIRECT_URI := os.getenv("FLOWER_REDIRECT_URI", None):
    redirect_uri = FLOWER_REDIRECT_URI
    print(f"FLOWER_REDIRECT_URI: ".ljust(40) + str(redirect_uri))
else:
    print(f"FLOWER_REDIRECT_URI: ".ljust(40) + "(default)")
del FLOWER_REDIRECT_URI
