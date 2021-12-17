from loguru import logger
# -*- coding: utf-8 -*-
# @Author: Nriver
# @Date:   2021-12-17 14:02:53
# @Last Modified by:   Nriver
# @Last Modified time: 2021-12-17 14:54:55

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

for x in range(5):
    logger.info(f'{x, a, b}')
