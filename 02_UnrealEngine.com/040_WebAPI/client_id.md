---
name: client_id
slug: unrealenginedotcom/webapi/client_id
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/webapi/client_id
kind: class
module: /Verse.org/webapi
grade: C
depth: oneliner
status: done
---

# client_id class <C>

WebAPI 的 client_id：授权用户在自己的模块中派生它，派生类的 Verse 类路径即后端服务中映射到端点的配置键。警告：不要把派生的 client_id 设为 public——它是你后端的私钥。示例：my_client_id := class(client_id)，MyClient := MakeClient(my_client_id)。
