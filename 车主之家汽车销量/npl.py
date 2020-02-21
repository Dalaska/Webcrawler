import xmnlp

doc = """小明 NLP 是一款开源的轻量级中文自然语言处理工具🔧，当前版本发布时间为2019年9月，改版本修复了一些 bug 也增加了一些特性，主要新增特性如下：分词/词性标注支持日期、email、url、html标签、书📖的识别。如果您有什么建议/疑问欢迎联系我 xmlee97@gmail.com"""

xmnlp.seg(doc, hmm=True)

pass