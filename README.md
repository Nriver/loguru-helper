# loguru-helper
将python的print语句批量替换成loguru的logger.info
replace all print with logger.info for loguru module

# 使用方法
可以用[Release](https://github.com/Nriver/loguru-helper/releases)里面打包的exe
把`.py`文件拖到exe上就会进行转换, 会在目标文件同目录下生成一个 `_mod.py` 结尾的文件

# 使用命令行调用
可以用命令行运行

将同目录下的 `target_file.py` 转换成 `target_file_mod.py`
```
python3 loguru_helper.py
```

转换其它文件
```
python3 loguru_helper.py target_file.py
```
会在目标文件同目录下生成一个 `_mod.py` 结尾的文件



