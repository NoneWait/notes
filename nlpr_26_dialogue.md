# Dialogue Systems and Chatbots

## intro

对话系统可以分为两大类型

- Task-oriented dialogue agents：主要是基于frame-based的结构（**GUS**架构）
- chatbots : 主要有rule-based，information retrieval and encoder-decoder三类系统

## 人类对话的特性

因为人类对话中存在以下细微的特性，以至于构造一个对话系统和人类对话是极具挑战性的。

### Turns

一个对话就是一个turns的序列：（$A_1$,$B_1$,$A_2$, and so on），该系统必须知道何时停止talking，何时开启一段

talking。

- endpointing or endpoint detection：检测用户是否停止说话

### Speech Acts

四种说话或者表达方式(utterance)，在对话中，讲话者的每种表述方式都是一种action。

| Action           | 含义                                                       | 举例               |
| ---------------- | ---------------------------------------------------------- | ------------------ |
| Constatives      | 讲话者答应某人，比如回答、肯定、拒绝                       | 我要在五月去旅游   |
| Directives       | 讲话者尝试让听者(addressee)去做某件事，比如advising,asking | 让助手关闭音乐     |
| Commissives      | 讲话者承诺在未来做某件事（promising,planning...）          | 你什么时候去旅游？ |
| Acknowledgements | 表达讲话者的态度，常用于设计活动（apologizing）            | 感谢助手帮忙预定   |

###  Grounding

一段对话不是一系列独立的speech acts，而是一个集合式的行为。所以，对话参与者的对话需要建立在他们都认可的common ground下，可以理解为相同背景下。

### Subdialogues and Dialogue Structure

### Initiative(主动的)

比如说一个采访者采访一个人，在这种场景下这个采访者就是对话发起者。实际场景中，发起者通常在对话中相互转换，即有时候提问有时候回答

### Inference and Implicature

推理和蕴含



## Chatbots

这种最简单的一种对话系统，主要出于娱乐目的，比如说微软的小冰等。聊天机器人可以分为以下两种架构类型，

分别是rule-based和corpus-based

### Rule-based chatbots：ELIZA and PARRY

主要是利用规则来生成回复

### Corpus-based chatbots

这些系统主要数据驱动的，比如说采用电影对话来训练。

#### IR retrieval systems

主要通过query和语料库中的回复的相似度匹配模型来返回response。如果query过短，可以使用之前的问句信息。

#### machine learned sequence transduction