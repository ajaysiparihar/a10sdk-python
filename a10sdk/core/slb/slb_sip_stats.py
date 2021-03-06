from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param msg_proxy_client_incomplete: {"description": "Number of packet which contains incomplete message", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param msg_proxy_server_drop: {"description": "Number of AX drop", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param msg_proxy_server_fail: {"description": "Number of SIP messages received from server but failed to forward to client", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param msg_proxy_create_server_conn: {"description": "Number of server connection system tries to create", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param msg_proxy_start_server_conn: {"description": "Number of server connection created successfully", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param msg_proxy_server_incomplete: {"description": "Number of packet which contains incomplete message", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param msg_proxy_server_send_success: {"description": "Number of SIP messages received from server and forwarded to client", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param session_freed: {"description": "SIP Session freed", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param msg_proxy_fail_start_server_conn: {"description": "Number of server connection create failed", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param msg_proxy_client_send_success: {"description": "Number of SIP messages received from client and forwarded to server", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param session_created: {"description": "SIP Session created", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param msg_proxy_client_drop: {"description": "Number of AX drop", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param msg_proxy_total: {"description": "Total number of sip proxy connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param msg_proxy_server_recv: {"description": "Number of SIP messages received from server", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param msg_proxy_client_fail: {"description": "Number of SIP messages received from client but failed to forward to server", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param msg_proxy_client_connection: {"description": "Connecting server", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param msg_proxy_current: {"description": "Number of current sip proxy connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param msg_proxy_client_recv: {"description": "Number of SIP messages received from client", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.msg_proxy_client_incomplete = ""
        self.msg_proxy_server_drop = ""
        self.msg_proxy_server_fail = ""
        self.msg_proxy_create_server_conn = ""
        self.msg_proxy_start_server_conn = ""
        self.msg_proxy_server_incomplete = ""
        self.msg_proxy_server_send_success = ""
        self.session_freed = ""
        self.msg_proxy_fail_start_server_conn = ""
        self.msg_proxy_client_send_success = ""
        self.session_created = ""
        self.msg_proxy_client_drop = ""
        self.msg_proxy_total = ""
        self.msg_proxy_server_recv = ""
        self.msg_proxy_client_fail = ""
        self.msg_proxy_client_connection = ""
        self.msg_proxy_current = ""
        self.msg_proxy_client_recv = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sip(A10BaseClass):
    
    """Class Description::
    Statistics for the object sip.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/sip/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/slb/sip/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


