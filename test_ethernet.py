from noolite_api import NooliteEthernet, dispatch_command
import asyncio


async def test_callback(t):
    print(t)


nl = NooliteEthernet(host='192.168.0.1', update_interval=30, cb_sensors=test_callback)


async def main():
    nl.start_listen()
    nl.send_api('on', 1)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
