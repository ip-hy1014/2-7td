# 2-7 Triple Draw デプロイガイド

このアプリをブラウザから遊べるようにデプロイする方法です。

## デプロイ方法

### オプション1: Render.com（推奨・無料プランあり）

1. **GitHubにプッシュ**
   ```bash
   cd scripts
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Render.comでアプリを作成**
   - https://render.com にアクセス
   - "New +" → "Web Service"
   - GitHubリポジトリを接続
   - 以下の設定：
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python3 app_27triple.py`
     - **Environment Variables**:
       - `SECRET_KEY`: ランダムな文字列（例: `openssl rand -hex 32`で生成）

3. **デプロイ完了後、提供されたURLでアクセス**

### オプション2: Railway

1. **Railwayにログイン** (https://railway.app)
2. **"New Project" → "Deploy from GitHub repo"**
3. **リポジトリを選択**
4. **環境変数を設定**:
   - `SECRET_KEY`: ランダムな文字列
   - `PORT`: Railwayが自動設定（削除不要）

### オプション3: Fly.io

1. **flyctlをインストール**: https://fly.io/docs/getting-started/installing-flyctl/
2. **ログイン**: `flyctl auth login`
3. **アプリ作成**: `flyctl launch`
4. **デプロイ**: `flyctl deploy`

### オプション4: Heroku

1. **Heroku CLIをインストール**: https://devcenter.heroku.com/articles/heroku-cli
2. **ログイン**: `heroku login`
3. **アプリ作成**: `heroku create <app-name>`
4. **環境変数設定**: `heroku config:set SECRET_KEY=<your-secret-key>`
5. **デプロイ**: `git push heroku main`

## ローカルでのテスト

デプロイ前にローカルでテストする場合：

```bash
cd scripts
pip install -r requirements.txt
export SECRET_KEY="test-secret-key"
python3 app_27triple.py
```

ブラウザで `http://localhost:5000` にアクセス

## 注意事項

- 現在の実装はメモリ内にゲーム状態を保持しています。複数ユーザーが同時にアクセスした場合、状態が混在する可能性があります
- 本番環境ではセッションキー（SECRET_KEY）を必ず変更してください
- Render.comの無料プランでは、一定時間アクセスがないとスリープします（再アクセス時に自動復帰）

