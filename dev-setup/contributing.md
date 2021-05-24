# 開発設定

（このドキュメントはscikit-learnの「[Contribute](https://scikit-learn.org/stable/developers/contributing.html)」
ガイドの部分的な翻訳です。）

作業の重複を避けるために、[issue tracker](https://github.com/scikit-learn/scikit-learn/issues)
と[PRリスト](https://github.com/scikit-learn/scikit-learn/pulls)を検索することを強くお勧めします。
重複した作業について疑問がある場合、または重要な機能に取り組みたい場合は、
最初に[issue tracker](https://github.com/scikit-learn/scikit/issues)で課題を開いて、
コア開発者からフィードバックを得ることが推奨されます。

取り組むべきissueを見つける簡単な方法の1つは、検索に「help wanted」ラベルを適用することです。
これは、これまでに請求されていないすべてのissueを一覧表示します。自分でissueを申し立てるには、
CIが自動的にissueを割り当てるように、`take`とコメントしてください。


## コントリビュートする方法

scikit-learnにコントリビュートするための好ましい方法は、
GitHubで[メインリポジトリ](https://github.com/scikit-learn/scikit-learn/)をフォークしてから、
「Pull Request」（PR）を送信することです。

最初のいくつかのステップでは、scikit-learnをローカルにインストールする方法と、gitリポジトリを設定する方法について説明します。

1.  まだアカウントを持っていない場合は、GitHubで[アカウントを作成](https://github.com/join)します。

2.  [プロジェクトのリポジトリ](https://github.com/scikit-learn/scikit-learn)をフォークします：
    ページの上部にある[Fork]ボタンをクリックします。これにより、GitHubユーザーアカウントにコードのコピーが作成されます。
    リポジトリをフォークする方法の詳細については、[このガイド](https://help.github.com/articles/fork-a-repo/)を参照してください。

3.  scikit-learnリポジトリのフォークをGitHubアカウントからローカルディスクにクローンします。

    ```
    git clone <git@github.com>:YourLogin/scikit-learn.git # 接続が遅かったら、--depth 1を追加する
    cd scikit-learn
    ```

4.  開発の依存関係をインストール:

    ```
    pip install cython pytest pytest-cov flake8 mypy
    ```

    追加NP:ゼロからのインストールの場合は`wheel`（と`numpy`と`scipy`？）も必要です。

5.  編集可能モードでscikit-learnをインストール:

    ```
    pip install --no-build-isolation --editable .
    ```

    scikit-learnのビルドでエラーが発生した場合は、[Building from source](https://scikit-learn.org/stable/developers/advanced_installation.html#install-bleeding-edge)セクションを参照してください。

6.  `upstream`リモートを追加します。これにより、メインのscikit-learnリポジトリへの参照が保存されます。
    これを使用して、リポジトリを最新の変更と同期させることができます。

    ```
    git remote add upstream https://github.com/scikit-learn/scikit-learn.git
    ```

これで、scikit-learnが正常にインストールされ、gitリポジトリが適切に構成されているはずです。
次のステップでは、コードを変更してPRを送信するプロセスについて説明します。

7.  `main`ブランチを `upstream/main`ブランチと同期します。詳細については、[GitHub Docs](https://docs.github.com/ja/github/collaborating-with-issues-and-pull-requests/working-with-forks/syncing-a-fork)をご覧ください。

    ```
    git checkout main
    git fetch upstream
    git merge upstream/main
    ```

8.  開発の変更を保持するフィーチャーブランチを作成して、

    ```
    git checkout -b my_feature
    ```

    変更を加え始めます。常にフィーチャーブランチを使用してください。
    `main`ブランチで作業しないことをお勧めします！

9.  (**オプション**)[pre-commit](https://pre-commit.com/#install)をインストールして、
    各コミットの前にコードスタイルチェックを実行します：
    
    ```
    pip install pre-commit
    pre-commit install
    ```

    事前コミットチェックを無効にしたい場合は、`git commit -n`を使用します。
    

10. Gitを使用してバージョン管理を行い、フィーチャーブランチでフィーチャーを開発します。
    編集が完了したら、`git add`を使用して変更されたファイルを追加してから`git commit`を使用します。

    ```
    git add modified_files
    git commit
    ```

    これにより、Gitでの変更が記録され、次に変更コミットをGitHubアカウントにプッシュします：

    ```
    git push -u origin my_feature
    ```

11.  ここの[アドバイス](https://help.github.com/articles/creating-a-pull-request-from-a-fork)の指示に従って、
    フォークからプルリクエストPRを作成します。これにより、コミッターにメールが送信されます。
    より幅広く周知するためにメーリングリストへメールすることも検討してください。
    

Cythonモジュールを変更する場合は、変更後、テストする前に再コンパイルする必要があります：

```
pip install --no-build-isolation -e .
```


`--no-build-isolation`フラグを使用して、変更したファイルのみを毎回プロジェクト全体でコンパイルしないようにします。

定期的にローカルフィーチャーブランチをメインのscikit-learnリポジトリの最新の変更と同期させることを勧めます：

```
git fetch upstream
git merge upstream/main
```

その後、コンフリクトを解決する必要があるかもしれません。
[コマンドラインを使用したマージのコンフリクトの解決に関連するGitドキュメント](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)を参照できます。


### プルリクエストのチェックリスト

PRをマージする前に、2人のコア開発者による承認が必要です。投稿が完了し、
詳細なレビューを受ける必要がある場合は、プルリクエストのタイトルの前に`[MRG]`を付けてください。
不完全な投稿（完全なレビューを受け取る前にさらに作業を行うことが予想される場合）は、
タイトルに `[WIP]`（進行中の作業を示すため）を付け、成熟したら `[MRG]`に変更する必要があります。
`WIP`は、重複した作業を無効にするために何かに取り組んでいることを示したり、
フィーチャーやAPIの広範なレビューを要求したり、共同作業者を探したりする場合に役立ちます。
`WIP`は、PRの説明に[タスクリスト](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
を含めることで恩恵を受けることがよくあります。

レビュープロセスを容易にするために、PRを`[MRG]`としてマークする前に、
投稿が次のルールに準拠することをお勧めします。 **太字**のものは特に重要です：

1.  **プルリクエストに役立つタイトル（コントリビューションの要約）を付けます。** 
    このタイトルは、マージされるとコミットメッセージになることが多いため、要約する必要があります。
    場合によっては、`Fix <ISSUE TITLE>`で十分ですが、`Fix ＃<ISSUE NUMBER>`は決して良いタイトルではありません。

2.  **コードがテストに合格していることを確認してください。** テスト全体を `pytest`で実行できますが、
    時間がかかるため、通常はお勧めしません。多くの場合、変更に関連するテストのみを実行するだけで十分です。
    たとえば、`sklearn/linear_model/_logistic.py`で何かを変更した場合、通常は次のコマンドを実行するだけで十分です。
    
    
    -   `pytest sklearn/linear_model/logistic.py` doctestの例が正しいことを確認
    -   `pytest sklearn/linear_model/tests/test_logistic.py`
        あるファイルに固有のすべてのテストを実行
    -   `pytest sklearn/linear_model`
        [`linear_model`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)
        モジュール全体のテストを実行
    -   `pytest doc/modules/linear_model.rst`
        ユーザーガイドの例が正しいことを確認
    -   `pytest sklearn/tests/test_common.py -k LogisticRegression`
        あるエスティメータ（例：`LogisticRegression`）の更新した場合は、それに対してるテストを実行

    他に失敗したテストがあるかもしれませんが、それらはCIによってキャッチされるので、
    テスト全体をローカルで実行する必要はありません。`pytest`を効率的に使用するための
    ガイドラインについては、[Useful pytest aliases and flags](https://scikit-learn.org/stable/developers/tips.html#pytest-tips)を参照してください。
    
3.  **コードが適切にコメント化および文書化されていることを確認してください。** そして**文書が適切にレンダリングされていることを確認してください。** ドキュメントを作成するには、
    [Documentation](https://scikit-learn.org/stable/developers/contributing.html#contribute-documentation)
    ガイドラインを参照してください。

4.  **拡張機能が受け入れられるにはテストが必要です。** バグ修正または新フィーチャーは、
    [非回帰テスト](https://ja.wikipedia.org/wiki/%E5%9B%9E%E5%B8%B0%E3%83%86%E3%82%B9%E3%83%88)
    で提供する必要があります。これらのテストは、修正またはフィーチャーの正しい動作を検証します。
    このようにして、コードベースのさらなる変更が許可され、目的の動作と一致します。
    バグ修正の場合、PR時に、`main`ブランチのコードベースで非回帰テストが失敗し、
    PRコードに合格する必要があります。
    
    
5.  **PRがPEP8違反を追加しないことを確認してください。** 変更したコードを確認するには、
    次のコマンドを実行するか（`upstream`リモートを設定の手続きは上記述べています）、
    ```
    git diff upstream/main -u -- "*.py" | flake8 --diff
    ```

    または`makeflake8-diff`を実行します。これはUnix系システムで動作します。
    
    
6.  [coding-guidelines](https://scikit-learn.org/stable/developers/develop.html#coding-guidelines)に従います。

7.  該当する場合は、`sklearn.utils`サブモジュールの検証ツールとスクリプトを使用します。
    開発者が利用できるユーティリティルーチンのリストは、[developers-utils](https://scikit-learn.org/stable/developers/utilities.html#developers-utils)ページにあります。

8.  多くの場合、プルリクエストは1つ以上の他のissue（またはプルリクエスト）を解決します。
    プルリクエストをマージすることで他のissue/PRを閉じる場合は、[キーワードを使用してそれらへのリンクを作成してください](https://github.com/blog/1506-closeing-issues-via-pull-requests/)
    （例： `Fixes ＃1234`; それぞれの前にキーワードが付いている限り、複数のissue/PRが可能）。
    マージすると、これらのissue/PRはGitHubによって自動的に閉じられます。
    プルリクエストが単に他のissue/PRに関連している場合は、キーワードを使用せずにそれらへの
    リンクを作成します（例：`See also ＃1234`）。
    
9.  PRは、パフォーマンスと効率のベンチマーク
    （[パフォーマンスの監視](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances)を参照）
    または使用例を通じて、変更を実証する必要があります。
    例では、ライブラリの機能と複雑さもユーザーに示しています。
    [examples/](https://github.com/scikit-learn/scikit-learn/tree/main/examples)
    ディレクトリにある他の例を参照してください。
    例では、新しい機能が実際に役立つ理由を示し、可能であれば、
    scikit-learnで利用可能な他の方法と比較する必要があります。
    

10.  新フィーチャーには、メンテナンスのオーバーヘッドがあります。
    PR作成者は、少なくとも最初は提出するコードの保守に参加することが期待されます。
    新しいフィーチャーは、ユーザーガイドの説明ドキュメントと小さなコードスニペットで説明される必要があります。
    必要に応じて、可能であればPDFリンクを使用して、文献に参照を追加してください。

11.  ユーザーガイドには、アルゴリズムの予想される時間とスペースの複雑さ、
    およびスケーラビリティも含める必要があります。
    例：「このアルゴリズムは、100000を超える多数のサンプルにスケーリングできますが、次元数はスケーリングしません。
    n_featuresは100未満であると予想されます」。

[Code Review Guidelines](https://scikit-learn.org/stable/developers/contributing.html#code-review)
をチェックして、レビュー担当者が何を期待するかを知ることもできます。

次のツールを使用して、一般的なプログラミングエラーを確認できます：

-   良好な単体テストカバレッジ（少なくとも80％、より良い100％）のコードについては、以下を確認してください：

    ```
    pip install pytest pytest-cov
    pytest --cov sklearn path/to/tests_for_package
    ```

    [Testing and improving test coverage](https://scikit-learn.org/stable/developers/contributing.html#testing-coverage)を参照してください。

-   `mypy`で静的分析を実行します：
    
    ```
    mypy sklearn
    ```

    プルリクエストで新しいエラーを生成してはなりません。
    `＃type：ignore`アノテーションを使用すると、
    特にmypyでサポートされていないいくつかのケースの回避策になる可能性があります：
    
    
    - CまたはCythonモジュールをインポートする場合
    - デコレータのあるプロパティについて


ベンチマークスクリプトとプロファイリング出力を使用したパフォーマンス分析を含むコントリビューションはボーナスポイントになります。
（[Monitoring performance](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances)を参照）。

プロファイリングとCython最適化の詳細については、
[How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html#performance-howto)
ガイドも確認してください。
