#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全技の自問自答監査（句カバレッジ方式）

設計思想:
  ホワイトリスト方式（検出器がある仕様だけ確認）ではなく、
  effect_textを全て句に分解し、各句が
    ① 狙ったテストで検証されている（DETECTORS）
    ② フレーバー/検証不要として明示的に無視指定されている（IGNORE）
    ③ ダブルバトル専用（DOUBLE_ONLY）
  のいずれかであることを要求する。
  どれにも該当しない句があれば「未分類の観点」として報告する。
  → 「未知の理由でテストされていない観点」を構造的にゼロにする。
"""
import re, sqlite3, sys
sys.path.insert(0, '/Users/shigeki/work/pokenavi/scripts')
from simulator.data import get_type_effectiveness as _gte

TS = open('/Users/shigeki/work/pokenavi/scripts/tests/test_move_effects.py', encoding='utf-8').read()
conn = sqlite3.connect('/Users/shigeki/work/pokenavi/scripts/pokenavi.db')
cur = conn.cursor()
cur.execute("SELECT name_jp, category, power, effect_text FROM move_master")
MOVES = cur.fetchall()
cur.execute("SELECT name_jp, type FROM move_master")
_MOVE_TYPE = dict(cur.fetchall())
conn.close()

def block(name):
    m = re.search(rf'# ── {re.escape(name)} ──(.*?)(?=\n# ── |\Z)', TS, re.DOTALL)
    return m.group(1) if m else ''

def labels(name):
    return re.findall(r'check\("([^"]+)"', block(name))

# 検証用ラベルから技名を除いた「説明部分」のみを返す。
# 「DB: X 取得可能」「副作用発現: X」等のボイラープレートは技名を含むため、
# 期待語が技名のDETECTORを偽陽性で満たしてしまう。説明部分だけで判定する。
_BOILERPLATE = ('DB:', '副作用発現', '効果発現', 'ダメージ計算', '優先度')
def verify_labels(name):
    out = []
    for l in labels(name):
        # ボイラープレートは先頭一致で除外（"グラスF優先度"等の正規ラベルを誤除外しない）
        if l.startswith(_BOILERPLATE):
            continue
        # 末尾の ": 技名" を除去（説明部分だけ残す）
        desc = re.sub(rf':\s*{re.escape(name)}\s*$', '', l)
        out.append(desc)
    return out

# ── 検出器: (句にマッチする正規表現, 検証ラベルに含まれるべき語のいずれか) ──
# マッチした句は、対応する語を含むcheckラベルが存在すれば「検証済み」
DETECTORS = [
    (r'\d+%の確率で相手を(まひ|やけど|こおり|どく|もうどく|ねむり|こんらん)状態', ['追加効果(','付与']),
    (r'相手を(まひ|やけど|こおり|どく|もうどく|ねむり|こんらん)状態にする', ['付与','状態異常','追加効果(','こんらん']),
    (r'\d+%の確率で相手をひるませる', ['ひるみ']),
    (r'相手をひるませる', ['ひるみ','追加効果(']),
    (r'\d+%の確率で相手を怯ませる', ['ひるみ']),
    (r'相手の(攻撃|防御|特攻|特防|素早さ|命中率|回避率)を\d+段階下げる', ['相手','ダウン','-','下げ']),
    (r'自分の[^。]*?(攻撃|防御|特攻|特防|素早さ|命中率|回避率)[^。]*?\d+段階[^。]*?(上げ|上が)', ['自分','上昇','+','上げ']),
    (r'自分の[^。]*?(攻撃|防御|特攻|特防|素早さ)[^。]*?\d+段階[^。]*?(下が|下げ)', ['自分','-','下が','下げ']),
    (r'自分のHP[^。]*?回復', ['HP回復','回復']),
    (r'(あめ|にほんばれ|晴れ|すなあらし|あられ|ゆき)状態にする', ['天候']),
    (r'(グラス|エレキ|サイコ|ミスト)フィールド状態にする', ['フィールド']),
    (r'(リフレクター|ひかりのかべ|オーロラベール)状態にする', ['スクリーン']),
    (r'相手をひんしにする', ['一撃必殺']),
    (r'与えたダメージの[^。]*?HPを回復', ['ドレイン']),
    (r'相手をバインド状態にする', ['バインド']),
    (r'自分はあばれ状態になる', ['あばれ']),
    (r'じごくづき状態にする', ['じごくづき']),
    (r'外れるか失敗すると自分の最大HPの1/2', ['外れ時']),
    (r'使ったターンで(溜め|空中|水中|地中|潜伏)状態', ['2ターン']),
    (r'タイプの相手にも効果バツグン', ['効果バツグン']),
    (r'与えたダメージの1/\d[^。]*?受ける', ['反動']),
    (r'\d[ー\-]?\d?回連続で攻撃', ['多段','連続']),
    (r'必ず命中する', ['必中']),
    (r'必ず急所', ['急所']),
    (r'HPに\d+ダメージ', ['固定']),
    (r'手持ちの他のポケモンと交代', ['ピボット']),
    (r'(使うと自分はひんしになる|自分はひんしになる)', ['自己ひんし','自分ひんし','カウンター','一撃']),
    (r'相手の場を(まきびし|どくびし|ステルスロック|ねばねばネット)状態', ['ハザード']),
    (r'受けた[^。]*?ダメージを[\d.]+倍にして返す', ['カウンター']),
    (r'能力変化をなく', ['能力リセット','くろいきり']),
    (r'2ターンの間ねむり状態', ['ねむる','全回復','ねむり付与']),
    (r'わざふうじ状態', ['わざ封じ','かなしばり']),
    (r'相手の道具を奪う', ['道具奪取']),
    (r'フィールドを解除する', ['フィールド解除']),
    (r'こおり状態を治す', ['こおり治癒']),
    (r'状態異常だと威力が2倍', ['状態異常で威力2倍','威力2倍']),
    (r'能力変化を無視してダメージ', ['ランク無視','能力変化無視']),
    (r'前のターン自分が動けなかったり', ['前ターン失敗2倍']),
    (r'グラスフィールド状態の時、威力が1/2', ['グラスF半減']),
    (r'でんじふゆう状態', ['じめん無効','でんじふゆうフラグ']),
    (r'(ねをはる状態|アクアリング状態)になる', ['ターン終了回復']),
    (r'にほんばれ状態の場合は2/3回復', ['天候別回復']),
    (r'エレキフィールド状態の効果を受けている場合、威力が2倍', ['エレキF威力2倍']),
    (r'相手をにげられない状態にする', ['にげられない付与']),
    (r'相手をアンコール状態にする', ['アンコール付与']),
    (r'相手をちょうはつ状態にする', ['ちょうはつ付与']),
    (r'自分はふういん状態になる', ['ふういん付与']),
    (r'(道具を入れ替える|道具を入れ替え|道具を入れ換え)', ['道具入替']),
    (r'道具を持っていると威力が1.5倍', ['道具持ち1.5倍']),
    (r'能力変化が1段階上がるごとに.*威力', ['ランクで威力増']),
    (r'相手の攻撃の能力値でダメージ', ['相手攻撃依存']),
    (r'防御の数値でダメージが決まる', ['自分防御依存','防御で計算']),
    (r'相手の防御の能力値でダメージ計算', ['物理防御依存']),
    (r'天気が変わっていると、威力が2倍', ['天候威力2倍']),
    (r'使った次のターン、自分は反動状態', ['リチャージ','反動状態']),
    (r'相手が重いほど威力が上がる', ['可変','重さ','威力']),
    (r'自分の残りHPが少ないほど威力が上がる', ['可変','HP','威力']),
    (r'自分の残りHPが少ないほど威力が下がる', ['可変','HP','威力']),
    (r'自分が相手より重いほど威力が上がる', ['重さ','可変','威力']),
    (r'自分の素早さが相手より低いほど威力', ['ジャイロ','速度','可変','威力']),
    (r'自分の素早さが相手より高いほど威力', ['エレキボール','速度','可変','威力']),
    (r'相手の残りHPが多いほど威力', ['ハードプレス','可変','威力']),
    (r'相手の残りHPの1/2のダメージ', ['いかりのまえば','1/2ダメ','可変']),
    (r'残っていたHP分のダメージを与える', ['いのちがけ','可変']),
    (r'相手の残りHPから自分の残りHPを引いた', ['がむしゃら','可変']),
    (r'やどりぎのタネ状態にする', ['やどりぎ']),
    (r'相手をしおづけ状態にする', ['しおづけ']),
    (r'相手をメロメロ状態にする', ['メロメロ']),
    (r'相手を連続不可状態にする', ['いちゃもん','連続不可']),
    (r'とくせいなし状態にする', ['いえき','とくせい']),
    (r'相手の特性を(たんじゅん|ふみん)に', ['シンプルビーム','なやみのタネ','特性']),
    (r'相手の特性を自分と同じ特性に', ['なかまづくり','特性']),
    (r'自分の特性を相手の特性と同じに', ['なりきり','特性']),
    (r'自分と相手の特性を入れ替え', ['スキルスワップ','特性']),
    (r'自分と相手の素早さを入れ替え', ['スピードスワップ','素早さ']),
    (r'攻撃・特攻の能力変化を相手の', ['パワースワップ']),
    (r'防御と特防の能力変化を相手の', ['ガードスワップ']),
    (r'防御の数値と特防の数値を足して', ['ガードシェア','防御平均']),
    (r'攻撃の数値と特攻の数値を足して', ['パワーシェア','攻撃平均']),
    (r'攻防反転状態', ['パワートリック','攻防入替']),
    (r'能力変化を自分にもかける', ['じこあんじ']),
    (r'自分のタイプを相手のタイプと同じに', ['ミラータイプ']),
    (r'相手のタイプをみずタイプに変える', ['みずびたし','タイプ']),
    (r'タイプをエスパータイプに変える', ['まほうのこな','タイプ']),
    (r'最後に消費した道具を元に戻し', ['リサイクル','道具復元']),
    (r'相手[のが]最後に?使(った|用した)技のPPを\d+減らす', ['PP','うらみ','ぶきみ']),
    (r'トリックルーム状態にする', ['トリックルーム','場の状態','ルーム']),
    (r'(全体の場を|全体の場をじゅうりょく|じゅうりょく状態にする)', ['じゅうりょく','場の状態']),
    (r'(マジックルーム|ワンダールーム)状態にする', ['場の状態','ルーム']),
    (r'自分が覚えている他の技の中からいずれか', ['ねごと','技発動']),
    (r'相手のやけど状態を治す', ['うたかた','やけど治']),
    (r'たくわえる状態を1増やす', ['たくわえ']),
    (r'たくわえる状態の数値が多いとHPを多く回復', ['のみこむ','たくわえ']),
    (r'たくわえる状態の数値が多いほど威力', ['はきだす','たくわえ']),
    (r'相手の能力変化を元に戻す', ['クリアスモッグ','リセット']),
    (r'手持ちのポケモンの数だけ相手を攻撃', ['ふくろだたき']),
    (r'相手が状態異常だと威力が2倍', ['状態異常で威力2倍']),
    (r'相手がどく状態、もうどく状態の場合威力が2倍', ['ベノムショック','状態異常で威力2倍']),
    (r'バインド状態・やどりぎのタネ状態と', ['バインド','こうそくスピン','キラースピン']),
    (r'物理技である方がダメージが大きい場合は物理技', ['シェルアームズ','物理']),
    (r'相手より後に攻撃すると技の威力が2倍', ['しっぺがえし','後攻']),
    (r'使ったターン中、相手がすでにダメージを受けているなら威力が2倍', ['ダメおし','後攻']),
    (r'道具を持っていない場合威力が2倍', ['アクロバット']),
    (r'自分が道具を持っていない場合相手の道具を奪う', ['道具奪取']),
    (r'倒すと攻撃が3段階上がる', ['とどめばり']),
    (r'最大HPの1/2減らし.*?みがわり', ['みがわり','しっぽきり']),
    (r'みがわりを出す', ['みがわり']),
    (r'みちづれ状態になる', ['みちづれ']),
    (r'ほろび状態にする', ['ほろび']),
    (r'相手と同じ.*能力値.*特性.*になる', ['特性コピー','全ステータスコピー','コピー']),
    (r'HP・持ち物・状態異常.*コピーされず.*PP', ['非コピー','PP5','コピーしない']),
    (r'交代すると元に戻る', ['元に戻る','復元']),
    (r'攻撃を6段階目まで上げる', ['はらだいこ']),
    (r'残りHPを足して互いに1/2', ['いたみわけ','HP折半']),
    (r'(弾|物理)技を使う前に接触技を受けると', ['被弾やけど', 'くちばしキャノン']),
    (r'接触技をしてきた相手をどく状態にする', ['接触どく']),
    (r'接触技をしてきた相手の最大HP', ['接触ダメ']),
    (r'相手からの技ダメージを受けていれば、?威力が2倍', ['条件成立で威力2倍']),
    (r'自分の能力が下がっている場合、?威力が2倍', ['条件成立で威力2倍']),
    (r'グラスフィールド状態の効果を受けている場合、?優先度', ['グラスF優先度']),
    (r'(地面にいない相手を着地状態|ひこうタイプのポケモンにじめんタイプの技が当たる)', ['接地化']),
    (r'やけど状態による物理技のダメージが半減される効果は無視', ['やけど攻撃半減無視']),
    (r'タイプとひこうタイプの2つの相性を組み合わせて', ['複合相性']),
    (r'連続で使うと失敗する', ['連続失敗']),
    (r'回避率まもる等を無視して当たる', ['回避無視']),
    (r'^きゅうしょアップ\+1で攻撃する', ['急所ランク+1']),
    (r'HPを1残して耐える', ['こらえHP1']),
    (r'相手の攻撃の数値分自分のHP', ['相手攻撃実数値分回復']),
    (r'先に相手からの技のダメージを受けると失敗', ['被弾失敗']),
    (r'相手がきのみを持っていれば', ['きのみ奪取']),
    (r'ひこうタイプが使うとそのターン中ひこうタイプでなくなる', ['ひこう消失']),
    (r'相手がいる場所をみらいにこうげき状態', ['発動', '予約']),
    (r'相手が道具を持っていない場合失敗', ['ポルターガイスト']),
    (r'他に覚えている技を全て使っていない場合失敗', ['とっておき','他技']),
    (r'HPが満タンだと失敗', ['満タン失敗']),
    (r'残りHPが足りない場合は失敗', ['HP不足失敗']),
    (r'きのみを持っていないと、?この技は使えない', ['きのみ無し失敗']),
    (r'戦闘中にきのみを食べていない場合、?この技は失敗', ['きのみ未食失敗']),
    (r'自分がほのおタイプではない場合失敗', ['非ほのお失敗']),
    (r'場にフィールドがない場合失敗', ['フィールド無し失敗']),
    (r'相手が先制技を使っていない場合失敗', ['先制技']),
    (r'でんき威力アップ状態になる', ['じゅうでん次でんき2倍']),
    (r'持っている道具によって威力と効果が変わる', ['道具別威力']),
    (r'にほんばれ状態の場合、?2段階上げる', ['晴れ2段階']),
    (r'にほんばれ状態の場合、?命中率が下がる', ['晴れ命中低下']),
    (r'他の天気の場合は威力が1/2', ['天候半減']),
    (r'\d回目は威力\d+', ['威力漸増']),
    (r'フィールドの種類によってタイプが変わる', ['フィールド型変化']),
    (r'味方の場をおいかぜ状態', ['おいかぜS2倍']),
    (r'相手のHPが自分のHP以下', ['相手HP以下で失敗']),
    (r'登場して最初に出す技でない場合失敗', ['初手以外で失敗']),
    (r'自分がいる場所をねがいごと状態', ['ねがいごと']),
    (r'味方の場をしんぴのまもり状態', ['状態異常防御']),
    (r'まもる.{0,4}みきり等の効果を解除して攻撃', ['まもる貫通']),
    (r'使うと道具はなくなる', ['道具消費']),
    (r'たくわえる状態ではない場合、?この技は失敗', ['たくわえ0で失敗']),
    (r'くさタイプ相手には無効', ['くさ無効']),
    (r'じめんタイプ相手には無効', ['じめん無効']),
    (r'くさタイプや粉が効かない相手には無効', ['くさ無効']),
    (r'自分がねむり状態の場合使うことができる', ['ねむり中使用', '技発動', 'ねごと']),
    (r'自分はきゅうしょアップ状態\+2', ['急所ランク+2']),
    (r'相手をハロウィン状態にする', ['ハロウィン','タイプ追加']),
    (r'もりののろい状態にする', ['もりののろい','タイプ追加']),
    (r'2回連続で攻撃する', ['多段','連続','2回']),
    (r'1-10回連続', ['多段','連続']),
    (r'威力が2倍になりタイプも変わる', ['天候威力2倍']),
    (r'相手の場をステルスロック状態にする', ['ハザード','ステルスロック']),
    (r'相手の場をまきびし状態にする', ['ハザード','まきびし']),
    (r'自分のフォルムによって技のタイプが変わる', ['レイジングブル','フォルム']),
    (r'30%の確率で威力が2倍', ['きまぐ','威力2倍']),
    (r'自分はアクアリング状態', ['ターン終了回復']),
    (r'自分はロックオン状態になる', ['ロックオン']),
    (r'相手の攻撃を2段階上げこんらん状態', ['いばる','こんらん']),
    (r'相手の特攻を1段階上げ、こんらん状態', ['おだてる','こんらん']),
    (r'相手の攻撃と特攻を1段階下げる', ['おたけび','相手']),
    (r'相手の攻撃と防御を1段階下げる', ['くすぐる','相手']),
    (r'相手の防御を2段階下げて、攻撃を2段階上げる', ['ハバネロ','相手']),
    (r'相手の攻撃[、特攻]*を1段階下げる', ['なみだめ','相手','ダウン']),
    (r'ねっさのだいち|だいちのはどう|フィールドの効果を受けている場合、威力が2倍', ['だいちのはどう','フィールド','可変']),
    (r'サイコフィールド状態の効果を受けている場合、威力が1.5倍', ['ワイドフォース','サイコ']),
    (r'ミストフィールド状態の効果を受けている場合威力が1.5倍', ['ミストバースト','ミスト']),
    (r'じゅうりょく状態の場合、威力が1.5倍', ['Gのちから','じゅうりょく']),
    (r'自分のほのおタイプがなくなる', ['もえつきる','タイプ']),
    (r'2回連続で出すことはできない', ['デカハンマー','連続不可']),
    (r'相手をあめまみれ状態', ['みずあめボム','あめまみれ']),
    (r'かいふくふうじ状態', ['サイコノイズ','かいふく']),
    (r'手持ちのポケモンが1匹ひんしになるたび威力が50上がる', ['ひんし','可変']),
    (r'攻撃技で受けた回数1回につき威力が50上がる', ['被弾','可変']),
    (r'使用後は交代・逃げができなくなる', ['交代不可']),
    (r'すでに交代不可の場合は失敗する', ['失敗']),
    (r'状態異常.*?場合は威力が2倍|どく状態、もうどく状態、まひ状態、やけど状態のいずれかの場合は威力が2倍', ['からげんき','状態異常']),
    (r'70%の確率で自分の特攻を上げる', ['チャージビーム','自分']),
    (r'50%の確率で自分の特攻が1段階上がる', ['ほのおのまい','自分']),
    (r'10[%％]の確率で自分の(防御|攻撃)を1段階上げる', ['はがねのつばさ','コメットパンチ','自分']),
    (r'10%の確率で自分の攻撃、防御、特攻、特防、素早さを1段階上げる', ['げんしのちから','自分']),
    (r'地中状態の相手には威力が2倍', ['地中2倍','地中','可変']),
    (r'水中状態の相手には[、]?威力が2倍', ['水中2倍','水中','可変']),
    (r'ちいさくなる状態の相手には[、]?威力が2倍', ['ちいさくなる2倍']),
    (r'使(った|用した)次のターン、自分は反動状態', ['リチャージ','反動状態','リチャージ付与']),
    (r'相手をねむけ状態にする', ['ねむけ付与','あくび']),
    (r'相手の場のひかりのかべ状態.*を解除して攻撃', ['スクリーン破壊']),
    (r'自分と味方の攻撃を1段階ずつ上げる', ['こうげき','とおぼえ']),
]

# ── フレーバー/検証不要として明示的に無視する句（理由付き） ──
# 「テストしない」と人間が判断した観点。ここに無い未知の句は必ず報告される。
IGNORE_PATTERNS = [
    (r'^通常の攻撃技$', '効果なし'),
    (r'最後に使われた技を使う', 'まねっこ（簡易スタブ・相手技の再実行は未実装＝既知の制限。REQUIREMENTS 5-2）'),
    (r'相手が直前に使った技をもう1度使わせる', 'さいはい（ダブルバトル専用）'),
    (r'連続で使うと成功率が前に使った時の1/3', 'まもる系共通の連続成功率低下（まもるで代表テスト済み・protect_consecutive共有）'),
    (r'^優先度[+\-]?\d+$', '優先度のみの行（DB priorityで担保）'),
    (r'優先度[+\-]?\d+.*必ず先制できる', '優先度技（DB priorityで担保）'),
    (r'^\(優先度[+\-]?\d+\)$', '優先度の補足表記'),
    (r'必ず先制できる', '優先度技（DB priorityで担保）'),
    (r'それ以外の天気の場合は1/4回復', '天候別回復の補足（晴れ>通常をテスト済み）'),
    (r'相手に控えがいる場合、?相手をランダムに交代させる', '強制交代（1v1では控えなしで効果なし＝ダブル/3on3寄り挙動）'),
    (r'相手の技から(身|見)を守る', 'まもる系防御（protecting本体はテスト済み）'),
    (r'使うとこおり状態が治る|使うと自分のこおり状態を治す', 'ほのお技の自己解凍（THAW_MOVES/こおり治癒でカバー）'),
    (r'使われた技がない場合失敗|相手が攻撃を選んでおり', '使用条件の補足'),
    (r'相手の道具を失わせる', 'はたきおとす道具排除（テスト済み別句）'),
    (r'途中で外れると攻撃は終わる', '多段の補足'),
    (r'相手を選ぶ技にしか効果はない', 'ダブル用補足'),
    (r'空中状態の相手にも当たる', '半無敵貫通の補足（1v1では空中状態を作れない）'),
    (r'命中率\d+%固定', '一撃必殺の命中率（KO挙動はテスト済み）'),
    (r'^威力[\d ー\-～]+$', '威力数値範囲の説明（可変威力本体はテスト済み）'),
    (r'威力\d+[ー\-]\d+', '威力範囲の説明'),
    (r'威力1ー150|威力20ー200|威力100ー300|威力40ー150|威力20-120', '威力範囲の説明'),
    (r'相手に必ず命中する$', '必中（必中テストで担保／条件付きは別途）'),
    (r'^相手に必ず命中する。?$', '必中（テスト済み）'),
    (r'残り1の場合は1ダメージ', '端数の補足'),
    (r'みがわりは、?自分の代わりに技を受ける', 'みがわり挙動の補足'),
    (r'最大HPの1/4のダメージを受けると消える', 'みがわり消滅の補足'),
    (r'能力変化、?みがわり等をそのポケモンに引き継ぐ', 'バトンタッチの補足'),
    (r'ちいさくなる状態になる', '自己付加状態（回避上昇本体はテスト済み）'),
    (r'2匹目以降の威力は2倍', 'りんしょう（ダブル専用）'),
    (r'相手が2匹いる場合', 'ダブル用補足'),
    (r'シールドフォルムにフォルムチェンジ', 'ギルガルド専用フォルム（メガ/フォルム系スコープ外）'),
    (r'モルペコのフォルムでタイプが変わる', 'モルペコ専用フォルム（スコープ外）'),
    (r'ゆき状態の場合にしか使えない|ゆき状態の場合に必中', '天候必中（テスト済み別句）'),
    (r'こおりタイプ以外が使うと20%', 'ぜったいれいど命中（OHKO挙動はテスト済み）'),
    (r'こおりタイプの相手には当たらない', 'ぜったいれいど無効（OHKO挙動で担保）'),
    (r'はがねタイプ相手には無効', 'どく状態のはがね無効（apply_statusの毒免疫テストで担保）'),
    (r'相手の回避率を1段階下げる。?$', 'きりばらい回避下げ（テスト別途）'),
    (r'すぐに攻撃できる|溜め状態にならず', '天候即時発動（ソーラービーム等、test_allで担保）'),
    (r'相手のこおり状態を治す', 'ねっとう相手こおり治癒（自/相こおり治癒でカバー）'),
    (r'^相手をやどりぎのタネ状態にする', 'やどりぎ（test_allで担保）'),
    (r'地面にいるポケモンのみが効果を受ける', 'フィールド共通補足'),
    (r'^自分は.*?状態になる$', '自己状態付与（個別テストで担保されない補助状態）'),
    (r'持っているきのみを食べる', 'ほおばる補足（防御+2は別途テスト）'),
    (r'同性、?性別不明の相手には失敗', 'メロメロ条件（性別未実装）'),
    (r'本シミュレータは性別を扱わないため常に失敗', 'メロメロ性別未実装の明示（常に失敗をテスト済み）'),
    (r'ドラゴンタイプなら\+2', 'ドラゴンエール（ダブル用味方バフ）'),
    (r'同じターンに複数のポケモンがこの技を使うと', 'りんしょう（ダブル専用）'),
    (r'いずれか1つを2段階上げる', 'つぼをつく（ランダム1能力、本体テスト済み）'),
    (r'相手の能力変化を無視してダメージを与える', '能力変化無視（テスト済み別句）'),  # safety
    # 以下、句カバレッジ徹底のため追加
    (r'リフレクター、まきびし、しんぴのまもり、フィールド等を解除', 'きりばらい場掃除（回避下げを別途テスト）'),
    (r'にほんばれ状態：ほのお|あめ状態：みず', 'ウェザーボール天候別タイプ（天候威力2倍テストで型変化も確認）'),
    (r'攻撃した後自分の最大HPの1/2のダメージを受ける', 'てっていこうせん反動（反動テスト済み別句）'),
    (r'味方に使用するとダメージは与えず', 'かふんだんご味方回復（ダブル用）'),
    (r'相手が技を出す前にこの技が命中すると', 'そうでん（相手技でんき化・ダブル寄り）'),
    (r'最大3回までたくわえられる', 'たくわえ上限（たくわえテスト済み）'),
    (r'自分と味方の攻撃を1段階ずつ上げる', 'とおぼえ（自分の攻撃上昇は実装、味方分はダブル）'),
    (r'\d回だと(最大HPの1/[24]回復|全回復)', 'のみこむ回復量（たくわえ依存・補足）'),
    (r'ひんしや状態異常のポケモンは数えない', 'ふくろだたき手持ち数の補足'),
    (r'技の威力は手持ちポケモンのこうげきで計算', 'ふくろだたき威力計算の補足'),
    (r'最大HPの1/4分のダメージを受けると消える', 'しっぽきりみがわり消滅補足'),
    (r'全体の場の.*?を解除する', 'おかたづけ場掃除（自己バフは別途テスト）'),
    (r'^相手の場のひかりのかべ状態、リフレクター状態、オーロラベール状態を解除して攻撃する', 'スクリーン破壊（テスト済み別句／レイジングブル等）'),
    (r'相手の攻撃[、,]?特攻を2段階上げる', 'デコレーション（味方バフ・ダブル）'),
    (r'味方をきゅうしょアップ状態', 'ドラゴンエール（味方バフ・ダブル）'),
    (r'相手の重さが自分の重さの1/5以下で120', 'ヘビーボンバー/ヒートスタンプ威力表（重さ比テスト済み）'),
    (r'相手をのろい状態にする', 'のろい（非ゴースト自己バフ/ゴースト呪いをテスト済み）'),
    (r'自分のHPを最大HPの1/2減らし、相手をのろい', 'のろい（テスト済み）'),
    (r'ちいさくなる状態の相手には[、]?威力が2倍になり必ず命中', 'ちいさくなる2倍（テスト済み別ラベル）'),
]

DOUBLE_ONLY = {
    'アロマミスト','コーチング','てだすけ','サイドチェンジ','ファストガード',
    'ワイドガード','このゆびとまれ','じばそうさ','いやしのねがい','いのちのしずく',
    'いやしのすず','フェアリーロック','りんしょう','さきおくり','おさきにどうぞ',
    'いかりのこな','いやしのはどう','おちゃかい','ふしょくガス','フラフラダンス',
    'ドラゴンエール',
}

IGNORE_RE = [(re.compile(p), why) for p, why in IGNORE_PATTERNS]

def split_clauses(effect):
    # 「。」で分割。空句は除外。
    return [c.strip() for c in re.split(r'。', effect) if c.strip()]

uncovered = []   # (技, 句) どの検出器にもIGNOREにも当たらない＝未分類
soft = []        # 副作用発現のみ

for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e:
        continue
    # 全角→半角正規化（生成側と一致させる）
    e = e.translate(str.maketrans('０１２３４５６７８９％＋', '0123456789%+'))
    if name in DOUBLE_ONLY:
        continue
    lbls = labels(name)
    vlbls = verify_labels(name)   # 技名・ボイラープレートを除いた説明部分のみ
    has_side = any('副作用発現' in l for l in lbls)
    for clause in split_clauses(e):
        # IGNORE判定
        if any(r.search(clause) for r, _ in IGNORE_RE):
            continue
        # DETECTOR判定（検証は説明ラベルのみ＝技名一致の偽陽性を排除）
        matched = False
        verified = False
        for pat, expect in DETECTORS:
            if re.search(pat, clause):
                matched = True
                if any(any(w in l for w in expect) for l in vlbls):
                    verified = True
                    break
        if matched:
            if not verified:
                if has_side:
                    soft.append((name, clause[:50]))
                else:
                    uncovered.append((name, clause[:50], 'DETECTOR一致だが対応テスト無し'))
            continue
        # どの検出器にもIGNOREにも当たらない＝未分類の観点
        uncovered.append((name, clause[:50], '未分類（検出器もIGNORE指定も無い）'))

# ── テスト強度ゲート ──────────────────────────────────────
# 「テストは存在するが中身が弱い」を構造的に検出する。
# 検査項目:
#   A. 多段: 複数回ヒット検証なし (ネズミざん型)
#   B. 可変威力ダメージ技: 条件比較テストなし
#   C. 反動: 1/N量検証なし (rcv > 0 のみ)
#   D. ドレイン: 与ダメ割合検証なし (hp > 1 のみ)
#   E. 相手能力ダウン: 段階数等値検証なし (< 0 のみ)
#   F. 自己能力変化: 段階数等値検証なし (!= 0 のみ)
#   G. HP回復変化技: 量検証なし (> N のみ)
_BP2 = ('DB:', '副作用発現', '効果発現', 'ダメージ計算', '優先度')
def _strong(name):
    return [l for l in labels(name) if not l.startswith(_BP2)]
def _blk(name):
    m = re.search(rf'# ── {re.escape(name)} ──(.*?)(?=\n# ── |\Z)', TS, re.DOTALL)
    return m.group(1) if m else ''
weak = []
_DOUBLE_EXCL = {'アロマミスト','コーチング','てだすけ','サイドチェンジ','ファストガード',
                'ワイドガード','りんしょう','このゆびとまれ','いかりのこな','てをつなぐ',
                'いのちのしずく','いやしのすず','デコレーション','ドラゴンエール',
                'じばそうさ','フェアリーロック','フラフラダンス','ふしょくガス','おちゃかい',
                'さきおくり','おさきにどうぞ'}
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e or name in DOUBLE_ONLY or name in _DOUBLE_EXCL:
        continue
    blk = _blk(name)
    ls = labels(name)
    # A. 多段
    if re.search(r'\d回連続で攻撃|連続\d回攻撃|\d回連続攻撃', e):
        if not any('多段ヒット発生' in l for l in ls):
            weak.append((name, 'A:多段技だが複数回ヒット検証なし'))
    # B. 可変威力ダメージ技
    if power is None and cat in ('physical', 'special'):
        if not _strong(name):
            weak.append((name, 'B:可変威力ダメージ技で条件検証テストなし'))
    # C. 反動量
    if re.search(r'与えたダメージの1/\d', e) and '受ける' in e and cat in ('physical','special'):
        if not any('反動ダメージ(1/' in l for l in ls):
            weak.append((name, 'C:反動1/N量検証なし'))
    # D. ドレイン量
    if '与えたダメージの' in e and 'HPを回復' in e and cat in ('physical','special'):
        if not any('与ダメ' in l for l in ls):
            weak.append((name, 'D:ドレイン割合検証なし'))
    # E. 相手能力ダウン段階数
    for m in re.finditer(r'相手の\w+を(\d+)段階下げる', e):
        n_dn = int(m.group(1))
        if f'== -{n_dn}' not in blk:
            weak.append((name, f'E:相手能力ダウン段階数等値検証なし(期待==-{n_dn})'))
            break
    # F. 自己能力変化段階数
    for m in re.finditer(r'自分の\w+を(\d+)段階(上げ|下げ)', e):
        n_st = int(m.group(1)); sign = 1 if '上げ' in m.group(2) else -1
        target = sign * n_st
        if f'== {target}' not in blk and f'>= {n_st}' not in blk:
            weak.append((name, f'F:自己能力変化段階数等値検証なし(期待=={target})'))
            break
    # G. HP回復量（変化技）
    if cat == 'status' and '自分のHP' in e and '回復' in e:
        excl = ('ひんしになる' in e or 'たくわえ' in e or name=='のみこむ' or '味方' in e
                or '相手のHP' in e or 'ねがいごと' in e or '相手の攻撃の数値分' in e)
        if not excl:
            if not any('/' in l for l in ls):
                weak.append((name, 'G:HP回復量分数検証なし'))
    # H. 可変威力で方向比較(>,<)のみ＝具体値未検証（テーブル/式の等値検証が必要）
    if (power is None or re.search(r'威力が?\d*倍|威力が(上が|下が|高く|低く)|重いほど|HPが少ない|素早さが', e)) \
            and cat in ('physical', 'special'):
        has_dir = re.search(r'_ep\(|calc_damage\(', blk) and (' > ' in blk or ' < ' in blk)
        # 具体値検証: == <数値>, テーブル一括(_ng), 式一致(== _exp), 2倍(== _x * 2), abs許容
        has_exact = bool(re.search(r'== \d+|_ng\b|== _exp|!= _exp|== _\w+ \* 2|abs\(', blk))
        if has_dir and not has_exact:
            weak.append((name, 'H:可変威力が方向比較のみで具体値未検証'))
    # I. 内部メカニズムフラグの手動セット＝条件成立(トリガー→状態)が未検証
    _MOCK = {'_took_damage_this_turn':'被弾', '._acts_second':'後攻', '.charged':'チャージ',
             '.minimized':'ちいさくなる', '.charging_move':'溜め', '.recharge':'リチャージ',
             '.grounded':'接地', '_destiny_bond_last_turn':'みちづれ連続', '._beak_primed':'くちばし',
             'future_sight_count':'みらいよち予約', 'throat_chop_count':'じごくづき'}
    for flag, label in _MOCK.items():
        if flag in blk:
            # 条件成立(arising)の検証語があるか。無ければ別技で担保される既知ケースを許可
            arise_words = ['成立', '実戦', '付与', 'charging:', 'minimized成立', 'charged成立',
                           '接地化', 'リチャージ付与', '被弾フラグ', 'destiny_bond', '予約成立']
            known_source_ok = flag in ('.minimized', '.charging_move')  # ちいさくなる/2ターン技で別途検証済み
            if not any(w in blk for w in arise_words) and not known_source_ok:
                weak.append((name, f'I:内部フラグ{flag}手動セットで条件成立未検証'))
                break
    # J. 状態異常付与技に「免疫タイプには無効」(negative)テストがあるか
    _ST_IMM = {'まひ':'でんき', 'やけど':'ほのお', 'こおり':'こおり', 'どく':'どく', 'もうどく':'どく'}
    # 特殊トリガー（接触/被弾/能力上昇時/ランダム）は通常経路でないため除外
    _st_special = any(w in e for w in ['接触技を', '行動前', '能力が上がっている', 'いずれか'])
    for _jp, _it in _ST_IMM.items():
        if re.search(rf'{_jp}状態にする|の確率で.*{_jp}', e) and not _st_special:
            if not any(f'{_jp}免疫' in l for l in ls):
                weak.append((name, f'J:{_jp}付与だが免疫({_it}型)negativeテストなし'))
            break

# K. 実装(DEF_DOWNS/STATUS_EFFECTS)にあるが effect_text に記述のない効果（むしくい型バグ）
_BT = open('/Users/shigeki/work/pokenavi/scripts/simulator/battle.py', encoding='utf-8').read()
_eff_map = {n: (e or '') for n, c, p, e in MOVES}
_STAT_JP_K = {'attack':'攻撃','defense':'防御','sp_attack':'特攻','sp_defense':'特防',
              'speed':'素早さ','accuracy':'命中','evasion':'回避'}
# DEF_DOWNS辞書を抽出
_mdd = re.search(r'DEF_DOWNS[^=]*=\s*\{(.*?)\n    \}', _BT, re.DOTALL)
if _mdd:
    for _nm, _stat, _delta, _prob in re.findall(r'"([^"]+)":\s*\("stage_(\w+)",\s*(-?\d+),\s*([\d.]+)\)', _mdd.group(1)):
        _e = _eff_map.get(_nm)
        if _e is None or not _e.strip():
            continue  # DB未登録/effect空はスキップ（別問題）
        _sj = _STAT_JP_K.get(_stat, _stat)
        if int(_delta) < 0 and (_sj not in _e or '下げ' not in _e):
            weak.append((_nm, f'K:実装で相手{_sj}ダウンだがeffect_textに記述なし（誤実装の疑い）'))
# STATUS_EFFECTS辞書を抽出（追加状態異常）
_mse = re.search(r'STATUS_EFFECTS[^=]*=\s*\{(.*?)\n    \}', _BT, re.DOTALL)
if _mse:
    _ST_JP_K = {'paralysis':'まひ','burn':'やけど','freeze':'こおり','poison':'どく',
                'badpoison':'もうどく','sleep':'ねむり','confused':'こんらん'}
    for _nm, _st in re.findall(r'"([^"]+)":\s*\("(\w+)",\s*[\d.]+\)', _mse.group(1)):
        _e = _eff_map.get(_nm)
        if _e is None or not _e.strip():
            continue
        _sj = _ST_JP_K.get(_st, _st)
        if _sj not in _e:
            weak.append((_nm, f'K:実装で{_sj}付与だがeffect_textに記述なし（誤実装の疑い）'))

# K2. その他の効果テーブル：実装にあるがeffect_textに無い効果（過剰実装）の全般検出
_DM = open('/Users/shigeki/work/pokenavi/scripts/simulator/damage.py', encoding='utf-8').read()
def _set_names(src, setname):
    mm = re.search(rf'{setname}\s*=\s*\{{(.*?)\}}', src, re.DOTALL)
    return re.findall(r'"([^"]+)"', mm.group(1)) if mm else []
def _dict_names(src, dictname):
    mm = re.search(rf'{dictname}[^=]*=\s*\{{(.*?)\n    \}}', src, re.DOTALL)
    return re.findall(r'"([^"]+)"\s*:', mm.group(1)) if mm else []
def _check_over(label, names, kw_fn):
    for _nm in names:
        _e = _eff_map.get(_nm)
        if _e is None or not _e.strip():
            continue
        if not kw_fn(_e):
            weak.append((_nm, f'K:実装で{label}だがeffect_textに記述なし（誤実装の疑い）'))
# FLINCH（ひるみ）。prob>0のみ対象（0.0登録は無効化済みなのでスキップ）
_mfl = re.search(r'FLINCH_MOVES[^=]*=\s*\{(.*?)\n    \}', _BT, re.DOTALL)
if _mfl:
    for _nm, _p in re.findall(r'"([^"]+)":\s*([\d.]+)', _mfl.group(1)):
        if float(_p) > 0:
            _e = _eff_map.get(_nm)
            if _e and _e.strip() and ('ひるま' not in _e and '怯ま' not in _e):
                weak.append((_nm, 'K:実装でひるみだがeffect_textに記述なし（誤実装の疑い）'))
_check_over('吸収', _dict_names(_BT, 'DRAIN_RATES'), lambda e: 'HPを回復' in e or '吸収' in e)
_check_over('多段', _set_names(_BT,'MULTI_HIT_2')+_set_names(_BT,'MULTI_HIT_RANDOM_25'), lambda e: '連続' in e or '回攻撃' in e)
_check_over('ちいさくなる2倍', _set_names(_DM,'MINIMIZE_2X'), lambda e: 'ちいさくなる' in e)
_check_over('急所ランク+1', _set_names(_BT,'high_crit_moves'), lambda e: 'きゅうしょ' in e or '急所' in e)
_check_over('リチャージ', _set_names(_BT,'RECHARGE_MOVES'), lambda e: '反動' in e or '動け' in e or '次のターン' in e)
# SELF_EFFECTS（自己能力変化）。空リストの技は効果なしなのでスキップ
_mse2 = re.search(r'SELF_EFFECTS:[^=]*=\s*\{(.*?)\n    \}', _BT, re.DOTALL)
if _mse2:
    for _nm, _body in re.findall(r'"([^"]+)":\s*(\[[^\]]*\])', _mse2.group(1)):
        if _body.strip() == '[]':
            continue
        _e = _eff_map.get(_nm)
        if _e and _e.strip() and '自分' not in _e:
            weak.append((_nm, 'K:実装で自己能力変化だがeffect_textに記述なし（誤実装の疑い）'))

# L. _effective_power 内で「DB威力固定だが条件付きで倍率がかかる」技に具体値テスト必須（やけっぱち型）
#    DB power=NULL の可変威力技は gate B/H が担保。ここは「固定威力＋隠れ条件倍率」を狙う。
_ep_m = re.search(r'def _effective_power\(.*?\n(.*?)\n    return power\n', _DM, re.DOTALL)
_ep_src = _ep_m.group(1) if _ep_m else ''
_db_power = {n: p for n, c, p, e in MOVES}
def _resolve_set_dm(ident):
    mm = re.search(rf'{ident}\s*=\s*\{{(.*?)\}}', _DM, re.DOTALL)
    return re.findall(r'"([^"]+)"', mm.group(1)) if mm else []
_cur_ep = []
_cond_mult = set()
for _line in _ep_src.split('\n'):
    if 'move.name_jp' in _line:
        _eqs = re.findall(r'move\.name_jp == "([^"]+)"', _line)
        _ins = re.search(r'move\.name_jp in \(([^)]+)\)', _line)
        _idm = re.search(r'move\.name_jp in (\w+)', _line)
        if _eqs:
            _cur_ep = _eqs
        elif _ins:
            _cur_ep = re.findall(r'"([^"]+)"', _ins.group(1))
        elif _idm:
            _cur_ep = _resolve_set_dm(_idm.group(1))
    # 条件/状態依存の威力変更（初期化 power = move.power or 0 以外の power 再代入すべて）。
    # 乗算(×N)・除算(÷N)に加え、加算/式（おはかまいり= 50+50*ひんし数 等）も対象にする。
    if re.search(r'^\s*power\s*=', _line) and 'move.power' not in _line:
        _cond_mult.update(_cur_ep)
for _nm in sorted(_cond_mult):
    _p = _db_power.get(_nm)
    if _p is None:
        continue  # NULL威力は gate B/H が担保
    _bk = _blk(_nm)
    # 具体値検証: ==数値 / ==(数値タプル) / テーブル一括 / 式一致 / 2倍(== _x*2) / abs許容 / blkに "* 2" 比較
    if not re.search(r'== \d+|== \(\d|_ng\b|== _exp|!= _exp|== _\w+ \* 2|abs\(|\* 2', _bk):
        weak.append((_nm, 'L:DB威力固定＋条件付き倍率だが具体値テストなし（やけっぱち型）'))

# N. 条件付き(トリガー型)効果に「条件不成立=negative」テストがあるか。
#    仕様「効果A、ただし条件Xを満たすとB」のうちBのpositiveだけ書いてAのnegativeを書き忘れる漏れ
#    （とどめばり型）を検出する。威力可変は gate B/H/L が、状態異常免疫は gate J が担保済みなので、
#    ここは「威力以外のトリガー効果」を対象にする。
_TRIG_MARK = ('倒すと', '倒した', 'きぜつさせると', 'きぜつさせた', '当てると', '受けると',
              '成功すると', '成功した', '持っていない場合', '持っている場合', '持っていれば',
              'しか使えない', '場合にしか', '場合に使える', 'でないと使えない')
_NEG_MARK = ('なし', 'ない', '無し', '無く', '上がらない', '下がらない', '失敗', '不発', '無効',
             '通常', '変わらない', '±0', '== 0', '==0', '治らない', '奪わない', '発動しない')
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e or name in DOUBLE_ONLY or name in _DOUBLE_EXCL:
        continue
    if not any(t in e for t in _TRIG_MARK):
        continue
    _ls_n = _strong(name)
    if not _ls_n:
        continue  # 狙ったテストが無いケースは未分類/SOFT側が拾う
    if not any(any(_n in _l for _n in _NEG_MARK) for _l in _ls_n):
        weak.append((name, 'N:条件付き(トリガー)効果だが条件不成立(negative)テストなし'))

# S. 【一般化】effect_text に条件表現を含む句があれば、分岐の検証痕跡を要求する。
#    マーカー列挙(gate N)では拾えない条件表現も対象にする一般ゲート。
#    分岐検証の痕跡 = 負例マーカー or 2つ以上の本体チェック（＝両分岐を別々に検証している証跡）。
# 「とき/時」は「その時に」等の参照表現を誤検出するため除外。条件性が明確な語のみ採用。
_COND_MARK = ('場合', 'ていれば', 'ていると', 'ている場合', 'しか', '限り', 'でないと', 'でなければ')
_DBL_CLAUSE = ('味方', '2匹', 'それぞれ', '全体', 'ダブル')
_S_STUB = {'まねっこ'}  # 文書化済みstub（REQUIREMENTS制約事項）。実装が無いため分岐テスト対象外。
_SVar = _NEG_MARK + ('_ng', '== _exp', '_ep(', '== (', '半減', '必中', '命中低下', '即攻撃でも',
                     '遅延', '予約', '強制交代', '交代しない', '* 2', '2倍', '1.5倍', 'フォルム',
                     '引き継', '地中', '水中', '後攻', 'じゅうりょく', 'ミスト時', '天候半減')
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e or name in DOUBLE_ONLY or name in _DOUBLE_EXCL or name in _S_STUB:
        continue
    _conds = [c for c in split_clauses(e)
              if any(m in c for m in _COND_MARK) and not any(d in c for d in _DBL_CLAUSE)]
    if not _conds:
        continue
    _ls_s = _strong(name)
    _bk_s = _blk(name)
    _has_branch = (len(_ls_s) >= 2) or any(v in _bk_s for v in _SVar)
    if not _has_branch:
        weak.append((name, f'S:条件句「{_conds[0][:24]}」あるが分岐検証の痕跡なし'))

# O. 「A状態・B状態…のいずれか」型（複数状態のうち1つをランダム付与）で、
#    全状態が実際に発生することを検証しているか。1状態しか見ていない漏れ（フェイタルクロー型）を検出。
_ST_EN = {'どく': 'poison', 'もうどく': 'badpoison', 'まひ': 'paralysis', 'やけど': 'burn',
          'こおり': 'freeze', 'ねむり': 'sleep', 'こんらん': 'confused'}
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    # 「いずれかにする」（複数状態のランダム付与）のみ対象。「いずれかの場合は威力…」（条件）は除外。
    if not e or name in DOUBLE_ONLY or 'いずれかにする' not in e:
        continue
    _states = re.findall(r'(どく|もうどく|まひ|やけど|こおり|ねむり|こんらん)状態', e)
    _states = list(dict.fromkeys(_states))
    if len(_states) < 2:
        continue
    _bk_o = _blk(name)
    _missing = [s for s in _states if _ST_EN[s] not in _bk_o and s not in _bk_o]
    if _missing:
        weak.append((name, f'O:「いずれか」複数状態のうち未検証={_missing}（全状態の発生確認なし）'))

# Q. 2ターン技で「天候で即攻撃」例外があり、かつ「使ったターンに自分の能力上昇」副次効果を持つ技は、
#    溜め時だけでなく即攻撃時にも副次効果が起きることを検証しているか（エレクトロビーム型の片側漏れ）。
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e or name in DOUBLE_ONLY or cat not in ('physical', 'special'):
        continue
    _has_imm = re.search(r'(にほんばれ|あめ|すなあらし|あられ|ゆき)状態の場合は?[^。]*?溜め状態にならず', e)
    _has_boost = re.search(r'使ったターンに自分の[^。]*?\d+段階上げ', e)
    if _has_imm and _has_boost:
        _bk_q = block(name)
        if '即攻撃でも' not in _bk_q:
            weak.append((name, 'Q:天候即攻撃時の副次効果(能力上昇)テストなし（溜め時のみ検証）'))

# V. 列挙マッピング句（「条件A：タイプX、条件B：タイプY…」）で全マッピングを検証しているか。
#    gate O（状態いずれか）の一般化。ウェザーボール型の「天候→タイプ」等、N個の対応を1つしか
#    テストしていない部分被覆を検出する。
_TYPES_V = ('ノーマル', 'ほのお', 'みず', 'でんき', 'くさ', 'こおり', 'かくとう', 'どく', 'じめん',
            'ひこう', 'エスパー', 'むし', 'いわ', 'ゴースト', 'ドラゴン', 'あく', 'はがね', 'フェアリー')
for name, cat, power, effect in MOVES:
    e = (effect or '')
    if not e or name in DOUBLE_ONLY:
        continue
    for _cl in split_clauses(e):
        _rhs = re.findall(r'[：:]\s*(' + '|'.join(_TYPES_V) + r')', _cl)
        if len(_rhs) >= 2:
            _bk_v = block(name)
            _miss = [t for t in _rhs if t not in _bk_v]
            if _miss:
                weak.append((name, f'V:列挙マッピングの未検証タイプ={_miss}（全対応の検証なし）'))
            break

# T. ハザード設置テストが「自分のハザード属性のみ」を厳密判定しているか。
#    全ハザードのOR（… or stealth_rock_set …）混入で別ハザードにより偽成立する漏れ（ねばねばネット型）を検出。
#    ステルスロックは run時確定(_stealth_rock_pending)許容が正当なので対象外。
_HZ_ATTR_T = {'まきびし': 'spikes', 'どくびし': 'toxic_spikes', 'ねばねばネット': 'sticky_web'}
for name, cat, power, effect in MOVES:
    e = (effect or '')
    for _hz_jp, _attr in _HZ_ATTR_T.items():
        if f'相手の場を{_hz_jp}状態' in e:  # 設置方向のみ（除去技「〜状態を解除」は対象外）
            _bk_t = block(name)
            if not _bk_t:
                continue
            if 'stealth_rock_set' in _bk_t or '_stealth_rock_pending' in _bk_t:
                weak.append((name, f'T:{_attr}設置テストにstealth_rock系フラグのOR混入（別ハザードで偽成立の疑い）'))
            elif f'{_attr}[' not in _bk_t:
                weak.append((name, f'T:{_attr}設置だが自身のハザード属性を判定していない'))

# U. 入替(スワップ)技は双方向（自分・相手の両方が入れ替わったこと）を検証しているか。
#    片側のみ検証＝「コピー」でも偽成立する漏れ（ガードスワップ型）を検出。
#    道具入替(トリック/すりかえ)・場所入替(サイドチェンジ)は別系統なので除外。
for name, cat, power, effect in MOVES:
    e = (effect or '')
    if name in DOUBLE_ONLY or '入れ替える' not in e:
        continue
    if any(w in e for w in ('道具', '場所')):
        continue
    _bk_u = block(name)
    if not _bk_u:
        continue
    _pvars = set(re.findall(r'(_\w+)\s*=\s*make_poke\(', _bk_u))
    _two_sided = False
    for _cm in re.finditer(r'check\("[^"]*",\s*(.+)\)\s*$', _bk_u, re.MULTILINE):
        _cond = _cm.group(1)
        _used = {v for v in _pvars if re.search(re.escape(v) + r'\.', _cond)}
        if len(_used) >= 2:
            _two_sided = True
            break
    if not _two_sided:
        weak.append((name, 'U:入替(スワップ)技だが双方向(自分・相手両方)を検証していない（コピーでも偽成立）'))

# R. 特定の複合効果に専用テストがあるか（effect_text句→必須ラベル語）。
#    キングシールドのフォルムチェンジ・バトンタッチの引き継ぎ・天候別回復の全分岐を要求する。
_GATE_R = [
    ('フォルムチェンジ', 'フォルム', 'フォルムチェンジ検証'),
    ('引き継ぐ', '引き継', '引き継ぎ検証'),
]
for name, cat, power, effect in MOVES:
    e = (effect or '').strip()
    if not e or name in DOUBLE_ONLY:
        continue
    _bk_r = block(name)
    for _sub, _kw, _desc in _GATE_R:
        if _sub in e and _kw not in _bk_r:
            weak.append((name, f'R:{_desc}（effect「{_sub}」に対応テストなし）'))
    # 天候別回復（晴れ2/3・他1/4）の全分岐検証
    if '2/3回復' in e and '1/4回復' in e:
        if not ('2/3' in _bk_r and '1/4' in _bk_r):
            weak.append((name, 'R:天候別回復の全分岐(2/3・1/4)テストなし'))

# M. 生成器(generate_move_tests.py)の重複 elif 分岐検出。
#    同じ技名が2つ以上の elif name== / in(...) 条件に現れると、後ろの分岐は
#    到達不能(デッドコード)になり、そのカスタムテストが無言で消える（今回のソーラー回帰）。
_GEN = open('/Users/shigeki/work/pokenavi/scripts/tests/generate_move_tests.py', encoding='utf-8').read()
_branch_names = {}
for _bl in re.findall(r"elif name == '([^']+)':", _GEN):
    _branch_names[_bl] = _branch_names.get(_bl, 0) + 1
for _grp in re.findall(r"elif name in \(([^)]+)\):", _GEN):
    for _bl in re.findall(r"'([^']+)'", _grp):
        _branch_names[_bl] = _branch_names.get(_bl, 0) + 1
for _bl, _cnt in sorted(_branch_names.items()):
    if _cnt > 1:
        weak.append((_bl, f'M:生成器に重複elif分岐が{_cnt}個（後続がデッドコード化しテスト消失）'))

# P. 「失敗/無効」negativeテストが、意図でなくタイプ無効(0倍)で偽成立していないか。
#    ダメージ技で「相手HPが変わらない＝失敗」を主張するテストが、実は相性0倍で常にダメ0
#    になっているだけ、というポルターガイスト型の偽テストを検出する。
_FAIL_LABEL = ('失敗', '不発', '無し', 'なし', '効かない', '通らない', '使えない', '変わらない')
_TYPEIMM_INTENT = ('無効', '免疫', 'タイプ')  # 型免疫を狙ったテスト自体は正当→除外
_TYPES = ('ノーマル','ほのお','みず','でんき','くさ','こおり','かくとう','どく','じめん',
          'ひこう','エスパー','むし','いわ','ゴースト','ドラゴン','あく','はがね','フェアリー')
for name, cat, power, effect in MOVES:
    if cat not in ('physical', 'special'):
        continue
    _mt = _MOVE_TYPE.get(name)
    if not _mt:
        continue
    blk = block(name)  # ボイラープレート除去前の生ブロック（変数定義を含む）
    for _line in blk.split('\n'):
        if 'check(' not in _line or '.hp ==' not in _line:
            continue
        _lm = re.search(r'check\("([^"]*)"', _line)
        if not _lm:
            continue
        _lab = _lm.group(1)
        # 「相手HPが変わらない＝失敗」系の主張か
        if not any(w in _lab for w in _FAIL_LABEL):
            continue
        # 型免疫を狙ったテスト自体は除外
        if any(w in _lab for w in _TYPEIMM_INTENT):
            continue
        # 主張の対象変数（X.hp == Y）を取り、その型を make_poke から逆引き
        _vm = re.search(r'(\w+)\.hp ==', _line)
        if not _vm:
            continue
        _dv = _vm.group(1)
        _def = re.search(rf'{re.escape(_dv)}\s*=\s*make_poke\(([^\n]*?)\)', blk)
        if not _def:
            continue
        _args = _def.group(1)
        _t1m = re.search(r'type1\s*=\s*"([^"]+)"', _args)
        _t2m = re.search(r'type2\s*=\s*"([^"]+)"', _args)
        _t1 = _t1m.group(1) if _t1m else 'ノーマル'  # make_poke既定はノーマル
        _t2 = _t2m.group(1) if _t2m else None
        if _t1 not in _TYPES:
            continue
        try:
            _eff = _gte(_mt, _t1, _t2)
        except Exception:
            continue
        if _eff == 0:
            weak.append((name, f'P:負例「{_lab[:20]}」が相性0倍({_mt}→{_t1}/{_t2})で偽成立の疑い'))
            break

print(f"=== 未分類/未検証の観点: {len(uncovered)}件 ===")
for n, c, why in uncovered:
    print(f"  {n}: 「{c}」 [{why}]")
print(f"\n=== SOFT（副作用発現のみ）: {len(soft)}件 ===")
for n, c in soft:
    print(f"  {n}: 「{c}」")
print(f"\n=== 弱いテスト（多段・可変威力・条件成立で中身が不十分）: {len(weak)}件 ===")
for n, why in weak:
    print(f"  {n}: {why}")
print(f"\n（ダブルバトル専用 {len(DOUBLE_ONLY)}技は対象外）")
