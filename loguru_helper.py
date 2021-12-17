import re
import sys

from loguru import logger


def convert_print_to_logger_info(input_file, output_file):
    new_content = 'from loguru import logger\n'

    # print 批量替换成 loguru的logger.info
    # replace all print with logger.info for loguru module

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if any(line.strip().startswith(keyword) for keyword in ['print(', '# print(']):

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
                elif not ('"' in line or "'" in line):
                    # 没有引号的直接用 单引号括起来 再加f-string
                    # string without ' or "
                    new_line = re.sub('print\((.*?)\)', "logger.info(f'{(\\1)}')", line)
                else:
                    # other cases
                    logger.error('unrecognized case !')
                    logger.error(line)
                    exit()

                # 移除多余的括号
                # remove redundant brackets
                new_line = new_line.replace('{(', '{')
                new_line = new_line.replace(')}', '}')

                new_content += new_line
            else:
                new_content += line

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        convert_print_to_logger_info('target_file.py', 'target_file_mod.py')
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
        if not '.py' in input_file:
            sys.exit()
        output_file = input_file.replace('.py', '_mod.py')
        convert_print_to_logger_info(input_file, output_file)

    logger.info('finish')
