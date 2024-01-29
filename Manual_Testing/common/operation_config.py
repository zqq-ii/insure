# This Python file uses the following encoding: utf-8
from configparser import ConfigParser
import os


class Config:
    def __init__(self, filename):
        base_path = os.path.dirname(os.path.dirname(__file__)) + "/config"  # 配置文件的所有文件夹目录
        self._filepath = os.path.join(base_path, filename)  # 文件路径+文件名
        self.config = ConfigParser()
        self.config.read(self._filepath)  # 读配置文件

    def get_value(self, section, option):
        """
        获取配置文件中的值,如果section和option都存在则返回option对应的值,否则返回None
        :param section: 节点
        :param option: 节点内的选项
        :return:
        """
        if self.config.has_section(section):  # 判读节点是否在文件中
            try:
                return self.config.get(section=section, option=option)  # 读取对应值
            except:
                print(f"{option}选项不存在")
                return None
        else:
            print(f"{section}节点不存在")
            return None

    def set_value(self, section, option, value=None):
        """
        更新配置文件中的值
        :param section: 节点
        :param option: 节点内的选项
        :return:
        """
        if not self.config.has_section(section):  # 判断节点是否存在
            self.config.add_section(section=section)  # 新增对应节点
        self.config.set(section=section, option=option, value=value)  # 更新对应节点-选项的值
        with open(self._filepath, "r+") as fp:
            self.config.write(fp=fp)  # 提交结果


if __name__ == '__main__':
    """
    cf = Config("config.ini")
    print(cf.get_value("test", "host"))
    print(cf.get_value("test","headers"))
    print(cf.set_value("test", "headers"))
    """
