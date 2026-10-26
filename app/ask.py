"""会話履歴を保ったまま対話できるチャットスクリプト。

使い方:
    uv run python -m app.ask
    uv run python -m app.ask "最初の質問"
"""

import argparse
import sys

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def display_token_usage(metadata) -> None:
    """トークン数のメタデータを表示する補助関数"""
    if metadata:
        prompt_tokens = metadata.prompt_token_count
        candidates_tokens = metadata.candidates_token_count
        total_tokens = metadata.total_token_count
        print(f"\n[トークン数] 入力: {prompt_tokens}, 出力: {candidates_tokens}, 合計: {total_tokens}")


def run_chat(initial_question: str | None = None) -> None:
    client = genai.Client(api_key=get_api_key())
    
    # 会話履歴を自動管理するチャットセッションの作成
    chat = client.chats.create(model=MODEL)

    print(f"[model] {MODEL}")
    print("会話を開始します（終了するには 'q', 'exit', または Ctrl+C を入力）\n")

    # 引数で渡された最初の質問がある場合は先に送信
    first_query = initial_question
    while True:
        try:
            if first_query:
                user_input = first_query
                first_query = None
                print(f"[質問] {user_input}")
            else:
                user_input = input("\n[質問] > ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit", "q"):
                print("会話を終了します。")
                break

            # 過去の会話履歴を含めてメッセージを送信
            response = chat.send_message(user_input)

            # 回答とトークン数の表示
            print(f"\n[回答]\n{response.text}")
            display_token_usage(response.usage_metadata)

        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            break
        except (KeyboardInterrupt, EOFError):
            print("\n会話を終了します。")
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="LLMと連続して対話する")
    parser.add_argument("question", nargs="?", default=None, help="最初に投げる質問（省略可）")
    args = parser.parse_args()

    run_chat(args.question)


if __name__ == "__main__":
    main()