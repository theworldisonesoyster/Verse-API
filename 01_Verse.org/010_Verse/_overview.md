---
name: Verse module
slug: versedotorg/verse
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse
kind: module
module: /versedotorg
grade: B
depth: brief
status: done
---

# Verse module <B>

Verse 语言核心模块：运算符、数学函数、字符串/诊断/结果类型、事件接口与时间函数。

## Classes and Structs

| Name | Description |
|---|---|
| [diagnostic](diagnostic.md) | 不透明的诊断消息，只出现在诊断日志中。其格式可能随时变化且无法被 Verse 代码检查。 |
| [locale](locale.md) | 用于 message 本地化的区域设置。 |
| [message](message.md) | 可本地化的文本消息。 |

## Interfaces

| Name | Description |
|---|---|
| [cancelable](cancelable.md) | 由可取消操作实现：持有它即可取消对应的进行中操作。 |
| [disposable](disposable.md) | 由实例生命周期有限（可释放）的类实现。 |
| [enableable](enableable.md) | 由实例可被启用/禁用的类实现。 |
| [invalidatable](invalidatable.md) | 由实例可能随时失效的类实现。 |
| [showable](showable.md) | 由实例可改变可见性的类实现。 |

## Functions

| Name | Description |
|---|---|
| [Print](print.md) | 把 Message 写入专用 Print 日志，并在客户端屏幕以 Color 显示 Duration 秒。 |
| [Print](print-1.md) | Print 的 message（可本地化文本）重载。 |
| [Print](print-2.md) | Print 的 diagnostic（诊断）重载。 |
| [event](event.md) | 参数化构造：按载荷类型 t 创建可重复触发的事件。 |
| [event](event-1.md) | event 的无载荷构造重载。 |
| [listenable](listenable.md) | 参数化接口构造：组合 awaitable 与 subscribable（持续订阅广播）。 |
| [listenable](listenable-1.md) | listenable 的无参数构造重载。 |
| [operator'='](operatorequals.md) | 可失败的相等比较：相等则成功并返回左值。 |
| [result](result.md) | 由「可为成功或失败的操作」的结果类实现。 |
| [MakeSuccess](makesuccess.md) | 构造一个表示成功的 result 实例。 |
| [MakeError](makeerror.md) | 构造一个携带错误信息的失败 result 实例。 |
| [ToDiagnostic](todiagnostic.md) | 把任意 Verse 值转换成不透明的诊断消息。 |
| [Err](err.md) | 以错误消息 Message 立即中止 Verse 运行时。 |
| [signalable](signalable.md) | 带载荷、可被触发（signal）的事件实现的参数化接口。 |
| [subscribable](subscribable.md) | 带载荷、可被订阅（Subscribe 持续接收）的事件实现的参数化接口。 |
| [subscribable](subscribable-1.md) | 无载荷、可被订阅的事件实现的参数化接口。 |
| [Localize](localize.md) | 按当前区域设置本地化 Message，生成字符串。 |
| [Concatenate](concatenate.md) | 把嵌套数组压平：按顺序连接 Arr 里每个子数组的元素，返回一个新数组。 |
| [Join](join.md) | 用 Separator 把 Element 数组拼接成一个 message（可本地化文本）。 |
| [Join](join-1.md) | 用 Separator 把 Element 数组拼接成一个字符串。 |
| [ConcatenateMaps](concatenatemaps.md) | 合并两个映射（M2 同键覆盖 M1）。 |
| [GetSecondsSinceEpoch](getsecondssinceepoch.md) | 返回自 1970 年 1 月 1 日 UTC 起的秒数（Unix 时间戳），忽略闰秒。 |
| [Abs](abs.md) | 返回 Value 的绝对值（int 版本）。 |
| [Abs](abs-1.md) | 返回 Value 的绝对值（float 版本）。 |
| [Ceil](ceil.md) | 返回大于等于 Val 的最小 int（向上取整，rational 输入版本）。 |
| [Ceil](ceil-1.md) | 返回大于等于 Val 的最小 int（向上取整，float 输入版本）。非有限值时失败。 |
| [Floor](floor.md) | 返回小于等于 Val 的最大 int（向下取整，rational 输入版本）。 |
| [Floor](floor-1.md) | 返回小于等于 Val 的最大 int（向下取整，float 输入版本）。非有限值时失败。 |
| [Round](round.md) | 返回 Val 四舍五入到最近整数的 int；小数部分恰为 0.5 时取最近的偶数（IEEE-754 默认舍入）。非有限值时失败。 |
| [Int](int.md) | 返回等于 Val 去掉小数部分的 int（向零取整）。 |
| [Clamp](clamp.md) | 把 Val 限制在 A 与 B 之间（int 版本；健壮处理 A、B 顺序）。 |
| [Clamp](clamp-1.md) | 把 Val 限制在 A 与 B 之间（float 版本；健壮处理 A、B 顺序）。 |
| [Min](min.md) | 返回 X 和 Y 中的较小值（int 版本）。 |
| [Min](min-1.md) | 返回 X 和 Y 中的较小值；任一为 NaN 时返回 NaN（float 版本）。 |
| [Max](max.md) | 返回 X 和 Y 中的较大值（int 版本）。 |
| [Max](max-1.md) | 返回 X 和 Y 中的较大值；任一为 NaN 时返回 NaN（float 版本）。 |
| [ToString](tostring.md) | 把 Val（float）转成字符串表示。 |
| [ToString](tostring-1.md) | 把 Val（char）转成可打印的字符串表示。 |
| [ToString](tostring-2.md) | 把 String 原样返回（string 的 ToString 重载）。 |
| [ToString](tostring-3.md) | 把单个 Character（char）转成字符串。 |
| [operator'?'](operatorquestionmark.md) | logic 查询：Value 为 true 则成功，为 false 则失败——logic 接入失败上下文的标准写法。 |
| [operator'?'](operatorquestionmark-1.md) | option 取值：Value 有值则成功并返回该值，为空则失败。 |
| [operator'<>'](operatorlessgreater.md) | 不相等比较：Lhs 与 Rhs 不相等则成功，相等则失败。与 [operator'=](operatorequals.md) 语义相反。 |
| [prefix'-'](prefixminus.md) | 整数取负（一元 -）。 |
| [prefix'-'](prefixminus-1.md) | 浮点取负（一元 -）。 |
| [operator'+'](operatorplus.md) | 整数加法。 |
| [operator'+'](operatorplus-1.md) | 浮点加法。 |
| [operator'+'](operatorplus-2.md) | 数组拼接：返回 Lhs 与 Rhs 元素顺序连接的新数组。 |
| [operator'+'](operatorplus-3.md) | 集合并集：返回包含 InSetL 与 InSetR 全部元素的新集合。 |
| [operator'+'](operatorplus-4.md) | 拼接两个诊断消息。 |
| [operator'+'](operatorplus-5.md) | 诊断消息与普通字符串拼接，结果为诊断消息。 |
| [operator'+'](operatorplus-6.md) | 普通字符串与诊断消息拼接，结果为诊断消息。 |
| [operator'-'](operatorminus.md) | 整数减法。 |
| [operator'-'](operatorminus-1.md) | 浮点减法。 |
| [operator'*'](operatorstar.md) | 整数乘法。 |
| [operator'*'](operatorstar-1.md) | 浮点乘法。 |
| [operator'*'](operatorstar-2.md) | int 与 float 相乘，结果为 float。 |
| [operator'*'](operatorstar-3.md) | float 与 int 相乘，结果为 float。 |
| [operator'/'](operatorslash.md) | 整数除法：返回 rational；除数为 0 时失败。 |
| [operator'/'](operatorslash-1.md) | 浮点除法（除数为 0 结果为 Inf/NaN，不失败）。 |
| [operator'+='](operatorplusequals.md) | 整数累加：等价于 set Lhs = Lhs + Rhs。 |
| [operator'+='](operatorplusequals-1.md) | 浮点累加。 |
| [operator'+='](operatorplusequals-2.md) | 数组累加：把 Rhs 的元素追加进 Lhs 数组。 |
| [operator'-='](operatorminusequals.md) | 整数累减。 |
| [operator'-='](operatorminusequals-1.md) | 浮点累减。 |
| [operator'*='](operatorstarequals.md) | 整数累乘。 |
| [operator'*='](operatorstarequals-1.md) | 浮点累乘。 |
| [operator'>'](operatorgreater.md) | 整数大于比较（可失败）。 |
| [operator'>'](operatorgreater-1.md) | 浮点大于比较（可失败）。 |
| [operator'>='](operatorgreaterequals.md) | 整数大于等于比较（可失败）。 |
| [operator'>='](operatorgreaterequals-1.md) | 浮点大于等于比较（可失败）。 |
| [operator'<'](operatorless.md) | 整数小于比较（可失败）。 |
| [operator'<'](operatorless-1.md) | 浮点小于比较（可失败）。 |
| [operator'<='](operatorlessequals.md) | 整数小于等于比较（可失败）。 |
| [operator'<='](operatorlessequals-1.md) | 浮点小于等于比较（可失败）。 |
| [operator'()'](operator.md) | 数组按索引取元素：越界则失败。 |
| [operator'()'](operator_-1.md) | 数组按索引取元素重载（u 元素类型版本）。 |
| [operator'()'](operator_-2.md) | 映射按键取值：键不存在则失败。 |
| [operator'()'](operator_-3.md) | 映射按键取值重载。 |
| [operator'()'](operator_-4.md) | 映射按键取值重载。 |
| [weak_map](weak_map.md) | 构造「键为弱引用对象」的映射类型（如以 player/session 为键的全局状态表）。 |
| [FitsInPlayerMap](fitsinplayermap.md) | 判断该类型是否能用作 player 映射的键（涉及持久化限制）。 |
| [classifiable_subset](classifiable_subset.md) | 构造可分类子集容器。 |
| [MakeClassifiableSubset](makeclassifiablesubset.md) | 构造包含 InElements 的 classifiable_subset。 |
| [BitAnd](bitand.md) | 按位与。 |
| [BitOr](bitor.md) | 按位或。 |
| [BitXor](bitxor.md) | 按位异或。 |
| [BitNot](bitnot.md) | 按位取反。 |
| [Sqrt](sqrt.md) | 返回 X 的平方根；X < 0.0 时返回 NaN。 |
| [Sin](sin.md) | 返回 X 的正弦（X 为弧度）。 |
| [Cos](cos.md) | 返回 X 的余弦（X 为弧度）。 |
| [Tan](tan.md) | 返回 X 的正切（X 为弧度）。 |
| [ArcSin](arcsin.md) | 返回 X 的反正弦（弧度）。 |
| [ArcCos](arccos.md) | 返回 X 的反余弦（弧度）。 |
| [ArcTan](arctan.md) | 返回 X 的反正切（弧度）。 |
| [ArcTan](arctan-1.md) | 返回原点到点 (X, Y) 连线与 X 轴的夹角（弧度）。 |
| [Sinh](sinh.md) | 返回 X 的双曲正弦。 |
| [Cosh](cosh.md) | 返回 X 的双曲余弦。 |
| [Tanh](tanh.md) | 返回 X 的双曲正切。 |
| [ArSinh](arsinh.md) | 返回 X 的反双曲正弦（X 有限时）。 |
| [ArCosh](arcosh.md) | 返回 X 的反双曲余弦（X ≥ 1.0 时）。 |
| [ArTanh](artanh.md) | 返回 X 的反双曲正切（X 有限时）。 |
| [Pow](pow.md) | 返回 A 的 B 次幂。 |
| [Quotient](quotient.md) | 返回欧几里得除法 X/Y 的商。 |
| [Mod](mod.md) | 返回欧几里得除法 X/Y 的余数。 |
| [Exp](exp.md) | 返回 e 的 X 次幂（自然指数）。 |
| [Ln](ln.md) | 返回 X 的自然对数。 |
| [Log](log.md) | 返回 X 的以 B 为底对数。 |
| [Lerp](lerp.md) | 在 From（t=0）与 To（t=1）之间线性插值/外推。 |
| [Sgn](sgn.md) | 返回 Val 的符号：正数 1、零 0、负数 -1（int 版本）。 |
| [Sgn](sgn-1.md) | 返回 Val 的符号（float 版本）。 |
| [IsAlmostEqual](isalmostequal.md) | 若 Val1 与 Val2 的差在 AbsoluteTolerance 内则成功（浮点比较专用）。 |

## Data

| Name | Description |
|---|---|
| [Inf](inf.md) | 浮点正无穷常量（IEEE 754 Inf）。 |
| [NaN](nan.md) | 浮点非数常量（IEEE 754 NaN），表示无效的浮点运算结果。 |
| [PiFloat](pifloat.md) | 浮点圆周率 π 常量。 |

## Submodules

| Name | Description |
|---|---|
| [Easing](010_Easing/_overview.md) | 缓动插值函数族（Linear/Ease/EaseIn/EaseOut/EaseInOut/CubicBezier）。 |
