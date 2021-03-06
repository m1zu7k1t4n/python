# coding: utf-8

class CardPack():
    standard_legend = (
        "ガブリエル",
        "ルシフェル",
        "サタン",
        "フェアリープリンセス",
        "エンシェントエルフ",
        "ローズクイーン",
        "海底都市王・乙姫",
        "ロイヤルセイバー・オーレリア",
        "ツバキ",
        "ミスリルゴーレム",
        "マーリン",
        "アークサモナー・エラスムス",
        "ファフニール",
        "ダークドラグーン・フォルテ",
        "ジルニトラ",
        "ケルベロス",
        "骸の王",
        "プルート",
        "クイーンヴァンパイア",
        "ソウルディーラー",
        "ビーストドミネーター",
        "スカルフェイン",
        "ムーンアルミラージ",
        "ジャンヌダルク",
    )
    evolved_legend = (
        "ダークエンジェル・オリヴィエ",
        "オーディン",
        "クリスタリアプリンセス・ティア",
        "アレキサンダー",
        "太陽の巫女・パメラ",
        "竜呼びの笛",
        "蝿の王",
        "ブラッディ・メアリー",
        "封じられし熾天使",
    )
    bahamut_legend = (
        "バハムート",
        "サハクィエル",
        "古き森の白狼",
        "レヴィオンセイバー・アルベール",
        "次元の魔女・ドロシー",
        "インペリアルドラグーン",
        "ネフティス",
        "血餓の女帝",
        "狂信の偶像",
    )
    standard_gold = (
        "ウルズ",
        "風神",
        "天翼を食う者",
        "アテナ",
        "冥府への道",
        "新たなる運命",
        "ペタルフェンサー",
        "リノセウス",
        "ノーブルフェアリー",
        "エンシェントフォレストドラゴン",
        "ロビンフッド",
        "ティターニアの妖精郷",
        "森の意志",
        "白銀の矢",
        "根源への回帰",
        "闇を纏う暗殺者",
        "ドラゴニュート・シャルロット",
        "宝杖の司令官",
        "フロントガードジェネラル",
        "ヴァンガード・レイサム",
        "騎士王の威光",
        "最前線",
        "軍師の妙策",
        "アルビダの号令",
        "エンシェントアルケミスト",
        "ドラゴンメイジ",
        "魔導の力場",
        "ノノの秘密研究室",
        "神秘の獲得",
        "次元の超越",
        "ファーストカース",
        "ファイアーチェイン",
        "冬の女王の気紛れ",
        "ドラゴニュートスカラー",
        "ジェネシスドラゴン",
        "騎竜兵",
        "変化する魔術師",
        "オーブドラゴン",
        "ハイドラ",
        "デスミストドラゴン",
        "竜化の塔",
        "鳳凰の庭園",
        "ワイトキング",
        "マダムリッチ",
        "ファントムドラゴン",
        "デスタイラント",
        "デュエリスト・モルディカイ",
        "悪霊の饗宴",
        "ファントムハウル",
        "腐の嵐",
        "死の祝福",
        "フリアエ",
        "デモンコマンダー・ラウラ",
        "エリニュス",
        "裁きの悪魔",
        "セクシーヴァンパイア",
        "メドゥーサ",
        "漆黒の契約",
        "ディアボリックドレイン",
        "黙示録",
        "光輝ドラゴン",
        "アークビショップ・レリア",
        "詠唱：夢想の白兎",
        "詠唱：神域の守護者",
        "祈りの集約",
        "詠唱：天喰らう聖竜",
        "テミスの審判",
        "愛の福音",
        "ダークオファリング",
    )
    evolved_gold = (
        "アークエンジェル・レイナ",
        "忌むべき悪魔の像",
        "エルフナイト・シンシア",
        "グランドアーチャー・セルウィン",
        "エルフの少女・リザ",
        "ホワイトパラディン",
        "レオニダス",
        "盗賊の極意",
        "古き魔術師・レヴィ",
        "白霜の風",
        "破砕の禁呪",
        "ネプチューン",
        "連なる咆哮",
        "竜巫女の儀式",
        "ケリドウェン",
        "魂の再利用",
        "死霊の宴",
        "アザゼル",
        "吸血姫・ヴァンピィ",
        "吸血鬼の古城",
        "カグヤ",
        "天空の守護者・ガルラ",
        "エイラの祈祷",
    )
    bahamut_gold = (
        "ウリエル",
        "ゴブリンブレイカー・ティナ",
        "ゴブリンスレイヤー・ルシウス",
        "セルウィンの号令",
        "宝石のエルフ",
        "マヘス",
        "天空城",
        "白銀の騎士・エミリア",
        "ファングスレイヤー",
        "エラスムスの秘儀",
        "プリンセスマナリア・アン",
        "禁忌の研究者",
        "サラマンダーブレス",
        "マナリアドラコ・グレア",
        "伊達政宗",
        "冥府神との契約",
        "バロール",
        "シャドウリーパー",
        "サディスティックナイト",
        "氷剣の戦鬼",
        "マステマ",
        "神魔裁判所",
        "煌角の戦士・サリッサ",
        "ヴァルハラジェネラル",
    )
    standard_silver = (
        "ベルエンジェル",
        "リザードマン",
        "ギルガメッシュ",
        "ゴブリンマウントデーモン",
        "エンジェルスナイプ",
        "エンジェルバレッジ",
        "エクスキューション",
        "光の道筋",
        "ワルツフェアリー",
        "ブレスフェアリーダンサー",
        "タムリン",
        "カニバルフラワー",
        "エルフプロフェテス",
        "エルダートレント",
        "フェアリービースト",
        "エルフプリンセスメイジ",
        "マナエルク",
        "フォレストジャイアント",
        "フォレストアケロウ",
        "収穫祭",
        "森の聖域",
        "メイドリーダー",
        "アサシン",
        "カースドジェネラル",
        "パーシヴァル",
        "ネイビールテナント",
        "ノーブルナイト",
        "わがままプリンセス",
        "ルミナスナイト",
        "プリンセスヴァンガード",
        "剣豪",
        "レイジングジェネラル",
        "鉄壁の城塞",
        "兵士徴集",
        "ジュエルゴーレム",
        "スペクトラルウィザード",
        "ウィッチクラフト・マギサ",
        "スカラーウィッチ",
        "クイーン・メイヴ",
        "フレイムウィッチ",
        "ルーンブレードサモナー",
        "錬金術の代償",
        "ゴーレムプロテクション",
        "アルケミックロア",
        "実験開始",
        "魔力の蓄積",
        "変成の魔術",
        "ドラゴニュートプリンセス",
        "グリムリーパー",
        "スカイドラコ・エチカ",
        "リヴァイアサン",
        "ライトニングベヒモス",
        "ドラゴンライダーデビル",
        "神龍",
        "プリズンドラゴン",
        "エースドラグーン",
        "ミストドラゴン",
        "黄金竜の棲家",
        "竜の伝令",
        "竜化の秘法",
        "スケルトンファイター",
        "デッドリーウィドウ",
        "ネクロエレメンタラー",
        "スカルライダー",
        "ゴエティアメイジ",
        "ソウルグラットン",
        "死都の女王",
        "魂飢の亡霊",
        "ソウルグラインダー",
        "デュラハン",
        "集団埋葬地",
        "再生の呪印",
        "幽体化",
        "復讐の悪魔",
        "モルモ",
        "ミッドナイトヴァンパイア",
        "ゲリュオン",
        "アルカード",
        "呪剣の吸血鬼",
        "ダークサモナー",
        "ヴァンパイアライカン",
        "仮面の殺戮者",
        "ヴァンパイアバード",
        "鮮血の花園",
        "夜の群れ",
        "獰猛な捕食",
        "教会の護り手",
        "プリズムプリースト",
        "クレリックランサー",
        "残忍な修道女",
        "ホワイトナイト",
        "加護の修道女",
        "レディアントシャーマン",
        "ホーリーメイジ",
        "神託の貴族",
        "シュラインナイトメイデン",
        "守護の陽光",
        "詠唱：聖獅子の牙",
        "詠唱：死の宣告",
    )
    evolved_silver = (
        "ユニコーンの踊り手・ユニコ",
        "ハンプティダンプティ",
        "烈火の魔弾",
        "千年妖狐・ユエル",
        "太古の森神",
        "エルフキング・ヴァルト",
        "エルフの弓術",
        "渾身の一振り",
        "ガンナーメイド・セリエ",
        "冷酷なる暗殺者",
        "コウガクノイチ",
        "デュアルウィッチ・レミラミ",
        "シャドウウィッチ",
        "連続実験",
        "氷像の召喚",
        "変異の巨竜",
        "ジークフリート",
        "ノクシャスロアードラゴン",
        "ドラゴニュートフィスト",
        "カローン",
        "アンドラス",
        "ボーンキマイラ",
        "死者の帰還",
        "ラビリンスデビル",
        "ジャガーノート",
        "貴き血牙",
        "メドゥーサの魔眼",
        "スレッジエクソシスト",
        "レディアンスエンジェル",
        "詠唱：獣姫の呼び声",
        "詠唱：禁じられた儀式",
    )
    bahamut_silver = (
        "氷獄の呼び声",
        "歴戦の傭兵・フィーナ",
        "天弓の天使・リリエル",
        "覇食帝・カイザ",
        "剣を樹に",
        "天馬のエルフ",
        "クリスタリア・リリィ",
        "エルフの王子・レオネル",
        "旋風刃",
        "蒼穹の提督・モニカ",
        "サブリーダー・ゲルト",
        "レヴィオンヴァンガード・ジェノ",
        "ルーンの貫き",
        "ディザスターウィッチ",
        "ドワーフアルケミスト",
        "神秘の探求者・クラーク",
        "竜の闘気",
        "ワイバーンライダー・エイファ",
        "輝石のドラゴン",
        "オウルガーディアン",
        "死霊の手",
        "ネクロアサシン",
        "よろめく不死者",
        "冥守の戦士・カムラ",
        "群れなす飢餓",
        "吸血貴・ヴァイト",
        "千雨の槍使い",
        "キャタラクトビースト",
        "ペガサスの結晶像",
        "エンシェントレオスピリット",
        "煌翼の戦士・リノ",
        "邪悪なる予言者・ダムス",
    )
    standard_bronze = (
        "ミノタウロス",
        "デザートライダー",
        "シールドエンジェル",
        "ヒーリングエンジェル",
        "研磨の魔法",
        "天上の楽曲",
        "デモンストライク",
        "ベビーエルフ・メイ",
        "ブレイブフェアリー",
        "ダンジョンフェアリー",
        "フェアリーブリンガー",
        "アーチャー",
        "沼の精",
        "ワンダーエルフメイジ",
        "フェアリーキャスター",
        "放浪するエルフ",
        "妖精の楽園",
        "まどろみの森",
        "自然の導き",
        "妖精のいたずら",
        "義賊の流儀",
        "精霊の呪い",
        "フェアリーサークル",
        "エレメンタルランス",
        "ニンジャエッグ",
        "不屈の兵士",
        "パレスフェンサー",
        "サイクロンソルジャー",
        "ケンタウロスヴァンガード",
        "フェンサー",
        "勇猛たる騎士",
        "セントリーナイト",
        "ノーヴィストルーパー",
        "スニッピーガーデナー",
        "歴戦のランサー",
        "ヴァンガード",
        "戦場の騎兵",
        "アドミラル",
        "激励の舞",
        "猛襲",
        "ジャイアントスレイヤー",
        "ペンギンウィザード",
        "クラフトウォーロック",
        "結界魔術師",
        "ルーンガーディアン",
        "ガントレットヒーラー",
        "ルーキーアルケミスト",
        "マスターアルケミスト",
        "旋風の魔術師",
        "怨恨の魔女",
        "上級アルケミスト",
        "雄大なる教え",
        "錬金工房",
        "初級錬金実験",
        "虹の輝き",
        "運命の導き",
        "地裂弾",
        "双璧の召喚",
        "アイボリードラゴン",
        "大嵐のドラゴン",
        "ドラゴンナイト・アイラ",
        "ツインヘッドドラゴン",
        "グリントドラゴン",
        "サンドストームドラゴン",
        "海剣竜",
        "スカルドラゴン",
        "インフェルノドラゴン",
        "ルフ鳥",
        "ファイアーリザード",
        "トリニティドラゴン",
        "氷結のドラゴン",
        "竜の翼",
        "竜の咆哮",
        "竜の力",
        "ワイルドハント",
        "スケルトンヴァイパー",
        "スカルウィドウ",
        "纏わりつく亡霊",
        "ラビットネクロマンサー",
        "スケルトンナイト",
        "ワイト",
        "カースドソルジャー",
        "ソウルイーター",
        "スパルトイ",
        "オルクス",
        "レッサーマミー",
        "スカルビースト",
        "ギルティクーリエ",
        "ソウルコンバージョン",
        "死への近道",
        "ソウルハント",
        "汚れた再生",
        "リリム",
        "ヴェノムコブラ",
        "レイニーデビル",
        "蠢く死霊",
        "ブラッドウルフ",
        "メタルガーゴイル",
        "キラーデビル",
        "憤怒の巨人",
        "バーバリックデーモン",
        "強欲な魔獣",
        "デモンハンドアサシン",
        "ランページジャイアント",
        "デモンスナイパー",
        "サキュバス",
        "リミルの秘密",
        "眷属の召喚",
        "ブラッドレイジ",
        "ラビットヒーラー",
        "アーデントシスター",
        "見習いシスター",
        "ダークプリースト",
        "ガーディアンシスター",
        "ヒールプリースト",
        "ディバインアーマー",
        "マスクジャイアント",
        "マイニュ",
        "敬虔な修道女",
        "詠唱：白翼への祈り",
        "詠唱：聖なる願い",
        "詠唱：異端審問",
        "詠唱：清浄の狐",
        "詠唱：神鳥の呼び笛",
        "守護の力",
        "治癒の祈り",
    )
    evolved_bronze = (
        "インペリアルマンモス",
        "レイジングエティン",
        "死の舞踏",
        "魔術書の解読",
        "パフュームドワーフ",
        "エルフバード",
        "癒しのエルフ",
        "森隠れの獣人",
        "深緑の守護者",
        "翅の輝き",
        "スウィフトペネトレーター",
        "勇敢なる旗手",
        "アサルトコマンダー",
        "アドバンスブレーダー",
        "ミラージュディフェンサー",
        "師の教え",
        "水晶の魔撃手",
        "ベビーウィッチ・エミル",
        "グランドガーゴイル",
        "くず鉄の練成",
        "魔女の雷撃",
        "炎熱の術式",
        "鉄鱗の竜人",
        "ムシュフシュ",
        "荒牙の竜少女",
        "アイランドホエール",
        "クイーンサーペント",
        "竜の知恵",
        "ダークコンジュラー",
        "死を追う者",
        "マリスゴースト",
        "デストロイヤーズコマンダー",
        "スパルトイソルジャー",
        "死の一閃",
        "享楽の悪魔",
        "ソウルミニデビル",
        "デモンスラル",
        "サーペントチャーマー",
        "ソウルナビゲーター",
        "鮮血の口付け",
        "天界の忠犬",
        "スカイスピリット",
        "ホーリーフォックス・グリモー",
        "翼の王子",
        "詠唱：神鉄の翼",
        "僧侶の聖水",
    )
    bahamut_bronze = (
        "戦乙女の槍",
        "ミニゴブリンメイジ",
        "セクトール",
        "御言葉の天使",
        "ハンサ",
        "絡みつく蔦",
        "フェアリーナイト",
        "フォレストスピリット",
        "ベビーフェルパー",
        "フォレストギガース",
        "ニンジャアーツ",
        "ブリッツランサー",
        "ソードウィップメイド",
        "サムライ",
        "シーフ",
        "破魔の術式",
        "マナリアウィザード・クレイグ",
        "タイムレスウィッチ",
        "ゲイザー",
        "刃の魔術師",
        "竜爪の首飾り",
        "ワイリーワイバーン",
        "グリフォンナイト",
        "ドラゴンテイマー",
        "煌牙の戦士・キット",
        "怨嗟の声",
        "怪犬の墓守",
        "双翼の警護者",
        "闇の従者",
        "海賊ゾンビ",
        "処刑人の斧",
        "レヴィオンデューク・ユリウス",
        "ジュエルデビル・モリアナ",
        "人狼の群れ長",
        "高慢なる悪魔",
        "信仰の具現化",
        "マスターレディセージ",
        "ソウルコレクター",
        "フロッグクレリック",
        "熟達の調教師",
    )
