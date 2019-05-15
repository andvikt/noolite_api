from noolite_api import NooliteSerial, dispatch_command
import asyncio


async def test_callback(t):
    print(f'Callback {t}')

nl = NooliteSerial(tty_name='test')
nl.reg_callback(1, test_callback)

async def main():
    nl.start_listen()
    nl.send_api('on', 1)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
