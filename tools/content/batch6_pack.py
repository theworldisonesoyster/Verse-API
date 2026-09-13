# -*- coding: utf-8 -*-
# 批次6：Assets / Colors（含 NamedColors 147 常量表）/ SpatialMath
import json as _json
import os as _os

_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
_m = _json.load(open(_os.path.join(_ROOT, "manifest.json"), encoding="utf-8"))


def _find(n, name):
    if n.get("name") == name:
        return n
    for c in n.get("children", []):
        r = _find(c, name)
        if r:
            return r
    return None


_named = _find(_m[0], "NamedColors")
NAMED_ROWS = [(c["name"], "预设颜色常量。") for c in _named.get("children", [])] if _named else []

PACKS = [
    {
        "outdir": "01_Verse.org/110_Assets", "module_slug": "versedotorg/assets",
        "overview_title": "Assets module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/assets",
        "overview": {"zh": "资产引用类型：网格、贴图、材质、音效、粒子、动画序列，以及输入动作与输入映射。"},
        "entries": {
            "versedotorg/assets/animation_sequence": {"zh": "动画序列资产。"},
            "versedotorg/assets/material": {"zh": "材质资产。"},
            "versedotorg/assets/particle_system": {"zh": "粒子系统资产。"},
            "versedotorg/assets/mesh": {"zh": "网格资产。"},
            "versedotorg/assets/sound_wave": {"zh": "声波（音频）资产。"},
            "versedotorg/assets/texture": {"zh": "贴图资产。"},
            "versedotorg/assets/input_action/input_action(t)": {"zh": "参数化的输入动作类。"},
            "versedotorg/assets/input_action": {"zh": "参数化构造：创建 input_action(t) 输入动作。"},
            "versedotorg/assets/input_mapping": {"zh": "输入映射：把物理输入绑定到 input_action，交给 player_input 启用/停用。"},
            "versedotorg/assets/has_icon": {"zh": "提供图标的接口。"},
        },
    },
    {
        "outdir": "01_Verse.org/120_Colors", "module_slug": "versedotorg/colors",
        "overview_title": "Colors module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors",
        "overview": {"zh": "颜色系统：以 ACES 2065-1 色彩空间的 RGB 表示颜色，提供 sRGB/十六进制/HSV/色温等构造方式与 NamedColors 预设常量。"},
        "overview_data_rows": NAMED_ROWS,
        "known_cells": {
            "Red component of this color.": "此颜色的红色（Red）分量。",
            "Color component of this color_alpha.": "此 color_alpha 的颜色（Color）分量。",
            "The location of this transform.": "此变换的位置（Location）。",
            "Green component of this color.": "此颜色的绿色（Green）分量。",
            "Blue component of this color.": "此颜色的蓝色（Blue）分量。",
            "Alpha component of this color_alpha.": "此 color_alpha 的透明度（Alpha）分量。",
            "The rotation of this transform.": "此变换的旋转（Rotation）。",
            "The scale of this transform.": "此变换的缩放（Scale）。",
        },
        "entries": {
            "versedotorg/colors/color": {"zh": "以 ACES 2065-1 色彩空间的 RGB 三元组表示颜色；分量值为线性（gamma = 1.0）。",
                "example": 'C := MakeColorFromHex("#422439")'},
            "versedotorg/colors/color_alpha": {"zh": "ACES 2065-1 的 RGB 颜色＋附加 Alpha 通道；Color 与 Alpha (A) 各自独立处理。"},
            "versedotorg/colors/operatorplus": {"zh": "c0 与 c1 逐分量相加，得到新的 ACES 2065-1 颜色。"},
            "versedotorg/colors/operatorminus": {"zh": "c0 与 c1 逐分量相减，得到新的 ACES 2065-1 颜色。"},
            "versedotorg/colors/operatorstar": {"zh": "c0 与 c1 逐分量相乘，得到新的 ACES 2065-1 颜色。"},
            "versedotorg/colors/operatorstar-1": {"zh": "c 的各分量乘以 factor，得到新颜色。"},
            "versedotorg/colors/operatorstar-2": {"zh": "c 的各分量乘以 factor，得到新颜色。"},
            "versedotorg/colors/operatorstar-3": {"zh": "c 的各分量乘以 factor，得到新颜色。"},
            "versedotorg/colors/operatorstar-4": {"zh": "c 的各分量乘以 factor，得到新颜色。"},
            "versedotorg/colors/operatorslash": {"zh": "c 的各分量除以 factor，得到新颜色。"},
            "versedotorg/colors/operatorslash-1": {"zh": "c 的各分量除以 factor，得到新颜色。"},
            "versedotorg/colors/makecolorfromsrgb": {"zh": "从 sRGB 分量 Red/Green/Blue 构造 ACES 2065-1 颜色。正常取值 0.0~1.0，也可接受更大的值。"},
            "versedotorg/colors/makesrgbfromcolor": {"zh": "把 InColor 从 ACES 2065-1 转换为 sRGB 元组。"},
            "versedotorg/colors/makecolorfromsrgbvalues": {"zh": "从整数 sRGB 分量 Red/Green/Blue（0~255）构造 ACES 2065-1 颜色。"},
            "versedotorg/colors/makecolorfromhex": {"zh": "从 CSS 风格的 sRGB 十六进制字符串构造 ACES 2065-1 颜色。支持 RGB / RRGGBB / RRGGBBAA 格式；无效字符串会失败。",
                "example": 'C := MakeColorFromHex("#FF8800")'},
            "versedotorg/colors/makecolorfromhsv": {"zh": "从色相/饱和度/明度（HSV，sRGB 空间模型）构造 ACES 2065-1 颜色。"},
            "versedotorg/colors/makehsvfromcolor": {"zh": "把 InColor 从 ACES 2065-1 转为 sRGB，再以 HSV 模型返回元组。"},
            "versedotorg/colors/makecolorfromtemperature": {"zh": "从开尔文温度下黑体辐射的色度构造 ACES 2065-1 颜色；温度会被钳制为 ≥0。"},
            "versedotorg/colors/makecoloralpha": {"zh": "由 R/G/B/A 各分量构造新的 color_alpha。"},
            "versedotorg/colors/over": {"zh": "以「CA1 置于 CA2 之上」混合两个非预乘 color_alpha；alpha 分量钳制在 0.0~1.0。"},
        },
    },
    {
        "outdir": "01_Verse.org/130_SpatialMath", "module_slug": "versedotorg/spatialmath",
        "overview_title": "SpatialMath module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath",
        "overview": {"zh": "三维数学：vector3/rotation/transform 三大类型与构造、距离、点积/叉积、插值等函数。"},
        "entries": {
            "versedotorg/spatialmath/rotation": {"zh": "三维空间中朝向变化的抽象表示。"},
            "versedotorg/spatialmath/transform": {"zh": "缩放、旋转、平移的组合，按此顺序应用。"},
            "versedotorg/spatialmath/vector3": {"zh": "带浮点分量的三维向量。"},
            "versedotorg/spatialmath/makerotationradians": {"zh": "用 Axis 与 Angle（弧度，右手系）构造旋转：例如绕 Up 的正旋转会把 Forward 转向 Left。"},
            "versedotorg/spatialmath/makerotationdegrees": {"zh": "MakeRotationRadians 的角度（Degrees）版本。"},
            "versedotorg/spatialmath/makerotationfromyawpitchrollradians": {"zh": "以 Yaw、Pitch、Roll 的顺序做预旋转，构造旋转（右手系）。"},
            "versedotorg/spatialmath/makerotationfromyawpitchrolldegrees": {"zh": "上者的角度版本。"},
            "versedotorg/spatialmath/makerotationfromeulerradians": {"zh": "以 Left、Up、Forward 轴的顺序做后旋转，构造旋转（右手系）。"},
            "versedotorg/spatialmath/makerotationfromeulerdegrees": {"zh": "上者的角度版本。"},
            "versedotorg/spatialmath/identityrotation": {"zh": "构造单位旋转。",
                "example": "R := IdentityRotation()"},
            "versedotorg/spatialmath/distance": {"zh": "返回 Rotation1 与 Rotation2 之间的距离：0.0 表示等价旋转，1.0 表示相对（相反）旋转。"},
            "versedotorg/spatialmath/angulardistanceradians": {"zh": "返回两旋转间的最小角距离（弧度）。"},
            "versedotorg/spatialmath/angulardistancedegrees": {"zh": "上者的角度版本。"},
            "versedotorg/spatialmath/operatorstar": {"zh": "把 PreRotation 前置应用到 PostRotation（v * PreRotation * PostRotation）。",
                "example": "Combined := IdentityRotation() * MakeRotationDegrees(0.0, 90.0, 0.0)"},
            "versedotorg/spatialmath/makeshortestrotationbetween": {"zh": "构造从 InitialVector 转到 FinalVector 的最小角度旋转（向量长度任意）。",
                "example": "R := MakeShortestRotationBetween(vector3{Forward:=1.0}, vector3{Left:=1.0})"},
            "versedotorg/spatialmath/slerp": {"zh": "在 From（Ratio=0.0）与 To（Ratio=1.0）之间做球面线性插值；要求 0.0 ≤ Ratio ≤ 1.0。"},
            "versedotorg/spatialmath/operatorstar-1": {"zh": "用 Rotation 旋转 Vector，得到新的 vector3。",
                "example": "V := vector3{Forward:=1.0} * MakeRotationDegrees(0.0, 90.0, 0.0)"},
            "versedotorg/spatialmath/tostring": {"zh": "以轴/角度格式（右手系）返回旋转的字符串表示。"},
            "versedotorg/spatialmath/degreestoradians": {"zh": "把角度转为弧度。"},
            "versedotorg/spatialmath/radianstodegrees": {"zh": "把弧度转为角度。"},
            "versedotorg/spatialmath/operatorstar-2": {"zh": "用 InTransform（缩放＋旋转＋平移）变换 InVector。",
                "example": "V2 := vector3{Forward:=1.0} * MyTransform"},
            "versedotorg/spatialmath/tostring-1": {"zh": "返回 InTransform 的字符串表示（Translation/Rotation/Scale 形式）。"},
            "versedotorg/spatialmath/reflectvector": {"zh": "反转 Direction 中 SurfaceNormal 方向的分量，得到反射向量。",
                "example": "Bounced := ReflectVector(Dir, Normal)"},
            "versedotorg/spatialmath/dotproduct": {"zh": "返回 V1 与 V2 的点积。",
                "example": "D := DotProduct(vector3{Forward:=1.0}, vector3{Forward:=2.0})   # 2.0"},
            "versedotorg/spatialmath/crossproductlefthanded": {"zh": "返回 V1 与 V2 的左手叉积。"},
            "versedotorg/spatialmath/crossproduct": {"zh": "返回 V1 与 V2 的右手叉积。",
                "example": "N := CrossProduct(Up, Forward)"},
            "versedotorg/spatialmath/distance-1": {"zh": "返回 V1 与 V2 的欧氏距离。",
                "example": "D := Distance(A, B)"},
            "versedotorg/spatialmath/distancesquared": {"zh": "返回 V1 与 V2 欧氏距离的平方（比较远近时代价比 Distance 低）。"},
            "versedotorg/spatialmath/distanceforwardleft": {"zh": "忽略 Up 分量差异后的二维欧氏距离。"},
            "versedotorg/spatialmath/distancesquaredforwardleft": {"zh": "上者的平方版本。"},
            "versedotorg/spatialmath/tostring-2": {"zh": "返回 V 的字符串表示。"},
            "versedotorg/spatialmath/lerp": {"zh": "在 From（Parameter=0.0）与 To（Parameter=1.0）之间线性插值/外推；要求所有参数有限。",
                "example": "M := Lerp(0.0, 10.0, 0.25)   # 2.5"},
            "versedotorg/spatialmath/prefixminus": {"zh": "取负：各分量变号。"},
            "versedotorg/spatialmath/operatorplus": {"zh": "Left 与 Right 逐分量相加。"},
            "versedotorg/spatialmath/operatorminus": {"zh": "Left 逐分量减去 Right。"},
            "versedotorg/spatialmath/operatorstar-3": {"zh": "Left 与 Right 逐分量相乘。"},
            "versedotorg/spatialmath/operatorstar-4": {"zh": "Left 的各分量乘以 Right。"},
        },
    },
]
