# Groupwork MCP Web

Windows PowerShellでの起動例（既存のMCPフォルダに展開する場合）:

```powershell
cd C:\Users\souta\MCP
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
```

ブラウザで http://127.0.0.1:8000 を開いてください。

- `server.py`: FastMCP (stdio) サーバー
- `app.py`: FastAPI。FastMCPクライアントとしてMCPツールを呼び出します。
- `static/index.html`: Web画面
- `speaker_result.json`: テスト用の話者結果。実際の話者識別は未実装。

**注意**: `server.py` が既存ファイルにある場合はバックアップしてから置き換えてください。ローカル開発用であり、インターネット公開しないでください。
