# Fibonacci API 🌀

「技術課題_Speee_13.pdf」 **問題1** で求められている  
“_n 番目のフィボナッチ数を返す REST API_” の実装です。  
Python 3.12 + FastAPI で最小構成かつ保守しやすい形にまとめています。:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🏗️ 目次
1. [動作環境](#動作環境)
2. [クイックスタート](#クイックスタート)
3. [実装方針](#実装方針)
4. [API 仕様](#api-仕様)
5. [テスト](#テスト)
6. [プロジェクト構成](#プロジェクト構成)
7. [デプロイ手順（Render 例）](#デプロイ手順render-例)
8. [ライセンス](#ライセンス)

---

## 動作環境
| ソフト           | バージョン |
|------------------|-----------|
| Python           | 3.12.x    |
| FastAPI          | 0.111.0   |
| Uvicorn          | 0.30.0    |
| pytest           | 8.1.1     |

---

## クイックスタート
```bash
git clone https://github.com/<yourname>/fib_api.git
cd fib_api

# 仮想環境
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 依存インストール
pip install -r requirements.txt

# テスト
pytest -q                      # すべて passed になれば OK

# 開発サーバ
uvicorn app.main:app --reload

# ブラウザ確認
open "http://127.0.0.1:8000/docs"   # Swagger UI
