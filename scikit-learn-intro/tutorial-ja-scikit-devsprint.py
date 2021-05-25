# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Scikit-learnチュートリアル
#
# ## 目次
#
# * データ探索
# * scikit-learnを使用した最初のモデル
# * 数値データの操作
# * 数値特徴の前処理
# * 数値変数とカテゴリ変数を一緒に使用
# * Gradient-boosting treeモデル
#
#

# %% [markdown]
#
# このチュートリアルは、MOOCコース「[Machine learning with scikit-learn](https://www.fun-mooc.fr/fr/cours/machine-learning-python-scikit-learn/)」
# の資料に基づいており、Creative Commons Attribution-ShareAlike 4.0ライセンスされています。

# %% [markdown]
# # データ探索
#
# このノートブックでは、機械学習を行う前に必要な手順を説明します。これには以下が含まれます。
#
# * データのロード;
# * 特に、データセット内の変数を確認すると、ほとんどの機械学習ワークフローで
#   異なる前処理が必要な数値変数とカテゴリ変数を区別できます。
# * データセットへの洞察を得るために変数の分布を視覚化します。

# %% [markdown]
# ## 成人の国勢調査データセットの読み込み
#
# [OpenML](http://openml.org/)からダウンロードした1994年の米国国勢調査のデータを使用します。
#
# このデータセットの詳細については、OpenML Webページを参照してください：
# <http://www.openml.org/d/1590>
#
# データセットはCSV（カンマ区切り値）ファイルとして利用でき、pandasを使用して読み取ります。
#
# ```{note}
# [Pandas](https://pandas.pydata.org/)は、1次元および2次元の構造化データを
# 操作するために使用されるPythonライブラリです。pandasを使用したことがない場合は、
# この[チュートリアル](https://pandas.pydata.org/docs/user_guide/10min.html)を
# 参照することをお勧めします。
# ```

# %%
import pandas as pd
adult_census = pd.read_csv("datasets/adult-census.csv")

# %% [markdown]
# このデータの目標は、年齢、雇用、教育、家族情報などの異種データから、
# 人が年間5万人以上を稼いでいるかどうかを予測することです。

# %% [markdown]
# ## データセット内の変数（列）
#
# データはpandasのdataframeに保存されます。dataframeは、
# 2次元で構成される構造化データの一種です。このタイプのデータは、表形式データとも呼ばれます。
#
# 各行はサンプルを表します。
#
# %% [markdown]
# データフレームを調べる簡単な方法は、次の`head`方法で最初の数行を表示することです。

# %%
adult_census.head()

# %% [markdown]
# **class**という名前の列は、ターゲット変数（つまり、予測する変数）です。
# 考えられる2つのクラスは、`<=50K`（低収益）と`>50K`（高収益）です。
# したがって、結果として生じる予測問題はバイナリ分類問題ですが、
# 他の列をモデルの入力変数として使用します。

# %%
target_column = 'class'
adult_census[target_column].value_counts()

# %% [markdown]
# ```{note}
# クラスはわずかに不均衡です。つまり、他のクラスと比較して1つ以上の
# クラスのサンプルが多くなります。クラスの不均衡は実際に頻繁に発生し、
# 予測モデルを構築するときに特別な手法が必要になる場合があります。
#
# たとえば、医療現場で、被験者がまれな病気を発症するかどうかを
# 予測しようとすると、データセットには病気の被験者よりもはるかに多くの
# 健康な被験者が存在します。
# ```

# %% [markdown]
# データセットには、数値データとカテゴリデータの両方が含まれています。
# 数値は、たとえば、連続値を取ります`age`。カテゴリ値は、たとえば、
# 有限数の値を持つことができます`native-country`。

# %%
numerical_columns = [
    'age', 'education-num', 'capital-gain', 'capital-loss',
    'hours-per-week']
categorical_columns = [
    'workclass', 'education', 'marital-status', 'occupation',
    'relationship', 'race', 'sex', 'native-country']
all_columns = numerical_columns + categorical_columns + [
    target_column]

adult_census = adult_census[all_columns]

# %% [markdown]
# データセットで使用可能なサンプル数と列数を確認できます。

# %%
print(f"The dataset contains {adult_census.shape[0]} samples and "
      f"{adult_census.shape[1]} columns")

