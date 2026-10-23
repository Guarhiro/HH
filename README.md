# Honey House BGM test

STORY ENGINEで外部音声URLをどう扱うか検証するための、オリジナル音列2曲と試聴ページです。

- 試聴ページ: https://guarhiro.github.io/HH/
- A（屋敷の朝）: https://guarhiro.github.io/HH/bgm/house-test.mp3
- B（庭のひと休み）: https://guarhiro.github.io/HH/bgm/garden-test.mp3

各16秒、MP3 32kbps・モノラル。`tools/generate_bgm.py`で生成できます（Python 3とFFmpegが必要）。

## Markdownの検証候補

通常リンク:

```markdown
[BGM A・屋敷の朝](https://guarhiro.github.io/HH/bgm/house-test.mp3)
```

画像記法で音声URLを指定:

```markdown
![BGM A](https://guarhiro.github.io/HH/bgm/house-test.mp3)
```

外部試聴ページへのリンク:

```markdown
[BGMプレーヤーを開く](https://guarhiro.github.io/HH/)
```

これらの記法がSTORY ENGINE内で再生できるかは別途検証する必要があります。外部プレーヤーはチャット変数の自動同期を行いません。
