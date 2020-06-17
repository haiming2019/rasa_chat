rasa


## 可视化story
```bash
# 生成 graph.html
rasa visualize -d domain.yml -s data/stories/sotries.md --out graph.html -c config.yml
# read
rasa visualize
```

## 训练

```bash
rasa train
```

## 启动

### Step 1: 启动 action server
```bash
# `xxxx` 部分应该替换成从 [心知天气](https://www.seniverse.com/) 申请获得的 API key 。用户可以免费注册，注册后可以在后台找到 `我的API密钥`。
SENIVERSE_KEY=xxxx rasa run actions
# etc
SENIVERSE_KEY=SqaphYs862YmgEz3U rasa run actions
```

### Step 2: 启动rasa server 

```bash
make run_model
```

### 命令行 进行对话
首先 Step 1: 启动 action server

然后
```bash
rasa shell
or rasa shell --debug
```

### [可选] 启动 rasa x
为了能够在不使用（或者没有）客户端的情况下以及测试模型的情况，我们可以使用 rasa x

```bash
rasa x --enable-api --auth-token 12345678
# start
rasa x
```
启动后会自动打开浏览器窗口

### client
Step 1: 启动 action server

Step 2: 启动rasa server 

Step 3: 进入cd client
```bash
bash ./start_server.bash
```