# %% [markdown]
# 列の1つがターゲットであるため、列の数を数えて1を引くことにより、特徴の数を計算できます。

# %%
print(f"The dataset contains {adult_census.shape[1] - 1} features.")

# %% [markdown]
# ## データの目視検査
# 予測モデルを構築する前に、データを確認することをお勧めします。
#
# * 達成しようとしているタスクは、機械学習なしで解決できるかもしれません。
# * タスクに必要な情報が実際にデータセットに存在することを確認する必要があります。
# * データを検査することは、特性を見つけるための良い方法です。
#   これらは、データ収集中に発生する可能性があり
#   （たとえば、センサーの誤動作や値の欠落）、またはデータが後で処理される方法
#   （たとえば、上限値）から発生する可能性があります。

# %% [markdown]
# データに関するいくつかの洞察を得るために、個々の機能の分布を見てみましょう。
# ヒストグラムをプロットすることから始めることができます。
# これは数値を含むフィーチャに対してのみ機能することに注意してください。

# %%
_ = adult_census.hist(figsize=(20, 14))

# %% [markdown]
# いくつかの変数について、すでにいくつかコメントすることができます。
#
# * `age`: `age > 70`少ない、職した人々が除外されたことを示しています（`hours-per-week > 0`）
# * `education-num`: 10と13にピークがあり、さらに詳しく調べないと、何に対応するのかわかりません。
# * `hours-per-week` ピークは40で、これはデータ収集時の標準的な労働時間である可能性が非常に高いです。
# * ほとんどの値capital-gainとcapital-lossゼロに近いです。

# %% [markdown]
# カテゴリ変数の場合、値の分布を確認できます。

# %%
adult_census['sex'].value_counts()

# %%
adult_census['education'].value_counts()

# %% [markdown]
# 上記のように、`education-num`分布には10と13の周りに2つの明確な
# ピークがあります。それが`education-num`教育の年数であると予想するのは合理的です。
#
# `education`と`education-num`の関係で見てみましょう。
# %%
pd.crosstab(index=adult_census['education'],
            columns=adult_census['education-num'])

# %% [markdown]
# これはそれ`education`を示しており`education-num`、同じ情報を提供します。
# たとえば、`education-num=2`はと同等`education='1st-4th'`です。
# 実際には`education-num`、情報を失うことなく削除できることを意味します。
# 冗長な（または高度に相関する）列があると、機械学習アルゴリズムで問題になる可能性があることに注意してください。

# %% [markdown]
# ```{note}
# 今後のノートブックでは、`education-num`変数を除いて、`education`変数のみを保持します。
# ```

# %% [markdown]
# データを検査する別の方法は`pairplot`です。
# 対角線に沿ったプロットは、各の個々の変数の分布を示しています`class`。
# 非対角線上のプロットは、変数間の交互作用を明らかにすることができます。

# %%
import seaborn as sns

# We will plot a subset of the data to keep the plot readable and make the
# plotting faster
n_samples_to_plot = 5000
columns = ['age', 'education-num', 'hours-per-week']
_ = sns.pairplot(data=adult_census[:n_samples_to_plot], vars=columns,
                 hue=target_column, plot_kws={'alpha': 0.2},
                 height=3, diag_kind='hist', diag_kws={'bins': 30})


# %% [markdown]
# # scikit-learnを使用した最初のモデル
#
# 最初に数値機能のみを使用して、表形式のデータセットで予測モデルを構築する方法を紹介します。
#
# 特に、以下を強調します：
#
# * scikit-learn API: `.fit(X, y)`/`.predict(X)`/`.score(X, y)`;
# * トレインテスト分割を使用してモデルの統計的パフォーマンスを評価する方法。
#
# ## Pandasでデータセットをロードする
#
# 数値データは、機械学習で使用される最も自然なタイプのデータであり、
# （ほぼ）直接予測モデルに入力できます。
# 数値列のみを含む元のデータのサブセットをロードします。

# %%
adult_census = pd.read_csv("datasets/adult-census-numeric.csv")

# %% [markdown]
# このデータフレームの最初のレコードを見てみましょう。

# %%
adult_census.head()

