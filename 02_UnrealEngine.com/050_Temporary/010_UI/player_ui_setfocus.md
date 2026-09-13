---
name: SetFocus function
slug: unrealenginedotcom/temporary/ui/player_ui/setfocus
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/player_ui
kind: function
module: /Verse.org/temporary/ui
grade: S
depth: oneliner
status: done
order: 4
parent: unrealenginedotcom/temporary/ui/player_ui
---

#
# SetFocus function <S>

把使用者的焦点设置到该 Widget。目标 Widget 必须可聚焦（focusable），否则无效果。若在 AddWidget 之前调用 SetFocus，则 AddWidget 之后该控件会获得焦点——除非在那之前又有别的 SetFocus 调用。
