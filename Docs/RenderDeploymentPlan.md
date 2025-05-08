# BlueCMS ローカル → Render 本番環境 移行計画

この文書では、ローカル開発環境（SQLite）から Render 上の本番環境（PostgreSQL）へ移行する手順と各ステップの流れをまとめています。

---
## 1. 前提条件
- ローカル開発: `SQLite` を使用
- 本番環境: `PostgreSQL`（Render マネージドDB）
- レポジトリ: GitHub 経由でデプロイ済み
- Django バージョン: 5.2

---
## 2. 移行ステップ概要

1. **依存パッケージの更新**
   - `psycopg2-binary`, `dj-database-url`, `gunicorn`, `whitenoise` を `requirements.txt` に追加・反映
2. **Django 設定変更**
   - `settings.py` で `DATABASES` を環境変数 `DATABASE_URL` から読み込むよう変更
   - `STATIC_ROOT`, `MEDIA_ROOT` の設定を追加
   - WhiteNoise ミドルウェアを組み込み
   - `STATICFILES_STORAGE` を `'whitenoise.storage.CompressedManifestStaticFilesStorage'` に設定
3. **静的ファイル収集**
   - `python manage.py collectstatic --noinput` を実行し、`staticfiles/` にまとめる
4. **レンダリング設定ファイル作成**
   - `Procfile` の追加: `web: gunicorn cms_django.wsgi`
   - `render.yaml` の追加（サービス＆DBプロビジョニング）
5. **Render ダッシュボード設定**
   - GitHub リポジトリを紐付け、ビルド／スタートコマンドを設定
   - 自動生成された `DATABASE_URL` を確認し環境変数に設定
   - Static Files セクションで `staticfiles` → `/static` を指定
   - （必要なら）Persistent Disk をアタッチし、`MEDIA_ROOT` をマウント
6. **マイグレーション & 確認**
   - `python manage.py migrate` を実行
   - アプリケーションが正常に動作することをブラウザで確認

---
## 3. Mermaid 図: 全体フロー
```mermaid
flowchart TD
  subgraph Local[ローカル開発]
    A1[SQLite DB] --> A2[requirements.txt 更新]
    A2 --> A3[settings.py 修正]
    A3 --> A4[静的・メディア設定]
    A4 --> A5[collectstatic 実行]
  end

  subgraph GitHub[GitHub]
    A5 --> B1[コード push]
  end

  subgraph Render[Render 本番]
    B1 --> C1[ビルド: pip install & collectstatic]
    C1 --> C2[Start: gunicorn 起動]
    C2 --> C3[Render PostgreSQL(DB) 利用]
    C2 --> C4[ホワイトノイズで STATIC 配信]
    C2 --> C5[Persistent Disk(MEDIA) マウント]
    C3 & C4 & C5 --> C6[アプリ起動完了]
  end

  C6 --> D[動作確認]
```

---
## 4. 詳細ステップ (補足)
- **依存パッケージ**: `pip install psycopg2-binary dj-database-url gunicorn whitenoise`
- **settings.py**:
  ```python
  import dj_database_url
  # コネクション寿命を設定
  DATABASES = {
      'default': dj_database_url.config(conn_max_age=600)
  }
  # WhiteNoiseミドルウェアを追加
  MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
  # 静的ファイル設定
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
  # メディアファイル設定
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- **collectstatic**: 自動ビルドステップに含める
- **render.yaml**: サービス定義・DB定義を IaC で管理
- **DATABASE_URL**: Renderダッシュボードで作成したPostgreSQLデータベースの接続情報を環境変数として設定する
  - データベース作成後、Renderダッシュボードの「Environment」タブで`DATABASE_URL`環境変数を確認
  - Webサービスの「Environment」タブで同じ`DATABASE_URL`を設定

## 5. トラブルシューティング
- **データベース接続エラー**: `DATABASE_URL`環境変数が正しく設定されていない場合、以下のエラーが発生します
  ```
  WARNING:root:No DATABASE_URL environment variable set, and so no databases setup
  django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured.
  ```
  - 解決策: Renderダッシュボードで`DATABASE_URL`環境変数を正しく設定し、サービスを再起動する
- **静的ファイル404エラー**: `STATICFILES_STORAGE`設定が正しくない場合に発生
  - 解決策: `whitenoise`が正しくインストールされ、設定が正しいことを確認

以上の計画に沿って設定・デプロイを行うことで、ローカル開発環境から Render 本番環境への移行が円滑に進みます。 