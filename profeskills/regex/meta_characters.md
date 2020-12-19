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
