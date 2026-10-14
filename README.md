# 感謝祭クイズ（Firebase版 / 誰でもQRで参加）

オールスター感謝祭ふうの早押し4択クイズ。参加者は **QRを読むだけ・アカウント不要** でスマホから参加できます。
進行役（あなた）がPCで出題・正解発表・順位発表をコントロールし、プロジェクターに映せます。

- 盤面：2×2の画像/テキストパネル、右に赤Qと縦書き問題、赤い丸のカウントダウン、締切0でも自動発表しない（全部手元操作）
- 正解発表：正解パネルがマゼンタに発光＋各選択肢の票数
- 結果発表：個人成績ランキングを下位から10人ずつ → トップ3はタメて、1位は赤＋紙吹雪
- 解答タイムは **各スマホ側で計測** するので、電波が弱くても公平（送信が発表前に届けばOK）
- カウントダウンBGM入り、プロジェクター全画面（スペース/→キーやクリッカーで送れる）

---

## セットアップ（最初の1回・無料）

### 1. Firebaseプロジェクトを作る
1. https://console.firebase.google.com/ → 「プロジェクトを追加」
2. 名前は何でもOK（例：kanshasai-quiz）。Googleアナリティクスは不要。

### 2. 匿名ログインを有効化
- 左メニュー「構築 > Authentication」→「始める」→「Sign-in method」→ **匿名** を有効にする

### 3. Realtime Database を作る
- 左メニュー「構築 > Realtime Database」→「データベースを作成」
- ロケーションは「asia-southeast1」等でOK
- セキュリティルールは **「テストモードで開始」** でOK（手早く試すなら）。
  きちんとするなら、作成後に「ルール」タブへ `database.rules.json` の中身を貼って公開してください。

### 4. Webアプリの設定（firebaseConfig）を取得
1. 「プロジェクトの設定（歯車）> 全般」→ 下の「マイアプリ」で **</> （ウェブ）** を追加
2. 表示される `firebaseConfig` をコピー
3. **`databaseURL` が無い場合**は自分で足してください。形式は
   `https://<プロジェクトID>-default-rtdb.<リージョン>.firebasedatabase.app`
   （Realtime Databaseの画面の上部に出ているURLでもOK）

### 5. index.html に貼り付け
`index.html` の上の方にある、この部分を自分の値に置き換えます：

```js
const firebaseConfig = {
  apiKey: "...",
  authDomain: "....firebaseapp.com",
  databaseURL: "https://....firebasedatabase.app",
  projectId: "...",
  appId: "..."
};
```

---

## 公開（デプロイ）

静的な1ファイルなので、どこに置いても動きます（**HTTPS必須**。下はどれも自動HTTPS）。

### いちばん簡単：Netlify Drop
1. https://app.netlify.com/drop を開く
2. この `index.html`（1ファイル）をドラッグ&ドロップ
3. 出てきたURLがそのまま本番URLです

### Firebase Hosting を使う場合
```bash
npm install -g firebase-tools
firebase login
cd kanshasai-quiz
firebase init hosting   # 既存プロジェクトを選択 / public ディレクトリはこのフォルダ / SPA は No
firebase deploy
```

---

## 使い方（当日の流れ）

1. **進行役**：公開URLをPCで開く（`?room=` が付いていないとホスト画面）
2. 「クイズを作る」で問題を作成（各選択肢に「＋画像」で写真も入れられる）→ **「ルームを作成」**
3. **QRと部屋コード**が出る → プロジェクターに映すか、家族に見せる
4. **参加者**：スマホのカメラでQRを読む → 名前を入れて参加
5. 進行役が **「クイズを開始」** → 出題（BGM＆カウントダウン）
6. 時間がきたら **「解答締め切り・正解発表」**（0になっても自動では出ません）
7. **「次の問題へ」** を繰り返し、最後に **「個人成績ランキングへ」** → 「発表スタート」
8. プロジェクターは「⛶ プロジェクター表示」で全画面。**スペース/→キー（プレゼンのクリッカー）** でも送れます。

### 注意
- 全員がネット接続（Wi-Fi/4G）に繋がっている必要があります（完全オフラインは別方式）。
- 画像はこの端末で作った問題に埋め込まれます。あまり巨大な写真は自動で縮小されます。

---

## ファイル
- `index.html` … これ1つが本体（デプロイするのはこれだけ）
- `database.rules.json` … Realtime Database のルール（任意）
- `template.html` / `board.css` / `bgm.b64` / `imgs.json` / `build.py` … `index.html` を再生成するための素材（編集用）

`index.html` を作り直すとき：
```bash
python3 build.py
```
