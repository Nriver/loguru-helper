from loguru import logger
# sample python file with some print

a = 'aaa'
b = 'bbb'

logger.info(f"{'111'}")
logger.info(f'{a}')
logger.info(f'{a, b}')
logger.info(f"{'111', a}")
logger.info(f'{"111", a}')
logger.info(f"{a, '111'}")
logger.info(f'{a, "111"}')
logger.info(f'{111, a}')
logger.info(f'{a, 111}')
logger.info(f'{a, b, 111}')
logger.info(f'{a, 111, b}')
logger.info(f'{a}')
logger.info(f'{a, b}')
logger.info(f'{a, b} 111')
# logger.info(f'{a, b} 111')
logger.info(f"{'loguru_convert()', a}")

for x in range(5):
    logger.info(f'{x, a, b}')
