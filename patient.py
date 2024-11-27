
import datetime
import random
patient = ["増山恵治","西間木和尚","岡勝憲","上野孔大","荻野奈央","中村弥生","荒木唯穏","中村清美"]
season = [["暑くなってきたが、","温度変化が激しいが、"],["暑い日が続くが、","厳しい暑さが続くが、"],["寒くなってきたが、","温度変化が激しいが、"],["寒い日が続くが、","厳しい寒さが続くが、"]]
dt = datetime.datetime.now()
month = dt.month
if month in [4,5]:
    season_num = 0
if month in [6,7,8,9]:
    season_num = 1
if month in [10,11]:
    season_num = 2
if month in [12,1,2,3]:
    season_num = 3 
masuyama_keiji = [["表情良好。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。","ご機嫌な様子。"],
                  [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"],
                  ["他利用者の愚痴を話されるが二言程度。","夜間頻尿は相変わらずだがよく眠れている。","グループホームや作業所でも変わりなく過ごされている。","グループホームや作業所でも変わりなく過ごされている。","グループホームや作業所でもトラブルなく過ごされている。"],
                  ["ショパンの曲を一緒に聴きました。","イルマの曲を一緒に聴きました。","リチャードクレイダーマンの曲を一緒に聴きました。","リストの曲を一緒に聴きました。","ラフマニノフの曲を一緒に聴きました。"]
                 ]

nishimaki_kazuhisa = [["表情良好。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。","表情良好。"],
                    [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"],
                      ["グル音良好。排便も良好。","グル音やや亢進気味であるが便の性状に問題なし。","グル音正常で排便に問題なし。","グル音良好。排便も良好。","グル音正常で排便に問題なし。"],
                      ["精神状態に問題ないが、今後も精神状態の変化に配慮し接していく。","精神状態に問題ないが、今後も精神状態の変化に気を付けながら対応する。","精神状態に問題ないが、今後も精神状態の変化に気を付けながら対応する。","精神状態に変わりはないが、今後も変化はないか確認していく。","精神状態に変わりはないが、今後も観察していく。"]
                     ]

oka_katsunori = [["本日入浴介助、髭剃り、創部の処置など介入したが入浴介助に拒否強い。","本日入浴介助、髭剃り、創部の処置など介入したが比較的機嫌がよく機嫌","無表情だが反応に変わりなし。","表情険しいが反応は普段通り。"],
                 ["ご自身で前胸部、陰部、足部までは洗うことができている。その他介入するも頭部のみ昨日洗ったと拒否強く断念。","ご自身で前胸部、陰部、くるぶしまでは自立して洗っている。その他介助しようとすると拒否強い。","ご自身で前胸部、陰部、くるぶしまでは自立して洗っているが、入念に洗っている様子はない。介助に対して拒否強いが説得して介入。"],
                 ["右第一足趾変色続くが範囲は小さくなっている。","変色は継続しているが出血や排膿ない。","排膿軽度あるが赤みはあまりなく炎症は強くない。","腫脹軽度あるが排膿や出血見られない。"],
                 ["来週以降も同様の介入していく予定ではあるが精神状態に注意し、介入していく。","来週以降も精神状態に注意し、介入していく。"]
                ]

ueno_koudai = [["表情良好。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。"],
               ["部屋は散らかっているため部屋の清掃を一緒に行った。","部屋は比較的整理されている。","部屋は自分が訪問する前に急いで綺麗にしたとのこと","模様替えされており、整理ができていないため一緒に片づけを行った。"],
               ["人間関係等でストレスはないとのこと。","","ご機嫌な様子。","楽しそうなご様子。"],
               []
              ]

ogino_nao = [["表情良好。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。"],
             ["心音に変わりはない。","心臓の音に変化は見られない。","心音に変化なく自覚症状もなし。"],
             [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"],
             [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"]
            ]

nakamura_yayoi = [["表情に変わりなし。","表情や機嫌に変わりなし。","無表情だが時折笑顔が見られる。","表情にお変わりなし"],
                  ["冷蔵庫の確認実施。期限切れはない。","冷蔵庫の確認実施。期限切れのものはない。","冷蔵庫の確認実施。期限切れのものは見当たらない。","冷蔵庫の確認実施。期限切れはない。",],                  
                  ["便秘傾向が続いているとのこと。","夜間頻尿による寝不足を訴える。","右手首の疼痛訴えあり。","夜間頻尿による寝不足あり。"],
                  ["次回受診日に上記症状を相談する旨お伝え。","症状が良くならなければ受信時に相談するよう伝えた。","次回受診日に上記症状を相談する旨お伝え。","次回受診日に上記症状を相談する旨お伝え。",],
                  [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"]
                ]

araki_ion = [["表情良好。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。"],
             ["施設や職場でトラブルなし。","機嫌よい。","ご機嫌な様子。","楽しそうなご様子。"],
             ["表情のスケールは9","asd"],
             [f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理は万全とのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調管理には自信があるとのこと。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないとのこと。"]
            ]

nakamura_kiyomi = [["表情に変わりなし。","表情や機嫌に変わりなし。","無表情だが反応に変わりなし。","表情険しいが反応は普段通り。"],
                   ["表情のスケールは9","表情スケールは8","表情スケールは10","表情のスケールは9"],
                   ["職場との切り替えはうまくいっているとのこと。","気持ちの切り替えはうまくいっていないとのこと。","職場で注意されずにうまくやれているとのこと。","仕事は楽しいとのこと。"],
                   [f"{season[season_num][int(random.randint(0, 1))]}体調管理はできている。",f"{season[season_num][int(random.randint(0, 1))]}体調に変わりはないと話される。",f"{season[season_num][int(random.randint(0, 1))]}体調管理はできていますと話される。",f"{season[season_num][int(random.randint(0, 1))]}体調に変化なく良好。",f"{season[season_num][int(random.randint(0, 1))]}特に体調に変わりはないと仰せ。"]
                  ]

patient_data = [masuyama_keiji,nishimaki_kazuhisa,oka_katsunori,ueno_koudai,ogino_nao,nakamura_yayoi,araki_ion,nakamura_kiyomi]