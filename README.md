# シャミ子youtubeプレイヤー
シャミ子がdiscordのボイスチャンネルでyoutubeをかけてくれるbot  

# サ終
Herokuじゃ動かせなくなったのでこういう悲しい結果で終わりですね・・・(サ終)

# できること
* youtubeの再生
* 広告のスキップ

# できない
* youtube以外の動画配信サイトの動画を再生する
* 危機管理フォームへの変身

# discord招待リンク
https://discord.com/api/oauth2/authorize?client_id=1004242238202712215&permissions=274944175360&scope=bot

# 使い方
コマンドの先頭に「;（セミコロン）」を付けることで、シャミ子はあなたのメッセージがコマンドであることを認識します。

* ;in：シャミ子をあなたが入っているボイスチャンネルに招待できます。あなたがどこにも入っていない場合はシャミ子が混乱します。

* ;play{URL}：現在シャミ子が入っているボイスチャンネルで指定のURLのyoutubeを流してくれます。どこにも入っていない場合はシャミ子が混乱します。すでに音楽が再生されている場合は止めて新しく再生します。

* ;stop：今流している音楽を止めてくれます。何も流していないとシャミ子が混乱します。

* ;q：シャミ子がボイスチャンネルを退出します。

# 注意
* Youtubeには違法にアップロードされた楽曲が存在しますが、それらの楽曲の再生は自己責任でお願い致します。(それらの再生は推奨しません。)何らかのトラブルが発生した場合でも責任を取りません。  
* botが楽曲を再生する際は一度サーバーに音声データを保存し、それをボイスチャンネルで放送します。サーバーに保存されるとまずいような音声がある場合はご注意下さい。  
* bot経由で再生した動画は視聴回数としてはカウントされません。ループ再生で視聴回数を伸ばすことはできませんのでご注意下さい。  
* 1度ダウンロードした楽曲は2度目以降ダウンロード済みの音声データを再生する仕様になっています。  
* 異常な程の速度で楽曲を切り替える等、youtubeのサーバーに負荷をかけるような行為はご遠慮下さい。  
* youtubeの音声ダウンロードには十分高速なライブラリを使用していますが、大変大きな動画サイズであった場合（6時間とか）はそれなりの時間がかかりますのでご了承ください。  
* 現時点でyoutubeのストリーミング配信には対応していません。  
* botの仕様上広告は一切再生されないため、応援したい配信者の動画は直接見に行った方が良いと思います。
