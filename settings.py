
# Loguru settings
# here is Loguru settings which will be added in loguru-set file

LOGGING = {
    "file": {
        "path": "logs.log",
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        "rotation": "1 day",
        "compression": "zip",
        "retention": "30 days",
        "serialize": False
    },

    "terminal": {
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    }
}