# %% [markdown]
# このCSVファイルには、予測したいターゲット（つまり`"class"`）と
# 予測モデルのトレーニングに使用したいデータ（つまり残りの列）のすべての
# 情報が含まれていることがわかります。
# 最初のステップは、ターゲットとデータを分離しましょう。

# ## データとターゲットを分離する

# %%
target_name = "class"
target = adult_census[target_name]
target

# %%
data = adult_census.drop(columns=[target_name, ])
data.head()

# %% [markdown]
# We can now linger on the variables, also denominated features, that we will
# use to build our predictive model. In addition, we can also check how many
# samples are available in our dataset.

# %%
data.columns

# %%
print(f"The dataset contains {data.shape[0]} samples and "
      f"{data.shape[1]} features")

# %% [markdown]
# ## モデルを適合させて予測を行う
#
# 「K-nearest neighbors」戦略を使用して分類モデルを構築します。
# 新しいサンプルのターゲットを予測するために、kNN法はkトレーニングセット内の最も近いサンプルを考慮に入れ、
# これらのサンプルの過半数のターゲットを予測します。

# ```{caution}
# ここでは、kNN法を使用します。ただし、実際にはほとんど役に立たないことに注意してください。
# 直感的なアルゴリズムであるため、これを使用します。次には、より良いモデルを紹介します。
# ```
#
# この`fit`メソッドは、入力（特徴）とターゲットデータからモデルをトレーニングするために呼び出されます。

# %%
# to display nice model diagram
from sklearn import set_config
set_config(display='diagram')

# %%
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(data, target)

# %% [markdown]
# 学習は次のように表すことができます。
#
# ![Predictor fit diagram](figures/api_diagram-predictor.fit.svg)
#
# この`fit`は、（i）学習アルゴリズムと（ii）いくつかのモデル状態の2つの要素で構成されています。
# 学習アルゴリズムは、トレーニングデータとトレーニングターゲットを入力として受け取り、
# モデルの状態を設定します。これらのモデルの状態は、後でデータを予測（分類と回帰の場合）または変換
# （トランスフォーマーの場合）するために使用されます。
#
# 学習アルゴリズムとモデル状態のタイプはどちらも、モデルのタイプごとに固有です。

# %% [markdown]
# ```{note}
# ここと後で、名前`data`と`target`を明示的に使用します。
# scikit-learnドキュメントで`data`は`X`、`target`は`y`を呼ばれています。
# ```

# %% [markdown]
# モデルを使用して、同じデータセットを使用していくつかの予測を行いましょう。

# %%
target_predicted = model.predict(data)

# %% [markdown]
# 予測メカニズムは次のように説明できます。
#
# ![Predictor predict diagram](figures/api_diagram-predictor.predict.svg)
#
# 予測するために、モデルは、モデルの状態とともに入力データを使用する予測関数を使用します。
# 予測関数はモデルのタイプごとに固有です。

# %% [markdown]
#
# 計算された予測を見てみましょう。簡単にするために、最初に予測された5つのターゲットを見ていきます。

# %%
target_predicted[:5]

# %% [markdown]
# 実際、これらの予測を実際のデータと比較することができます...

# %%
target[:5]

# %% [markdown]
# ...そして、予測が実際の目標と一致するかどうかを確認することもできます。

# %%
target[:5] == target_predicted[:5]

# %%
print(f"Number of correct prediction: "
      f"{(target[:5] == target_predicted[:5]).sum()} / 5")

# %% [markdown]
# ここでは、最初のサンプルを予測するときにモデルが誤りを犯していることがわかります。
#
# より良い評価を得るために、平均成功率を計算することができます。

# %%
(target == target_predicted).mean()

# %% [markdown]
# しかし、この評価は信頼できるのでしょうか、それとも真実であるには良すぎるのでしょうか。
#
# ## トレインテストデータの分割
#
# モデルのトレーニング時にデータのサブセットを除外し、後でモデルの評価に使用することで、
# 正しい評価を簡単に行うことができます。モデルの適合に使用されるデータはトレーニングデータと呼ばれ、
# モデルの評価に使用されるデータはテストデータと呼ばれます。
#
# 元のデータセットから実際に除外された、より多くのデータをロードできます。

# %%
adult_census_test = pd.read_csv('datasets/adult-census-numeric-test.csv')

# %%
target_test = adult_census_test[target_name]
data_test = adult_census_test.drop(columns=[target_name, ])

