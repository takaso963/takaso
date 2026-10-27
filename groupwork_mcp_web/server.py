from fastmcp import FastMCP
from pathlib import Path
import json

mcp = FastMCP('GroupworkMCP')
BASE = Path(__file__).resolve().parent
PARTICIPANTS = {
    'A': {'name': '参加者A', 'interests': ['AI', '教育'], 'skills': ['Python']},
    'B': {'name': '参加者B', 'interests': ['ゲーム', 'デザイン'], 'skills': ['プレゼン']},
}

@mcp.tool
def hello() -> str:
    """接続確認"""
    return 'MCPサーバー接続成功！'

@mcp.tool
def get_all_participants() -> dict:
    """全参加者のプロフィールを取得"""
    return PARTICIPANTS

@mcp.tool
def get_participant(participant_id: str) -> dict:
    """指定した参加者のプロフィールを取得"""
    return PARTICIPANTS.get(participant_id, {'error': '参加者が見つかりません'})

@mcp.tool
def get_speaker() -> dict:
    """音声識別プログラムが保存した最新の識別結果を取得"""
    path = BASE / 'speaker_result.json'
    if not path.exists():
        return {'speaker': None, 'status': 'waiting', 'message': '識別結果はまだありません'}
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'))
    except (OSError, json.JSONDecodeError):
        return {'speaker': None, 'status': 'error', 'message': '結果ファイルを読み込めません'}

if __name__ == '__main__':
    mcp.run(transport='stdio')
