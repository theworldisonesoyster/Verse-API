---
name: GetSecondsSinceEpoch
slug: versedotorg/verse/getsecondssinceepoch
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/getsecondssinceepoch
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# GetSecondsSinceEpoch function <B>

> Returns the number of seconds since January 1, 1970 UTC, ignoring leap seconds. I.e, this function implements Unix time. This function always returns the same value within the same transaction.
> 返回自 1970 年 1 月 1 日 UTC 起的秒数（Unix 时间戳），忽略闰秒。

`using { /Verse.org/Verse }`

```verse
GetSecondsSinceEpoch<public><native>():float
```

## Parameters

GetSecondsSinceEpoch 不接受任何参数。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
