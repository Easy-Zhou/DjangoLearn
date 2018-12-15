# 此文件用于自定义类型转换器，例子如下：
# 使用方法为在urls.py中通过  django.urls.register_converter(converters.FourDigitYearConverter,'yyyy') 来注册转换器并使用

class FourDigitYearConverter:
    """
    4位数字年份转换器，其中必须含有如下三部分
    """
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
