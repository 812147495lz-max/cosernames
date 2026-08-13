# Coser Names Dictionary

中文：Coser 人名与别名字典

This repository provides a community-maintained dictionary of creator names
and aliases for archive classification tools.

本仓库提供用于压缩包分类工具的 Coser 人名及别名字典。

## Scope / 内容范围

The dictionary focuses on matching names that appear in folder and archive
names. It is not intended to make claims about identity, affiliation, or
current activity.

字典主要用于匹配文件夹名和压缩包名中出现的人名，不用于证明身份、所属关系或当前活动情况。

## Contributions Welcome / 欢迎补充

1. We try to collect as many useful names and aliases as possible. Contributions,
   corrections, and missing aliases are welcome.
2. We have tried to deduplicate entries and aliases across different dictionary
   forms, and to match multiple names and aliases belonging to the same person.

1. 我们会尽量收集更多有用的人名和别名，欢迎补充、纠错和提交缺失的别名。
2. 我们尽量对不同字典写法进行去重，并将同一个人的多个名字和别名统一匹配。

Because matching names can be ambiguous, please provide evidence or context
when submitting a change that merges two previously separate people.

由于姓名匹配可能存在歧义，如果提交内容涉及把两个原本独立的人合并，请尽量提供依据或上下文。

## Format / 格式

`coser_names.csv` uses UTF-8 CSV with two columns:

`creator,aliases`

- `creator`: canonical display name / 规范显示名
- `aliases`: aliases separated by `/` / 多个别名使用 `/` 分隔

The dictionary does not contain private paths, accounts, IP addresses,
passwords, API keys, logs, or deployment configuration.

字典不包含私有路径、账号、IP 地址、密码、API key、日志或部署配置。

## License / 许可证

The dictionary is released under CC BY 4.0 where applicable. Please preserve
attribution and check the rights of any data you contribute.

在适用范围内，字典采用 CC BY 4.0 发布。提交内容时请保留必要署名，并确认所贡献数据的使用权利。
