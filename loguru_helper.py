import os.path
import re
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QTextBrowser
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

                # 已经是 f-string 的就只替换print, 跳过后续的处理
                # already a f-string
                skip = False
                if 'print(f"' in line or "print(f'" in line or 'f"{' in line or "f'{" in line:
                    new_line = line.replace('print', 'logger.info')
                    skip = True
                elif "'" in line:
                    # 有单引号的用双引号括起来 再加f-string
                    # string with ' inside
                    new_line = re.sub('print\((.*)\)', 'logger.info(f"{(\\1)}")', line)
                elif '"' in line:
                    # 有双引号的用单引号括起来 再加f-string
                    # string with " inside
                    new_line = re.sub('print\((.*)\)', "logger.info(f'{(\\1)}')", line)
                elif not ('"' in line or "'" in line):
                    # 没有引号的直接用 单引号括起来 再加f-string
                    # string without ' or "
                    new_line = re.sub('print\((.*)\)', "logger.info(f'{(\\1)}')", line)
                else:
                    # other cases
                    logger.error('unrecognized case !')
                    logger.error(line)
                    exit()

                if not skip:
                    # 移除多余的括号
                    # remove redundant brackets
                    new_line = new_line.replace('{(', '{')
                    new_line = new_line.replace(')}', '}')

                new_content += new_line
            else:
                new_content += line

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'loguru转换工具 v1.0 by Nriver'
        self.add_suffix = True
        self.init_user_interface()

    def init_user_interface(self):
        self.setWindowTitle(self.title)
        self.resize(300, 180)

        # 窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 开启接受拖入事件
        self.setAcceptDrops(True)

        grid = QGridLayout()

        # 文字框
        self.text_browser = QTextBrowser()
        self.text_browser.setAcceptDrops(True)

        # 选项
        self.check_box_add_suffix = QCheckBox('添加后缀')
        self.check_box_add_suffix.setChecked(self.add_suffix)
        self.check_box_add_suffix.clicked.connect(self.set_add_suffix)

        grid.addWidget(self.text_browser, 0, 0)
        grid.addWidget(self.check_box_add_suffix, 1, 0)

        self.setLayout(grid)
        self.show()

    def set_add_suffix(self):
        self.add_suffix = not self.add_suffix
        logger.info(f"添加后缀 {self.add_suffix}")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ingore()

    def dropEvent(self, event):
        # 获取文件路径
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path):
                process_file(path, self.add_suffix)
            else:
                for root, dirs, files in os.walk(".", topdown=False):
                    for name in files:
                        input_path = os.path.join(root, name).replace('\\', '/')
                        process_file(input_path, self.add_suffix)


def process_file(input_file, add_suffix=True):
    if not ('.py' in input_file and input_file[-3:] == '.py'):
        logger.info(f'忽略 {input_file}')
        return
    logger.info(f'处理 {input_file}')
    if add_suffix:
        output_file = input_file.replace('.py', '_mod.py')
    else:
        output_file = input_file
    convert_print_to_logger_info(input_file, output_file)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # convert_print_to_logger_info('target_file.py', 'target_file_mod.py')
        logger.info('无参数, 启动pyqt界面')
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

    elif len(sys.argv) == 2:
        process_file(sys.argv[1])

    logger.info('程序结束')
