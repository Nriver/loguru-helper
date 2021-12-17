# loguru-helper
将python的print语句批量替换成loguru的logger.info
replace all print with logger.info for loguru module

# 使用

将同目录下的 `target_file.py` 转换成 `target_file_mod.py`
```
python3 loguru_helper.py
```

转换其它文件
```
python3 loguru_helper.py target_file.py
```
会在目标文件同目录下生成一个 _mod.py 结尾的文件