# %% [markdown]
# この新しいセットで利用可能な機能とサンプルの数を確認できます。

# %%
print(f"The testing dataset contains {data_test.shape[0]} samples and "
      f"{data_test.shape[1]} features")

# %% [markdown]
#
# 予測を計算して平均成功率を手動で計算する代わりに、
# `score`を使用できます。分類の場合、このメソッドはパフォーマンスメトリックを返します。

# %%
accuracy = model.score(data_test, target_test)
model_name = model.__class__.__name__

print(f"The test accuracy using a {model_name} is "
      f"{accuracy:.3f}")

# %% [markdown]
# `score`メソッドが呼び出されたときに、基になるメカニズムを確認しましょう。
#
# ![Predictor score diagram](figures/api_diagram-predictor.score.svg)
#
# スコアを計算するために、予測子は最初に（`predict`を使用して）予測を計算し、
# 次にスコアリング関数を使用して真のターゲット`y`と予測を比較します。最後に、スコアが返されます。






# %% [markdown]
# # 数値データの操作
#
# 先にいくつかのデータでkNNモデルをトレーニングしましたが、実際のデータはより複雑です：
# これから
#
# * 異種データセット内の数値データを特定する。
# * 数値データに対応する列のサブセットを選択する。
# * scikit-learnヘルパーを使用してデータをtrain-testセットに分割します。
# * より複雑なscikit-learnモデルのトレーニングと評価。
#

# %%
adult_census = pd.read_csv("datasets/adult-census.csv")
adult_census = adult_census.drop(columns="education-num")
adult_census.head()

# %% [markdown]
# 次のステップでは、ターゲットをデータから分離します。

# %%
data, target = adult_census.drop(columns="class"), adult_census["class"]

# %%
data.head()

# %%
target

# %% [markdown]
#
# ## 数値データを特定する
#
# ```{caution}
# 数値データは数字で表されますが、数字は必ずしも数値データを表すとは限りません。
# カテゴリはすでに数字でエンコードされている可能性があるため、これらの機能を識別する必要があります。
# ```
#
# データセット内の各列のデータ型を確認できます。

# %%
data.dtypes.unique()


# %% [markdown]
# 数値データを含む列を選択して、その内容を確認できます。

# %%
numerical_columns = ["age", "capital-gain", "capital-loss", "hours-per-week"]
data[numerical_columns].head()

# %% [markdown]
# `age`を確認しましょう。

# %%
data["age"].describe()

# %% [markdown]
# 年齢は17歳から90歳の間で変化することがわかります。
#
# ここで、数値列のサブセットを新しいデータフレームに格納します。

# %%
data_numeric = data[numerical_columns]

# %% [markdown]
# ## トレインテストはデータセットを分割
#
# 前回トレーニングデータセットとテストデータセットの2つの別々のデータセットをロードしました。
# ただし、2つの異なるファイルに別々のデータセットがあることは珍しいことです。
# ほとんどの場合、メモリにロードされた後に分割する必要があるすべてのデータを含む単一のファイルがあります。
#
# Scikit-learnは`sklearn.model_selection.train_test_split`を用意しています。
# これでデータセットを2つのサブセットに自動的に分割できます。

# %%
from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    data_numeric, target, random_state=42, test_size=0.25)


# %% [markdown]
# `train_test_split`を呼び出すときに、サンプルの25％をテストセットに入れ、
# 残りのサンプル（75％）をトレーニングセットで使用を指定しました。

# %%
print(f"Number of samples in testing: {data_test.shape[0]} => "
      f"{data_test.shape[0] / data_numeric.shape[0] * 100:.1f}% of the"
      f" original set")

# %%
print(f"Number of samples in training: {data_train.shape[0]} => "
      f"{data_train.shape[0] / data_numeric.shape[0] * 100:.1f}% of the"
      f" original set")

# %% [markdown]
# ここで、線形モデルファミリに属する​​、ロジスティック回帰モデルを使用します。

# %%
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# %% [markdown]
# モデルが作成されたので、kNNモデルの使用とまったく同じ方法でモデルを使用できます。
# 特に、`fit`を使用して、トレーニングデータとラベルを使用してモデルをトレーニングできます。

# %%
model.fit(data_train, target_train)

