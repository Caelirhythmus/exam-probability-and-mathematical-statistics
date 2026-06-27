# 概率论与数理统计 · 期末试卷题解

叉叉大学 202× 至 202× 学年第一学期概率论与数理统计（理工类）课程期末考试试卷题解。

## 目录结构

```
docs/
├── exam/
│   ├── md/
│   │   ├── 1-collections/          # 原子卡集合
│   │   │   ├── collections.md       # 发布态卡片
│   │   │   ├── not-release-collections.md  # 未发布卡片
│   │   │   ├── deprecated/          # 旧版归档
│   │   │   └── _example-*.md        # 原子卡制作的例题参考
│   │   ├── 2-random-21-22/         # 常规卷
│   │   │   ├── exam.md              # 试卷原题
│   │   │   ├── a/                   # 一、填空题
│   │   │   ├── d/                   # 四、解答题（二）
│   │   │   ├── e/                   # 五、解答题（三）
│   │   │   ├── notes/               # 备注
│   │   │   └── pdf/                 # 试卷 PDF 备份
│   │   └── 3-advanced/             # 提高卷
│   │       ├── exam.md              # 试卷原题
│   │       ├── d/                   # 四、计算题
│   │       ├── e/                   # 五、应用题
│   │       ├── f/                   # 六、证明题
│   │       └── exam.pdf
│   └── pdf/                         # 源 PDF 文件
├── hints/                            # 命名规范等提示
└── prompts/                          # 工作流提示
    ├── atomic-card.md                # 原子卡制作规范
    ├── edit.txt                      # 编辑流程提示
    └── git.txt                       # Git 提交规范
scripts/
└── anki/
    └── build-anki-cards.py           # collections.md → Anki TSV
```

## 命名规则

文件前缀表示试卷上的大题号：
- `a` — 第一大题（填空题）
- `d` — 第四大题（解答题 / 计算题）
- `e` — 第五大题（应用题）
- `f` — 第六大题（证明题）

文件名采用描述式命名，例如 `e1-binomial-probability-using-clt.md`。

## 体例

每题按「题目 → 步骤 → 题解」三段式组织。

## 原子卡系统

`collections.md` 以 A/B 双卡机制组织，每张卡片含：

| 字段 | 说明 |
|------|------|
| 主题 | `版块，上一步完成后的环境提示` |
| 求解 | 当前步要解决的问题 |
| 路径 | 答案（需回忆的内容） |

运行 `scripts/anki/build-anki-cards.py` 可生成 Anki 可导入的 TSV 文件。
