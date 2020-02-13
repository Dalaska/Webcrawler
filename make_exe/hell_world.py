# https://zhuanlan.zhihu.com/p/45288707
# pip install pyinstaller
# pyinstaller -F hell_world.py
'''
其中，-F 表示打包成单独的 .exe 文件，这时生成的 .exe 文件会比较大，而且运行速度回较慢。仅仅一个 helloworld 程序，生成的文件就 5MB 大。
另外，使用 -i 还可以指定可执行文件的图标； -w 表示去掉控制台窗口，这在 GUI 界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
'''
print('hell world')