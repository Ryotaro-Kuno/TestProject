import pickle
import sys #コマンドライン引数を使うための
import math

args = sys.argv #変数args[]にはコマンドラインに入力された値が順番に入る
#args[1]:Start,args[2]:Goal(0~31)、ただこれはstr型なのであとで変換する

with open('res/pathdata/opu.pickle', 'rb') as f:
    mapper = pickle.load(f) #距離のデータが入っているファイルを参照

nodes = mapper.default_targets #mapperのなかのdefault_targets(各チェックポイントの座標)を読み込んでいる
start = nodes[int(args[1])] #今ここでエラーが出ている→str型からint型へ変換しないといけない,解決済み
goal = nodes[int(args[2])]
e_path = mapper.paths #pathsデータを移してきた
#print(e_path[forsearch][0]) #確認用出力
#print(len(nodes)) #確認用、nodesの長さは32(チェックポイントの数)

def find_near_points(s, g): #実際に見つけるメソッド(返り値：近い点を記録したリストnear_objects)
    forsearch = (start, goal) #2重tuple
    path_use = e_path[forsearch] #今回選ばれたチェックポイント間の経路
    n_o = [] #近い点を記録するリストnear_objectの略
    for i in range(len(path_use[0])): #座標上で1マスずつ進んでいる
        for j in range(len(nodes)):
            a = list(path_use[0][i]) #計算する2点を別のリストへ
            b = list(nodes[j])
            dis = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) #2点間の距離を計算
            if dis < 100:
                n_o.append(nodes[j]) #near_objectに追加
    n_o = list(dict.fromkeys(n_o)) #重複を削除
    return n_o

near_objects = find_near_points(start, goal)
print("Start :",start)
print("Goal :",goal)
print("Near point :",near_objects) #出力       

'''
def finding(a): #近い点を探すメソッド
    count = 0 #見つかった近い点を数える変数
    for i in e_path[a]: #座標上で1マスずつ進んでいる
        for j in len(nodes): #チェックポイントを探索
            dis = 1000000 #とても大きい数
            if nodes[j] != start and nodes[j] != end: #スタートとエンドは対象の点から外す
                dis = np.linalg.norm(e_path[a][i] - nodes[j]) #Numpyを用いて2点間の距離を計算
            if dis < 50: #取り敢えず距離50以下に設定
                count = count + 1
                print("object",count,nodes[j]) #出力
    if count == 0:
        print("No point was found.")
'''


'''
x = 0
print("start :",start,"goal :",goal)
for i in e_path: #持ってくる部分
    if start == distance_of[i][1]: #スタートが一致している
        if start == distance_of[i][2]: #ゴールが一致している
            x = i #何番目のデータか(distance_ofとe_pathは点の並び方が同じであるため)
            finding(x)
'''

'''
nodes_to_index:Dict[Node, int] = {}
for i, node in enumerate(nodes):
    nodes_to_index[node] = i + 1
'''