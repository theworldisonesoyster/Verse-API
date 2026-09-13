---
name: InteractDuration data
slug: versedotorg/scenegraph/interactable_duration/interactduration
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_duration
kind: data
module: /Verse.org/scenegraph
grade: B
depth: oneliner
status: done
order: 1
parent: versedotorg/scenegraph/interactable_duration
---

#
# InteractDuration data <B>

代理需与对象持续交互这么多秒才能完成一次交互；≤0.0 表示立即成功。若在交互进行中设置，新值将用于下一次交互，剩余时长按「新值减去已用时间」更新；差值 ≤0 则立即结束。
