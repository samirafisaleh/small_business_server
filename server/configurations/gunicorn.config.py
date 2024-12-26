# https://docs.gunicorn.org/en/latest/settings.html#settings


import os
from dotenv import load_dotenv

load_dotenv(override=True)


#############################################
# Config File
#############################################
# config
# wsgi_app

#############################################
# Debugging
#############################################

if GUNICORN_RELOAD := os.getenv("GUNICORN_RELOAD", None):
    GUNICORN_RELOAD = bool(int(GUNICORN_RELOAD))
    reload = GUNICORN_RELOAD
del GUNICORN_RELOAD

if GUNICORN_RELOAD_ENGINE := os.getenv("GUNICORN_RELOAD_ENGINE", None):
    reload_engine = GUNICORN_RELOAD_ENGINE
del GUNICORN_RELOAD_ENGINE

# reload_extra_files

if GUNICORN_SPEW := os.getenv("GUNICORN_SPEW", None):
    GUNICORN_SPEW = bool(int(GUNICORN_SPEW))
    spew = GUNICORN_SPEW
del GUNICORN_SPEW


if GUNICORN_CHECK_CONFIG := os.getenv("GUNICORN_CHECK_CONFIG", None):
    GUNICORN_CHECK_CONFIG = bool(int(GUNICORN_CHECK_CONFIG))
    check_config = GUNICORN_CHECK_CONFIG
del GUNICORN_CHECK_CONFIG

if GUNICORN_PRINT_CONFIG := os.getenv("GUNICORN_PRINT_CONFIG", None):
    GUNICORN_PRINT_CONFIG = bool(int(GUNICORN_PRINT_CONFIG))
    print_config = GUNICORN_PRINT_CONFIG
del GUNICORN_PRINT_CONFIG

#############################################
# Logging
#############################################

if GUNICORN_ACCESSLOG := os.getenv("GUNICORN_ACCESSLOG", None):
    accesslog = GUNICORN_ACCESSLOG
del GUNICORN_ACCESSLOG

if GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG := os.getenv(
    "GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG", None
):
    GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG = bool(
        int(GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG)
    )
    disable_redirect_access_to_syslog = GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG
del GUNICORN_DISABLE_REDIRECT_ACCESS_TO_SYSLOG


# access_log_format

if GUNICORN_ERRORLOG := os.getenv("GUNICORN_ERRORLOG", None):
    errorlog = GUNICORN_ERRORLOG
del GUNICORN_ERRORLOG


if GUNICORN_LOGLEVEL := os.getenv("GUNICORN_LOGLEVEL", None):
    loglevel = GUNICORN_LOGLEVEL
del GUNICORN_LOGLEVEL

if GUNICORN_CAPTURE_OUTPUT := os.getenv("GUNICORN_CAPTURE_OUTPUT", None):
    GUNICORN_CAPTURE_OUTPUT = bool(int(GUNICORN_CAPTURE_OUTPUT))
    capture_output = GUNICORN_CAPTURE_OUTPUT
del GUNICORN_CAPTURE_OUTPUT

if GUNICORN_LOGGER_CLASS := os.getenv("GUNICORN_LOGGER_CLASS", None):
    logger_class = GUNICORN_LOGGER_CLASS
del GUNICORN_LOGGER_CLASS

if GUNICORN_LOGCONFIG := os.getenv("GUNICORN_LOGCONFIG", None):
    logconfig = GUNICORN_LOGCONFIG
del GUNICORN_LOGCONFIG


# logconfig_dict

if GUNICORN_LOGCONFIG_JSON := os.getenv("GUNICORN_LOGCONFIG_JSON", None):
    logconfig_json = GUNICORN_LOGCONFIG_JSON
del GUNICORN_LOGCONFIG_JSON

if GUNICORN_SYSLOG_ADDR := os.getenv("GUNICORN_SYSLOG_ADDR", None):
    syslog_addr = GUNICORN_SYSLOG_ADDR
del GUNICORN_SYSLOG_ADDR

if GUNICORN_SYSLOG := os.getenv("GUNICORN_SYSLOG", None):
    GUNICORN_SYSLOG = bool(int(GUNICORN_SYSLOG))
    syslog = GUNICORN_SYSLOG
del GUNICORN_SYSLOG


if GUNICORN_SYSLOG_PREFIX := os.getenv("GUNICORN_SYSLOG_PREFIX", None):
    syslog_prefix = GUNICORN_SYSLOG_PREFIX
del GUNICORN_SYSLOG_PREFIX

if GUNICORN_SYSLOG_FACILITY := os.getenv("GUNICORN_SYSLOG_FACILITY", None):
    syslog_facility = GUNICORN_SYSLOG_FACILITY
del GUNICORN_SYSLOG_FACILITY


if GUNICORN_ENABLE_STDIO_INHERIT := os.getenv("GUNICORN_ENABLE_STDIO_INHERIT", None):
    GUNICORN_ENABLE_STDIO_INHERIT = bool(int(GUNICORN_ENABLE_STDIO_INHERIT))
    enable_stdio_inheritance = GUNICORN_ENABLE_STDIO_INHERIT
