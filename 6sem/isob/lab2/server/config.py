TARGET_SERVICE_PORT = 9090
TARGET_SERVER_NAME = 'target_server'
TARGET_SERVER_KEY = 'target_ket'

KDC_PASSWORD = 'kdc_password'
KDC_SERVER_PORT = 8888
KDC_SERVER_NAME = 'kdc_server'
KDC_SERVER_TICKET_PERIOD = 24 * 3600

TICKET_GRANTING_SERVER_PORT = 9092
TICKET_GRANTING_SERVER_NAME = 'tgs_server'
TICKET_GRANTING_SERVER_KEY = 'ticket_key'

CLIENT_HOST = 'localhost'
CLIENT_TARGET_SERVER_ADDRESS = (CLIENT_HOST, TARGET_SERVICE_PORT)
CLIENT_KDC_SERVER_ADDRESS = (CLIENT_HOST, KDC_SERVER_PORT)
CLIENT_TICKET_GRANTING_SERVER_ADDRESS = (CLIENT_HOST,  TICKET_GRANTING_SERVER_PORT)


DEFAULT_USERS = {'default_user': 'default_user'}