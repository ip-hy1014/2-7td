# Vercel デプロイガイド

Vercelで2-7 Triple Drawをデプロイする手順です。

## 前提条件

- Vercelアカウント（無料で作成可能）
- GitHubアカウント
- ローカルにVercel CLIがインストールされていること（オプション）

## デプロイ手順

### 方法1: Vercel CLIを使用（推奨）

1. **Vercel CLIをインストール**
   ```bash
   npm i -g vercel
   ```

2. **ログイン**
   ```bash
   vercel login
   ```

3. **プロジェクトディレクトリに移動**
   ```bash
   cd scripts
   ```

4. **デプロイ**
   ```bash
   vercel
   ```
   - 初回は設定を聞かれます（基本的にデフォルトでOK）
   - 本番環境にデプロイする場合は `vercel --prod`

5. **環境変数を設定**
   ```bash
   vercel env add SECRET_KEY
   ```
   ランダムな文字列を入力（例: `openssl rand -hex 32`で生成した値）

### 方法2: GitHub連携を使用

1. **GitHubにプッシュ**
   ```bash
   cd scripts
   git add .
   git commit -m "Add Vercel deployment"
   git push
   ```

2. **Vercelダッシュボードでインポート**
   - https://vercel.com にアクセス
   - "Add New..." → "Project"
   - GitHubリポジトリを選択
   - ルートディレクトリを `scripts` に設定
   - 環境変数 `SECRET_KEY` を追加（ランダムな文字列）

3. **デプロイ**
   - "Deploy" をクリック

## 注意事項

### セッション管理について

現在の実装では、ゲーム状態をメモリ内の`games`辞書で管理しています。Vercelのサーバーレス関数では、**各リクエストが独立したプロセスで実行されるため、メモリは保持されません**。

このため、以下のいずれかの対応が必要です：

1. **データベースを使用**（推奨）
   - Vercel Postgres（推奨）またはその他のデータベースサービス
   - ゲーム状態をDBに保存

2. **クライアント側で状態管理**
   - ゲーム状態をブラウザのLocalStorageに保存
   - ただし、セキュリティ上の懸念がある

3. **一時的な回避策**
   - 現在の実装のまま動作しますが、複数タブで開くと状態が混在する可能性があります

### セッションキー

本番環境では必ず環境変数 `SECRET_KEY` を設定してください。安全なランダム文字列を生成するには：

```bash
openssl rand -hex 32
```

## トラブルシューティング

### エラー: "Module not found"

`requirements.txt`が正しく配置されているか確認してください。

### エラー: "Handler not found"

`api/index.py`が存在し、正しく設定されているか確認してください。

### セッションが保持されない

Vercelのサーバーレス環境では、メモリベースのセッションは保持されません。データベースの使用を検討してください。

## v0との統合

v0を使用している場合、UI改善のアイデアをv0で生成し、既存のAPIエンドポイントと統合できます。

