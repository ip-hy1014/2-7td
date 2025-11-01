import sys
import os

# 親ディレクトリをパスに追加してapp_27tripleをインポート可能にする
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app_27triple import app

# VercelのPython RuntimeはWSGIアプリケーションを直接サポート
# 'application'という名前でエクスポートする必要があります
application = app

# Vercel用のハンドラー（オプション - 互換性のため）
def handler(request, response):
    # WSGIアプリとして直接実行
    # Vercelが自動的にWSGIアプリを処理します
    return application