# %% [markdown]
# `score`を使用して、テストセットのモデル統計パフォーマンスを確認できます。

# %%
accuracy = model.score(data_test, target_test)
print(f"Accuracy of logistic regression: {accuracy:.3f}")

# %% [markdown]
# # 数値特徴の前処理
#
# 下記の新しい技術を紹介します：
#
# * 前処理の例、つまり**数値変数のスケーリング**
# * scikit-learnの**パイプライン**を使用して前処理とモデルトレーニングを連鎖
# * **相互検証 cross validation**を介してモデルの統計的パフォーマンスを評価
#

# %%
adult_census = pd.read_csv("datasets/adult-census.csv")
target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=target_name)
numerical_columns = [
    "age", "capital-gain", "capital-loss", "hours-per-week"]
data_numeric = data[numerical_columns]
data_train, data_test, target_train, target_test = train_test_split(
    data_numeric, target, random_state=42)

# %% [markdown]
# ## 前処理によるモデルフィッティング
#
# scikit-learnのさまざまな前処理アルゴリズムにより、
# モデルをトレーニングする前に入力データを変換できます。
# この例では、データを標準化してから、その新しいバージョンのデータセットで
# 新しいロジスティック回帰モデルをトレーニングします。
#
# トレーニングデータに関するいくつかの統計を見ましょう。

# %%
data_train.describe()

# %% [markdown]
# データがさまざまな範囲にまたがっていることがわかります。一部のアルゴリズムは、
# 特徴の分布に関していくつかの仮定を行い、通常、特徴を正規化することは、これらの仮定に対処するのに役立ちます。
#
# ```{tip}
# スケーリングする理由：
#
# * サンプルのペア間の距離に依存するモデル、たとえばkNN法は、各特徴が距離計算にほぼ等しく寄与するように、
#   正規化された特徴でトレーニングする必要があります。
#
# * ロジスティック回帰などの多くのモデルは、（勾配降下法に基づく）数値ソルバーを使用して
#   最適なパラメーターを見つけます。このソルバーは、フィーチャがスケーリングされると、より速く収束します。
# ```
#
# `StandardScaler`と呼ばれるscikit-learnトランスフォーマーを使用して正規化をします。
# このトランスフォーマーは、各特徴を個別にシフトおよびスケーリングして、すべてが0の平均および
# 1の標準偏差を持つようにします。

# まず、`fit`でデータからスケーリングを学習させます。

# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(data_train)

# %% [markdown]
#
# ![Transformer fit diagram](figures/api_diagram-transformer.fit.svg)
#
# この場合、アルゴリズムは各特徴の平均と標準偏差を計算し、それらをいくつかのNumPyのarrayに保存します。
#
# 計算された平均と標準偏差を調べます：

# %%
scaler.mean_

# %%
scaler.scale_

# %% [markdown]
# `fit`を使用してから、`transform`でデータ変換を実行できます。

# %%
data_train_scaled = scaler.transform(data_train)
data_train_scaled

# %% [markdown]
# ![Transformer transform diagram](figures/api_diagram-transformer.transform.svg)
#
# %% [markdown]
# `fit`と`transform｀を同時に行うため、`fit_transform`を使えます：
#
# ![Transformer fit_transform diagram](figures/api_diagram-transformer.fit_transform.svg)

# %%
data_train_scaled = scaler.fit_transform(data_train)
data_train_scaled

# %%
data_train_scaled = pd.DataFrame(data_train_scaled,
                                 columns=data_train.columns)
data_train_scaled.describe()

# %% [markdown]
# 上の関数の順次操作を簡単にscikit-learnの`Pipeline`で合わせます。

# %%
import time
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), LogisticRegression())
model

# %%
model.named_steps

# %% [markdown]
# この予測パイプラインは、同じメソッドを提供しています：`fit`、`predict`、`score`など。


# %%
start = time.time()
model.fit(data_train, target_train)
elapsed_time = time.time() - start

# %% [markdown]
# パイプラインの内部メカニズムを表します：
#
# ![pipeline fit diagram](figures/api_diagram-pipeline.fit.svg)
#
# テストセットを指定してターゲットを予測するには、`predict`を使用します。

# %%
predicted_target = model.predict(data_test)
predicted_target[:5]

