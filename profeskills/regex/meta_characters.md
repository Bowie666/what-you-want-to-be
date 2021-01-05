# Meta Characters(元字符)
- 这里就开始真正的正则匹配了

## 一 点运算符 **.** The Full Stop(句号)
- **.** 是元字符中最简单的例子. **.** 匹配任意单个字符, 但不匹配换行符. 例如, 表达式 **.** ar匹配一个任意字符后面跟着是a和r的字符串.
```python
import re

re.findall(r'.ar', 'The car parked in the garage.')
# ['car', 'par', 'gar']
```

## 二 字符集 [ ] character sets
- 字符集也叫做字符类. 方括号用来指定一个字符集. 在方括号中使用连字符来指定字符集的范围. 在方括号中的字符集不关心顺序. 例如, 表达式[Tt]he 匹配 the 和 The.

```python
import re

re.findall(r'ar[.a]', 'The car parked in the garage.')
# ['ar.', 'ara']
```

## 三 否定字符集 ^ Negated Character Sets
- 一般来说 ^ 表示一个字符串的开头, 但它用在一个方括号的开头的时候, 它表示这个字符集是否定的. 例如, 表达式[^c]ar 匹配一个后面跟着ar的除了c的任意字符.

```python
import re

re.findall(r'[^c]ar', 'The car parked in the garage.')
# ['par', 'gar']
```

## 四 重复次数
> ### * 号 The Star
>> \* 号匹配在 * 之前的字符出现大于等于0次.
```python
import re

print(re.findall(r'[a-z]*', 'The car parked in the garage.'))
# ['', 'he', '', 'car', '', 'parked', '', 'in', '', 'the', '', 'garage', '', '']
```
> ### + 号 The Plus
>> +号匹配+号之前的字符出现 >=1 次个字符
```python
import re

print(re.findall(r'c.+t', 'The fat cat sat on the mat.'))
print(re.findall(r'c.+t', 'The fat cat sat on the .'))
# ['cat sat on the mat']
# ['cat sat on t']
```
> ### ? 号 The Question Mark
>> 在正则表达式中元字符 ? 标记在符号前面的字符为可选 即出现 0 或 1 次
```python
import re

print(re.findall(r'[T]?he', 'The car is parked in the garage.'))
# ['The', 'he']
```
> ### {} 号 Braces
>> 在正则表达式中 {} 是一个量词, 常用来一个或一组字符可以重复出现的次数
```python
import re

print(re.findall(r'[0-9]{2,3}', 'The number was 9.9997 but we rounded it off to 10.0.'))
# 不加后面的范围就是说最低2位  高了不限
print(re.findall(r'[0-9]{2,}', 'The number was 9.9997 but we rounded it off to 10.0.'))
# ['999', '10']
# ['9997', '10']
```
> ### (...) 特征标群 Capturing Groups .
>> 特征标群是一组写在 (...) 中的子模式
- (xyz)字符集, 匹配与 xyz 完全相等的字符串
```python
# 这个拉闸了 python 中使用括号不管用
import re

print(re.findall(r'(ar)', 'The car is parked in the garage.'))
# ['ar', 'ar', 'ar']
```
> ### | 或运算符 Alternation
>> 特征标群是一组写在 (...) 中的子模式
```python
import re

print(re.findall(r'he|car', 'The car is parked in the garage.'))
# ['he', 'car', 'he']
```
> ### \ 转码特殊字符
>> 特征标群是一组写在 (...) 中的子模式

> ### 锚点 Anchors
>> ^ 号
>>> ^ 用来检查匹配的字符串是否在所匹配字符串的开头.
```python
import re

print(re.findall(r'^[Tt]he', 'The car is parked in the garage.'))
# ['The']
```
>> $ 号
>>>$ 号用来匹配字符是否是最后一个.
```python
import re

print(re.findall(r'(at\.)$', 'The fat cat. sat. on the mat.'))
# ['at.']
```