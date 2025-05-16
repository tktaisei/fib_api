# Fibonacci API 🌀

「技術課題\_Speee\_13.pdf」
***n 番目のフィボナッチ数を返す REST API*** の実装。
Python 3.12 + FastAPI で最小構成かつ保守しやすい形にまとめています。

---

## 🏗️ 目次

1. [動作環境](#動作環境)
2. [クイックスタート](#クイックスタート)
3. [実装方針](#実装方針)
4. [API 仕様](#api-仕様)
5. [テスト](#テスト)
6. [プロジェクト構成](#プロジェクト構成)

---

## 動作環境

| ソフト     | バージョン   |
| ------- | ------- |
| Python  | 3.12.x  |
| FastAPI | 0.111.0 |
| Uvicorn | 0.30.0  |
| pytest  | 8.1.1   |

---

## クイックスタート

```bash
# 1. クローン
git clone https://github.com/tktaisei/fib_api
cd fib_api

# 2. 仮想環境 (任意)
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# 3. 依存インストール
pip install -r requirements.txt

# 4. ユニットテスト
python -m pytest -q

# 5. 開発サーバ起動
uvicorn app.main:app --reload

# 6. 動作確認
curl "http://127.0.0.1:8000/fib?n=10"
# {"result":55}

# Swagger UI
start "http://127.0.0.1:8000/docs"   # Windows は start / mac は open
```

---

## 実装方針

* **関心分離** : `fib.py` に計算ロジック、`main.py` に HTTP ルーティングを分離。
* **入力検証** : `Query(gt=0)` で 1 以上の整数を強制。
* **キャッシュ** : `@lru_cache` で同じ n を再計算しない。
* **エラー統一** : すべて `{status, message}` 形式で返却。

---

## API 仕様

| メソッド  | パス     | クエリパラメータ           | 説明                       |
| ----- | ------ | ------------------ | ------------------------ |
| `GET` | `/fib` | `n` = 1 以上の整数 (必須) | *n* 番目のフィボナッチ数を JSON で返す |

### レスポンス例

#### 成功 (200)

```json
{
  "result": 55
}
```

#### 失敗 (400)

| ケース          | 例                                                              |
| ------------ | -------------------------------------------------------------- |
| `n` が負数または 0 | `{ "status": 400, "message": "n must be a positive integer" }` |
| クエリ未指定・型不一致  | `{ "status": 400, "message": "Bad request." }`                 |

---

## テスト

```bash
pytest -q
```

`tests/test_fib.py` が **ロジック関数** と **API エンドポイント** の両方を検証。

---

## プロジェクト構成

```plaintext
fib_api/
├── app/
│   ├── __init__.py
│   ├── fib.py
│   └── main.py
├── tests/
│   └── test_fib.py
├── requirements.txt
└── README.md
```