# %% [markdown]
#
# ![pipeline predict diagram](figures/api_diagram-pipeline.predict.svg)
#
# `model.score`で予測パイプラインのスコアを確認できます：

# %%
model_name = model.__class__.__name__
score = model.score(data_test, target_test)
print(f"The accuracy using a {model_name} is {score:.3f} "
      f"with a fitting time of {elapsed_time:.3f} seconds "
      f"in {model[-1].n_iter_[0]} iterations")

# %% [markdown]
# この予測モデルを、特徴をスケーリングしなかった以前の予測モデルと比較しましょう：

# %%
model = LogisticRegression()
start = time.time()
model.fit(data_train, target_train)
elapsed_time = time.time() - start

# %%
model_name = model.__class__.__name__
score = model.score(data_test, target_test)
print(f"The accuracy using a {model_name} is {score:.3f} "
      f"with a fitting time of {elapsed_time:.3f} seconds "
      f"in {model.n_iter_[0]} iterations")

# %% [markdown]
# ロジスティック回帰をトレーニングする前にデータをスケーリングすることは、
# 計算パフォーマンスの観点から有益であることがわかります。
# 実際、反復回数とトレーニング時間は減少しました。
# 両方のモデルが収束したため、統計的パフォーマンスは変化しませんでした。

# %% [markdown]
# ## 交差検定でのモデル評価
#
# 前の例では、元のデータをトレーニングセットとテストセットに分割しました。
# この戦略にはいくつかの問題があります。データ量が少ない設定では、
# トレーニングまたはテストに使用されるサブセットが少なくなります。
# その上、単一の分割は、得られた結果の信頼性に関する情報を提供しません。
#
# 代わりに、相互検証「cross validation」を使用できます。
# 相互検証は、トレーニングセットとテストセットが毎回異なるように手順を繰り返すことで構成されます。
# 統計的パフォーマンスメトリックは、繰り返しごとに収集され、集計されます。
# その結果、モデルの統計的パフォーマンスの変動性の推定値を取得できます。

# いくつかの相互検証戦略があり、それぞれが`fit`と`score`手順を定義します。
# ここでは、K-foldを使用します。データセット全体がパーティションにされます。
# `fit`と`score`をK回繰り返され、各繰り返しで k-1 パーティションがモデルと適合させるために
# 使用されています。残ってるパーティションはテストのために使用されます。
#
# ![Cross-validation diagram](figures/cross_validation_diagram.png)
#
# 交差検定分割ごとに、手順はすべての赤いサンプルでモデルをトレーニングし、
# 青いサンプルでモデルのスコアを評価します。したがって、交差検定は、
# 1つではなく複数のモデルをトレーニングする必要があるため、計算量が多くなります。
#
# 分割戦略を定義`cross_validate`するパラメーター`cv`を取ります。

# %%
# %%time
from sklearn.model_selection import cross_validate

model = make_pipeline(StandardScaler(), LogisticRegression())
cv_result = cross_validate(model, data_numeric, target, cv=5)
cv_result

# %% [markdown]
# `cross_validate`の出力はディクショナリであり、デフォルトで3つのエントリが含まれています。
# （i）各フォールドのトレーニングデータでモデルをトレーニングする時間、
# （ii）各フォールドのテストデータでモデルを使用して予測する時間、
# （iii）各フォールドのテストデータのデフォルトスコア。
#
# `cv_result`からテストスコアを抽出し、平均精度とフォールド間の精度の変動を計算してみましょう。

# %%
scores = cv_result["test_score"]
print("The mean cross-validation accuracy is: "
      f"{scores.mean():.3f} +/- {scores.std():.3f}")



# %% [markdown]
# # 数値変数とカテゴリ変数を一緒に使用
#

# %%
adult_census = pd.read_csv("datasets/adult-census.csv")
adult_census = adult_census.drop(columns="education-num")

target_name = "class"
target = adult_census[target_name]

data = adult_census.drop(columns=[target_name])

# %% [markdown]
# ## データ型に基づく選択
#

# %%
from sklearn.compose import make_column_selector as selector

numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

numerical_columns = numerical_columns_selector(data)
categorical_columns = categorical_columns_selector(data)