del GUNICORN_ENABLE_STDIO_INHERIT

if GUNICORN_STATSD_HOST := os.getenv("GUNICORN_STATSD_HOST", None):
    statsd_host = GUNICORN_STATSD_HOST
del GUNICORN_STATSD_HOST

if GUNICORN_DOGSTATSD_TAGS := os.getenv("GUNICORN_DOGSTATSD_TAGS", None):
    dogstatsd_tags = GUNICORN_DOGSTATSD_TAGS
del GUNICORN_DOGSTATSD_TAGS

if GUNICORN_STATSD_PREFIX := os.getenv("GUNICORN_STATSD_PREFIX", None):
    statsd_prefix = GUNICORN_STATSD_PREFIX
del GUNICORN_STATSD_PREFIX


#############################################
# Process Naming
#############################################

if GUNICORN_PROC_NAME := os.getenv("GUNICORN_PROC_NAME", None):
    proc_name = GUNICORN_PROC_NAME
del GUNICORN_PROC_NAME


if GUNICORN_DEFAULT_PROC_NAME := os.getenv("GUNICORN_DEFAULT_PROC_NAME", None):
    default_proc_name = GUNICORN_DEFAULT_PROC_NAME
del GUNICORN_DEFAULT_PROC_NAME


#############################################
# SSL
#############################################

if GUNICORN_KEYFILE := os.getenv("GUNICORN_KEYFILE", None):
    keyfile = GUNICORN_KEYFILE
del GUNICORN_KEYFILE

if GUNICORN_CERTFILE := os.getenv("GUNICORN_CERTFILE", None):
    certfile = GUNICORN_CERTFILE
del GUNICORN_CERTFILE


# ssl_version
# cert_reqs

if GUNICORN_CA_CERTS := os.getenv("GUNICORN_CA_CERTS", None):
    ca_certs = GUNICORN_CA_CERTS
del GUNICORN_CA_CERTS

# suppress_ragged_eofs
# do_handshake_on_connect
# ciphers


#############################################
# Security
#############################################

if GUNICORN_LIMIT_REQUEST_LINE := os.getenv("GUNICORN_LIMIT_REQUEST_LINE", None):
    GUNICORN_LIMIT_REQUEST_LINE = int(GUNICORN_LIMIT_REQUEST_LINE)
    limit_request_line = GUNICORN_LIMIT_REQUEST_LINE
del GUNICORN_LIMIT_REQUEST_LINE

if GUNICORN_LIMIT_REQUEST_FIELDS := os.getenv("GUNICORN_LIMIT_REQUEST_FIELDS", None):
    GUNICORN_LIMIT_REQUEST_FIELDS = int(GUNICORN_LIMIT_REQUEST_FIELDS)
    limit_request_fields = GUNICORN_LIMIT_REQUEST_FIELDS
del GUNICORN_LIMIT_REQUEST_FIELDS


if GUNICORN_LIMIT_REQUEST_SIZE := os.getenv("GUNICORN_LIMIT_REQUEST_SIZE", None):
    GUNICORN_LIMIT_REQUEST_SIZE = int(GUNICORN_LIMIT_REQUEST_SIZE)
    limit_request_field_size = GUNICORN_LIMIT_REQUEST_SIZE
del GUNICORN_LIMIT_REQUEST_SIZE


#############################################
# Server Hooks
#############################################


def on_starting(server):
    """Function"""
    print(f"On Starting: {server}")


def on_reload(server):
    """Function"""
    print(f"On Reload: {server}")


def when_ready(server):
    """Function"""
    print(f"When Ready: {server}")


def pre_fork(server, worker):
    """Function"""
    print(f"Pre Fork: {server}")
    print(f"Pre Fork: {worker}")


def post_fork(server, worker):
    """Function"""
    print(f"Post Fork: {server}")
    print(f"Post Fork: {worker}")


def post_worker_init(worker):
    """Function"""
    print(f"Post Worker Init: {worker}")


def worker_int(worker):
    """Function"""
    print(f"Worker Int: {worker}")


def worker_abort(worker):
    """Function"""
    print(f"Worker Abort: {worker}")


def pre_exec(server):
    """Function"""
    print(f"Pre Exec: {server}")


def pre_request(worker, req):
    """Function"""
    print(f"Pre Request: {worker}")
    print(f"Pre Request: {req}")


def post_request(worker, req, environ, resp):
    """Function"""
    print(f"Pre Request: {worker}")
    print(f"Pre Request: {req}")
    print(f"Pre Request: {environ}")
    print(f"Pre Request: {resp}")


def child_exit(server, worker):
    """Function"""
    print(f"Child Exit: {server}")
    print(f"Child Exit: {worker}")


def worker_exit(server, worker):
    """Function"""
    print(f"Worker Exit: {server}")
    print(f"Worker Exit: {worker}")


def nworkers_changed(server, new_value, old_value):
    """Function"""
    print(f"NWorkers Changed: {server}")
    print(f"NWorkers Changed: Old Value: {old_value}")
    print(f"NWorkers Changed: New Value: {new_value}")


def on_exit(server):
    """Function"""
    print(f"On Exit: {server}")


