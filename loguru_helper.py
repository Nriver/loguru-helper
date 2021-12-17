# -*- coding: utf-8 -*-
# @Author: Nriver
# @Date:   2021-12-17 14:02:53
# @Last Modified by:   Nriver
# @Last Modified time: 2021-12-17 14:55:56
import os
import re
from loguru import logger

new_content = 'from loguru import logger\n'

# print 批量替换成 loguru的logger.info
# replace all print with logger.info for loguru module

with open(r'target_file.py', 'r', encoding='utf-8') as f:
    for line in f:
        if any(line.strip().startswith(keyword) for keyword in ['print(', '# print(']):

            switch = 10
            switch = 20

            if switch == 10:
                # 暴力替换, 用tuple括起来
                # simple quote everything with tuple
                new_line = re.sub('print\((.*?)\)', 'logger.info((\\1))', line)
            elif switch == 20:
                # 用 f-string 替换
                # replace with f-string

                # 已经是 f-string 的就只替换print
                # already a f-string
                if 'f"{' in line or "f'{" in line:
                    new_line = line.replace('print', 'logger.info')
                elif "'" in line:
                    # 有单引号的用双引号括起来 再加f-string
                    # string with ' inside
                    new_line = re.sub('print\((.*?)\)', 'logger.info(f"{(\\1)}")', line)
                elif '"' in line:
                    # 有双引号的用单引号括起来 再加f-string
                    # string with " inside
                    new_line = re.sub('print\((.*?)\)', "logger.info(f'{(\\1)}')", line)
                elif not('"' in line or "'" in line):
                    # 没有引号的直接用 单引号括起来 再加f-string
                    # string without ' or "
                    new_line = re.sub('print\((.*?)\)', "logger.info(f'{(\\1)}')", line)
                else:
                    # other cases
                    logger.error(line)
                    logger.error('异常')
                    exit()
                new_line = new_line.replace('{(', '{')
                new_line = new_line.replace(')}', '}')

            new_content += new_line
        else:
            new_content += line


with open('target_file_mod.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

os.system('target_file_mod.py')
