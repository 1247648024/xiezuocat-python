# xiezuocat-python

封装写作猫智能纠错，智能改写API，提供单点登录签名算法实现

# 第一步：安装xiezuocat模块

pip install xiezuocat

# 第二部：引入模块，传入secret_key调用api，调用示例如下：

```python

import xiezuocat
import json

if __name__ == '__main__':
    my_xiezuocat = xiezuocat.Xiezuocat('xx')

    check_data = json.dumps({
                "texts": [
                    "哈哈哈。我天今吃了一顿饭",
                    "我想念十分赵忠祥。嘿嘿嘿。"
                ]
            })
    check_result = my_xiezuocat.check(check_data)
    print("check_result === ", check_result)

    rewrite_data = json.dumps({
      "items": [
        "一般"
      ],
      "level": "middle"
    })
    rewrite_result = my_xiezuocat.rewrite(rewrite_data)
    print("rewrite_result === ", rewrite_result)

    sign_result = my_xiezuocat.signature("xxx", "ll")
    print("sign_result === ", sign_result)


```