def ssl_context(config, default_ssl_context_factory):
    """Function"""
    print(f"SSL Context: {config}")
    return default_ssl_context_factory()


#############################################
# Server Mechanics
#############################################

if GUNICORN_PRELOAD_APP := os.getenv("GUNICORN_PRELOAD_APP", None):
    GUNICORN_PRELOAD_APP = bool(int(GUNICORN_PRELOAD_APP))
    preload_app = GUNICORN_PRELOAD_APP
del GUNICORN_PRELOAD_APP


# sendfile

if GUNICORN_REUSE_PORT := os.getenv("GUNICORN_REUSE_PORT", None):
    GUNICORN_REUSE_PORT = bool(int(GUNICORN_REUSE_PORT))
    reuse_port = GUNICORN_REUSE_PORT
del GUNICORN_REUSE_PORT


# chdir

if GUNICORN_DAEMON := os.getenv("GUNICORN_DAEMON", None):
    GUNICORN_DAEMON = bool(int(GUNICORN_DAEMON))
    daemon = GUNICORN_DAEMON
del GUNICORN_DAEMON


# raw_env

if GUNICORN_PIDFILE := os.getenv("GUNICORN_PIDFILE", None):
    pidfile = GUNICORN_PIDFILE
del GUNICORN_PIDFILE


# worker_tmp_dir
# user
# group


if GUNICORN_UMASK := os.getenv("GUNICORN_UMASK", None):
    GUNICORN_UMASK = int(GUNICORN_UMASK)
    umask = GUNICORN_UMASK
del GUNICORN_UMASK


if GUNICORN_INITGROUPS := os.getenv("GUNICORN_INITGROUPS", None):
    GUNICORN_INITGROUPS = int(GUNICORN_INITGROUPS)
    initgroups = GUNICORN_INITGROUPS
del GUNICORN_INITGROUPS


# tmp_upload_dir
# secure_scheme_headers
# forwarded_allow_ips
# pythonpath
# paste
# proxy_protocol
# proxy_allow_ips
# raw_paste_global_conf
# strip_header_spaces
# permit_unconventional_http_method
# permit_unconventional_http_version
# casefold_http_method
# header_map
# tolerate_dangerous_framing
#############################################
# Server Socket
#############################################

if GUNICORN_BIND := os.getenv("GUNICORN_BIND", None):
    bind = GUNICORN_BIND
del GUNICORN_BIND

if GUNICORN_BACKLOG := os.getenv("GUNICORN_BACKLOG", None):
    GUNICORN_BACKLOG = int(GUNICORN_BACKLOG)
    backlog = GUNICORN_BACKLOG
del GUNICORN_BACKLOG


#############################################
# Worker Processes
#############################################

if GUNICORN_WORKERS := os.getenv("GUNICORN_WORKERS", None):
    GUNICORN_WORKERS = int(GUNICORN_WORKERS)
    workers = GUNICORN_WORKERS
del GUNICORN_WORKERS


if GUNICORN_WORKER_CLASS := os.getenv("GUNICORN_WORKER_CLASS", None):
    worker_class = GUNICORN_WORKER_CLASS
del GUNICORN_WORKER_CLASS

if GUNICORN_THREADS := os.getenv("GUNICORN_THREADS", None):
    GUNICORN_THREADS = int(GUNICORN_THREADS)
    threads = GUNICORN_THREADS
del GUNICORN_THREADS


if GUNICORN_WORKER_CONNECTIONS := os.getenv("GUNICORN_WORKER_CONNECTIONS", None):
    GUNICORN_WORKER_CONNECTIONS = int(GUNICORN_WORKER_CONNECTIONS)
    worker_connections = GUNICORN_WORKER_CONNECTIONS
del GUNICORN_WORKER_CONNECTIONS


if GUNICORN_MAX_REQUESTS := os.getenv("GUNICORN_MAX_REQUESTS", None):
    GUNICORN_MAX_REQUESTS = int(GUNICORN_MAX_REQUESTS)
    max_requests = GUNICORN_MAX_REQUESTS
del GUNICORN_MAX_REQUESTS


# max_requests_jitter

if GUNICORN_TIMEOUT := os.getenv("GUNICORN_TIMEOUT", None):
    GUNICORN_TIMEOUT = int(GUNICORN_TIMEOUT)
    timeout = GUNICORN_TIMEOUT
del GUNICORN_TIMEOUT


if GUNICORN_GRACEFUL_TIMEOUT := os.getenv("GUNICORN_GRACEFUL_TIMEOUT", None):
    GUNICORN_GRACEFUL_TIMEOUT = int(GUNICORN_GRACEFUL_TIMEOUT)
    graceful_timeout = GUNICORN_GRACEFUL_TIMEOUT
del GUNICORN_GRACEFUL_TIMEOUT


if GUNICORN_KEEPALIVE := os.getenv("GUNICORN_KEEPALIVE", None):
    GUNICORN_KEEPALIVE = int(GUNICORN_KEEPALIVE)
    keepalive = GUNICORN_KEEPALIVE
del GUNICORN_KEEPALIVE
