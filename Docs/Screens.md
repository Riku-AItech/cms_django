# BlueCMS 画面一覧と遷移

このドキュメントは、BlueCMSアプリケーションの主要な画面とその間の遷移についてまとめたものです。

## 画面一覧

以下は、BlueCMSに含まれる主な画面（テンプレート）と対応するURLパターン（一部）です。

-   **認証関連**
    -   ログイン (`/accounts/login/`) - `registration/login.html`
    -   サインアップ (`/accounts/signup/`) - `registration/signup.html`
-   **投稿関連**
    -   投稿一覧 (`/posts/`) - `blog/post_list.html`
    -   投稿詳細 (`/posts/<pk>/`) - `blog/post_detail.html`
    -   投稿作成/編集 (`/posts/new/`, `/posts/<pk>/edit/`) - `blog/post_form.html`
    -   下書き一覧 (`/posts/drafts/`) - `blog/draft_list.html`
    -   投稿削除確認 (※現在はブラウザ標準ダイアログ使用) - (`blog/post_confirm_delete.html`)
-   **プロフィール関連**
    -   プロフィール表示 (編集可能) (`/users/<username>/`) - `blog/profile.html`
    -   プロフィール表示 (閲覧専用) (`/users/<username>/readonly/`) - `blog/profile_readonly.html`
    -   プロフィール編集 (`/accounts/profile/edit/`) - `blog/profile_edit.html`