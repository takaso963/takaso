from pathlib import Path
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

BASE = Path(__file__).resolve().parent
app = FastAPI(title='Groupwork AI')

async def invoke(name: str, args: dict | None = None):
    transport = StdioTransport(command=sys.executable, args=[str(BASE / 'server.py')], cwd=str(BASE))
    try:
        async with Client(transport) as client:
            result = await client.call_tool(name, args or {})
            if result.is_error:
                raise RuntimeError(str(result.content))
            return result.data
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'MCP呼び出しに失敗: {exc}') from exc

@app.get('/')
async def home():
    return FileResponse(BASE / 'static' / 'index.html')

@app.get('/api/participants')
async def participants():
    return await invoke('get_all_participants')

@app.get('/api/speaker')
async def speaker():
    return await invoke('get_speaker')

@app.get('/api/hello')
async def hello():
    return {'message': await invoke('hello')}