# %% [markdown]
# ## 特定のプロセッサに列をディスパッチ
#
# データの性質（つまり、数値またはカテゴリ）に応じてデータを異なる方法で処理する必要があります。
#
# Scikit-learnは、`ColumnTransformer`という特定の列を特定の
# トランスフォーマーに送信するクラスを提供します。
# 
# まず、データ型に応じて列を定義します：
#
# * **one-hot encoding**は、カテゴリ列に適用されます。
#   また、`handle_unknown="ignore"`でまれなカテゴリによる潜在的な問題を解決するために使用します。
# * **数値スケーリング**は、数値列に適用されます。
#

# %%
from sklearn.preprocessing import OneHotEncoder, StandardScaler

categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")
numerical_preprocessor = StandardScaler()

# %% [markdown]
# トランスフォーマーを作成し、これらの各プリプロセッサーをそれぞれの列に関連付けます。

# %%
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('one-hot-encoder', categorical_preprocessor, categorical_columns),
    ('standard-scaler', numerical_preprocessor, numerical_columns)])

# %% [markdown]
#
# ![columntransformer diagram](figures/api_diagram-columntransformer.svg)
#
# 重要なことは、`ColumnTransformer`は、他のscikit-learnトランスフォーマーと同じです。
# 特に、`Pipeline`と合わせます。

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(preprocessor, LogisticRegression(max_iter=500))

# %%
model

# %% [markdown]
#
# このモデルは以前のモデルよりも複雑ですが、それでも同じAPI
# （ユーザーが呼び出すことができる同じメソッドのセット）に従います。
#
# - `fit`は、データを前処理してから、前処理されたデータの分類子をトレーニングする
# - `predict`は、新しいデータを予測する
# - `score`は、テストデータを予測し、予測を予想されるテストラベルと比較して、精度を計算する

# %%
data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=42)

# %% [markdown]
#
# トレインセットでモデルをトレーニングします：

# %%
_ = model.fit(data_train, target_train)

# %% [markdown]
# 例として、テストセットの最初の5つのサンプルを予測します。

# %%
data_test.head()

# %%
model.predict(data_test)[:5]

# %%
target_test[:5]

# %% [markdown]
# テストセット全体の精度スコアを計算してみましょう。

# %%
model.score(data_test, target_test)

# %% [markdown]
# ##　交差検定でのモデルの評価

# %%
from sklearn.model_selection import cross_validate

cv_results = cross_validate(model, data, target, cv=5)
cv_results

# %%
scores = cv_results["test_score"]
print("The mean cross-validation accuracy is: "
      f"{scores.mean():.3f} +/- {scores.std():.3f}")

# %% [markdown]
# 複合モデルは、数値変数とカテゴリ変数を分離して使用した2つのモデルよりも高い予測精度を備えています。

# %% [markdown]
# # Gradient-boosting treeモデル
#
# 線形モデルは、通常、トレーニングが早くて、展開が小さく、予測が速く、適切なベースラインが得られるため、優れています。
#
# ただし、「ensemble of decision trees」などのより複雑なモデルがより高い予測
# パフォーマンスになることを確認すると役立ちます。
# ここで**gradient-boosting trees*モデルを使用して、その統計的パフォーマンスを評価します。
#
# ツリーベースのモデルの場合、数値変数とカテゴリ変数の処理は線形モデルの場合よりも簡単です。
# * 数値を**スケーリングする必要はありません**
# * カテゴリ変数に**序数エンコーディングは十分**です。
#

# %%
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import OrdinalEncoder

categorical_preprocessor = OrdinalEncoder(handle_unknown="use_encoded_value",
                                          unknown_value=-1)

preprocessor = ColumnTransformer([
    ('categorical', categorical_preprocessor, categorical_columns)],
    remainder="passthrough")

model = make_pipeline(preprocessor, HistGradientBoostingClassifier())

# %% [markdown]
# モデルを作成したので、統計的パフォーマンスを確認します：

# %%
# %%time
_ = model.fit(data_train, target_train)

# %%
model.score(data_test, target_test)

# %% [markdown]
# gradient-boostモデルを使用すると、精度が大幅に向上することがわかります。
# これは、データセットに多数のサンプルがあり、数値変数とカテゴリ変数が混在する有益な特徴の数が限られている
# （たとえば、1000未満）場合によく見られます。
#
# これは、Gradient Boosted Machinesが表形式のデータを処理するため人気です。
