# Common Config
TOPIC = "nginx-access-log-compressed"
BOOTSTRAP_SERVER = ['host.docker.internal:9092']

# Producer code related config
INPUT_FILE = "<provide absolute path of access.log here>"
COMPRESSION_TYPE = "gzip"
LINGER_MS = 0
BATCH_SIZE = 16384

# Consumer code related config
GROUP_ID = "nginx-access-log-cg"
