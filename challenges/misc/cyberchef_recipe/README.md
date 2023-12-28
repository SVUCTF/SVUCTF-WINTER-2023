# 蟹皇堡秘方

- 作者：13m0n4de
- 参考：-
- 难度：Normal
- 分类：Misc
- 镜像：-
- 端口：-

## 题目描述

痞老板：「凯伦，接着，刚刚偷到的蟹皇堡」\
凯伦：「你知道的吧，光有......」\
痞老板：「当然，这次我还偷偷记录下了制作过程」

## 题目解析

得承认，这题出得不行，让太多选手以为是消耗寿命的手搓题，下次得出个超过百年寿命的。

[recipe](./attachments/recipe) 的内容，其实是 CyberChef 的“菜谱”，意为加解密的全部过程，可以以各种形式导入导出。

这题是默认的 `CHEF FORMAT` ，本来想做 JSON 格式的，考验一下大家的编码水平，但怕没人认出来是 CyberChef 就还是用了默认的。

考点是替换字符串，将加密的 recipe 换成解密的 recipe，再导入 CyberChef 解密。

大概规则如下：

```
To                         -> From
Encode                     -> Decode
Encrypt                    -> Decrypt
ROT47(47)                  -> ROT47(-47)
ROT47(40)                  -> ROT47(-40)
ROT13(true,false,false,15) -> ROT13(true,false,false,-15)
```

至于 `Reverse` 、`Rc4` 、`ROT13(true,true,false,13)` 什么的，保持原样就好。

**最后不要忘记将替换后的文本按行倒序。**

能这么直接替换的原因是，CyberChef 各个模块加解密的格式基本不太变化，很多是同样的参数，只换个名字，比如 `To_Base64` 和 `From_Base64`。

但也有例外，就是最外层的 Zlib 压缩，它的加解密需要填写的参数是不一样的：

```
Zlib_Deflate('Dynamic Huffman Coding')
Zlib_Inflate(0,0,'Adaptive',false,false)
```

这个自己手动添加一下就好。

替换无论是使用文本编辑器的替换功能，还是命令工具的替换还是编写脚本等等，都可以。

最后的解密 recipe 在 [writeup/recipe](./writeup/recipe)

导入 recipe 后将 data 也拖入输入窗口，输出会转圈圈很久，这是正常的，我使用本地最新的 CyberChef 在一分钟左右。

如果你要测试，不要勾选 `Auto Bake` ，不然每次变动都会计算一轮，会卡住的。

```
flag{secret_recipe_for_kraby_patty}
```

任何手搓和编写解密脚本的方法，都是神仙下凡。
