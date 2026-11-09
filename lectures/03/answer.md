# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：toolを使って回答を生成するようになった．
- `--trace` で見えたツール呼び出し（ツール名と引数）： get_lecture_summary({'lecture': 2})
- 1つの質問での LLM 呼び出し回数（`requests`）：1
- 追加したツールと、docstring に書いた説明：
def make_quiz(lecture: int) -> str:
    """指定した回の用語から 1つを選び、
    確認問題と答えを返す。
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    """

## 宿題

- 取り組んだレベル：実装 
- やったこと：
学習の記録を learning_log/ フォルダに保存するツール save_learning_logの実装をした

- 結果：

base) PS C:\Users\yamag\programs\class\AIEngineering2026\lecture-ai-engineering-2026> uv run --env-file .env python -m app.agent "第3回の要点をまとめて、学習記録として保存して"
[model] gemini-3.5-flash-lite
                 pydantic-ai v2.57.0 • Python 3.12.3
      / \
     /   \       agent: target • model: google:gemini-3.5-flash-lite • tools: 4 • capabilities: 1
   /___.___\
  /    |    \    observability: off — see every model and tool call live, with cost
/      |      \    set it up free with Logfire and a GitHub login: https://pydantic.dev/ai-setup.md
`---.._|_..---'    or use any OpenTelemetry backend: https://pydantic.dev/docs/ai/logfire/#otel

                 goes away once observability is on — or PYDANTIC_AI_NO_BANNER=1

[確認] ツール: save_learning_log
{
  "title": "第3回 AIエージェント 学習記録",
  "content": "# 第3回 学習記録: AIエージェント\n\n## 学んだ内容\n- **AIエージェントの基本構造**: 「モデル ＋ ループ ＋ ツール」の組み合わせで構成されている。\n- **ツールの仕組み**: LLM自身がツールを実行するのではなく、モデルがツール名や説明文、引数の型を見て呼び出しを依頼し、実際の実行はプログラム側が行う。説明文の設計が非常に重要。\n- **エージェントループ**: 1つの質問に対してLLMを複数回呼び出すため、応答時間やコスト、レート制限への影響に注意する必要がある。\n- **ハーネスとフレームワーク**: Claude CodeやPiといったハーネスや、型安全なツール定義ができるPydantic AIについて学んだ。\n- **安全性の確保**: ガードレールやHuman-in-the-loop（人の確認）を取り入れる重要性を理解した。\n\n関連する回：第3回"
}
この内容を保存しますか？ (y/n): y
第3回の要点をまとめ、学習記録として `learning_log/` フォルダに保存しました。

### 第3回の要点まとめ
- **AIエージェントの基本構造**: 「モデル ＋ ループ ＋ ツール」の組み合わせにより、LLMが自律的に目的を達成するシステム。
- **ツールの活用**: モデルはツールの説明文や引数の型を見て呼び出しを判断し、実行はプログラム側が行う。
- **エージェントループのコスト**: 1回の質問でLLMが複数回呼び出されるため、コストや応答時間への配慮が必要。
- **フレームワークとハーネス**: Pydantic AIを使ったツール定義や、Piなどのハーネスの役割を学びました。
- **安全性**: ガードレールやHuman-in-the-loopの導入によるリスク管理が重要。

関係する回：第3回
- 気づき・疑問：
必要なツールを呼び出したうえで保存することが確認できた．\
人間側が使いたいツールが明らかな場合は良いが，潜在的に使った方が良いが気づいていない場合にagentに使わせるのは，難しそう．