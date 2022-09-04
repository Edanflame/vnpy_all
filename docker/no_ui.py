""""""
from time import sleep
from logging import INFO
import os

from vnpy.event import EventEngine
from vnpy.trader.setting import SETTINGS
from vnpy.trader.engine import MainEngine, LogEngine

from dotenv import load_dotenv
from vnpy_ctp import CtpGateway
from vnpy_rpcservice import RpcServiceApp
from vnpy_rpcservice.rpc_service.engine import EVENT_RPC_LOG, RpcEngine


SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True


load_dotenv()


ctp_setting = {
    "用户名": os.getenv("USERID"),
    "密码": os.getenv("PASSWORD"),
    "经纪商代码": os.getenv("BROKERID"),
    "交易服务器": os.getenv("TD_ADDRESS"),
    "行情服务器": os.getenv("MD_ADDRESS"),
    "产品名称": os.getenv("APPID"),
    "授权编码": os.getenv("AUTH_CODE")
}

rpc_address = {
    "rep_address": "tcp://*:2014",
    "pub_address": "tcp://*:4102"
}

def main():
    """"""
    SETTINGS["log.file"] = True

    event_engine: EventEngine = EventEngine()
    main_engine: MainEngine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)
    rpc_engine: RpcEngine = main_engine.add_app(RpcServiceApp)
    main_engine.write_log("主引擎创建成功")

    log_engine: LogEngine = main_engine.get_engine("log")
    event_engine.register(EVENT_RPC_LOG, log_engine.process_log_event)
    main_engine.write_log("注册日志事件监听")

    main_engine.connect(ctp_setting, "CTP")
    main_engine.write_log("连接CTP接口")

    sleep(10)

    rpc_engine.start(
        rep_address=rpc_address["rep_address"],
        pub_address=rpc_address["pub_address"]
    )


if __name__ == "__main__":
    main()