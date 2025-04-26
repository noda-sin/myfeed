from openai import OpenAI

SYSTEM_PROMPT = """\
あなたは技術編集者です。
与えられた DB 関連ニュース項目のリストを読み、
各項目ごとにURL先をチェックして日本語で要約してください。
そして、bullet list に要約してください。
各行は「
# 元のタイトル / 日本語タイトル
- (リンク)
要約 」
の形式にしてください。
"""

def summarize(api_key: str, items: list[dict], cfg: dict) -> str:
    client = OpenAI(api_key=api_key)
    if not items:
        return "本日は新しいトピックはありません :zzz:"

    bullets = "\n".join(f"- {i['title']} ({i['link']})" for i in items[:20])
    user_prompt = f"ニュース一覧:\n{bullets}"
    res = client.chat.completions.create(
        model=cfg["openai_model"],
        messages=[{"role":"system","content":SYSTEM_PROMPT},
                  {"role":"user","content":user_prompt}],
        max_tokens=2048
    )
    return res.choices[0].message.content.strip()
