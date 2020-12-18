# Basic Matchers(基本匹配)
##### https://github.com/ziishaned/learn-regex/blob/master/translations/README-zh-simple.md

### 在Python里面使用re模块

```python
import re
# 常用match和search方法 其它的在标准库文件里面详细介绍
# match的第一个参数是用正则表达式格式的参数 第二个参数是需要匹配的字符串 第三个是标志位可以忽略
print(re.match(r'www', 'www.runoob.com'))  # <_sre.SRE_Match object; span=(0, 3), match='www'>
```
基本匹配就是指没有使用正则的规则，匹配什么就写什么