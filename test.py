from noolite_api import NooliteSerial, dispatch_command
import asyncio


@dispatch_command
async def test_callback(t):
    print(t)


nl = NooliteSerial(tty_name='test', input_command_callback_method=test_callback)


async def main():
    nl.start_listen()
    nl.send_api('on', 1)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
