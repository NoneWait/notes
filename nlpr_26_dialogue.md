# Dialogue Systems and Chatbots

## intro

对话系统可以分为两大类型

- Task-oriented dialogue agents：主要是基于frame-based的结构（**GUS**架构）
- chatbots : 主要有rule-based，information retrieval and encoder-decoder三类系统

## 人类对话的特性

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