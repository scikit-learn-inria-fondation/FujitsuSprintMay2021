# Development setup

# 開発設定

To avoid duplicating work, it is highly advised that you search through
the [issue tracker](https://github.com/scikit-learn/scikit-learn/issues)
and the [PR list](https://github.com/scikit-learn/scikit-learn/pulls).
If in doubt about duplicated work, or if you want to work on a
non-trivial feature, it\'s recommended to first open an issue in the
[issue tracker](https://github.com/scikit-learn/scikit-learn/issues) to
get some feedbacks from core developers.

作業の重複を避けるために、[issue tracker](https://github.com/scikit-learn/scikit-learn/issues)
と[PRリスト](https://github.com/scikit-learn/scikit-learn/pulls)を検索することを強くお勧めします。
重複した作業について疑問がある場合、または重要な機能に取り組みたい場合は、
最初に[issue tracker](https://github.com/scikit-learn/scikit/issues)で課題を開いて、
コア開発者からフィードバックを得ることが推奨されます。



One easy way to find an issue to work on is by applying the \"help
wanted\" label in your search. This lists all the issues that have been
unclaimed so far. In order to claim an issue for yourself, please
comment exactly `take` on it for the CI to automatically assign the
issue to you.

取り組むべき問題を見つける簡単な方法の1つは、検索に「help wanted」ラベルを適用することです。
これは、これまでに請求されていないすべての問題を一覧表示します。自分で問題を申し立てるには、
CIが自動的に問題を割り当てるように、`take`とコメントしてください。


## How to contribute

## コントリビュートする方法

The preferred way to contribute to scikit-learn is to fork the [main
repository](https://github.com/scikit-learn/scikit-learn/) on GitHub,
then submit a "pull request" (PR).

scikit-learnにコントリビュートするための好ましい方法は、
GitHubで[メインリポジトリ](https://github.com/scikit-learn/scikit-learn/)をフォークしてから、
「Pull Request」（PR）を送信することです。

In the first few steps, we explain how to locally install scikit-learn,
and how to set up your git repository:

最初のいくつかのステップでは、scikit-learnをローカルにインストールする方法と、gitリポジトリを設定する方法について説明します。

1.  [Create an account](https://github.com/join) on GitHub if you do not
    already have one.
    
    まだアカウントを持っていない場合は、GitHubで[アカウントを作成](https://github.com/join)します。

2.  Fork the [project
    repository](https://github.com/scikit-learn/scikit-learn): click on
    the 'Fork' button near the top of the page. This creates a copy of
    the code under your account on the GitHub user account. For more
    details on how to fork a repository see [this
    guide](https://help.github.com/articles/fork-a-repo/).
    
    [プロジェクトのリポジトリ](https://github.com/scikit-learn/scikit-learn)をフォークします：
    ページの上部にある[Fork]ボタンをクリックします。これにより、GitHubユーザーアカウントにコードのコピーが作成されます。
    リポジトリをフォークする方法の詳細については、[このガイド](https://help.github.com/articles/fork-a-repo/)を参照してください。

3.  Clone your fork of the scikit-learn repo from your GitHub account to
    your local disk:
    
    scikit-learnリポジトリのフォークをGitHubアカウントからローカルディスクにクローンします。

    ```
    git clone <git@github.com>:YourLogin/scikit-learn.git # 接続が遅かったら、--depth 1を追加する
    cd scikit-learn
    ```

4.  Install the development dependencies:

    開発の依存関係をインストール:

    ```
    pip install cython pytest pytest-cov flake8 mypy
    ```

    追加NP:ゼロからのインストールの場合は`wheel`（と`numpy`と`scipy`？）も必要です。

5.  Install scikit-learn in editable mode:

    編集可能モードでscikit-learnをインストール:

    ```
    pip install --no-build-isolation --editable .
    ```

    If you receive errors in building scikit-learn, see the
    [Building from source](https://scikit-learn.org/stable/developers/advanced_installation.html#install-bleeding-edge) section.
    
    scikit-learnのビルドでエラーが発生した場合は、[Building from source](https://scikit-learn.org/stable/developers/advanced_installation.html#install-bleeding-edge)セクションを参照してください。

6.  Add the `upstream` remote. This saves a reference to the main
    scikit-learn repository, which you can use to keep your repository
    synchronized with the latest changes:
    
    `upstream`リモートを追加します。これにより、メインのscikit-learnリポジトリへの参照が保存されます。
    これを使用して、リポジトリを最新の変更と同期させることができます。

    ```
    git remote add upstream https://github.com/scikit-learn/scikit-learn.git
    ```

You should now have a working installation of scikit-learn, and your git
repository properly configured. The next steps now describe the process
of modifying code and submitting a PR:

これで、scikit-learnが正常にインストールされ、gitリポジトリが適切に構成されているはずです。
次のステップでは、コードを変更してPRを送信するプロセスについて説明します。

7.  Synchronize your `main` branch with the `upstream/main` branch, more
    details on [GitHub
    Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork):
    
    `main`ブランチを `upstream/main`ブランチと同期します。詳細については、[GitHub Docs](https://docs.github.com/ja/github/collaborating-with-issues-and-pull-requests/working-with-forks/syncing-a-fork)をご覧ください。

    ```
    git checkout main
    git fetch upstream
    git merge upstream/main
    ```

8.  Create a feature branch to hold your development changes:

    開発の変更を保持するフィーチャーブランチを作成して、

    ```
    git checkout -b my_feature
    ```

    and start making changes. Always use a feature branch. It\'s good
    practice to never work on the `main` branch!
    
    変更を加え始めます。常にフィーチャーブランチを使用してください。
    `main`ブランチで作業しないことをお勧めします！

9.  (**Optional**) Install [pre-commit](https://pre-commit.com/#install)
    to run code style checks before each commit:

    (**オプション**)[pre-commit](https://pre-commit.com/#install)をインストールして、
    各コミットの前にコードスタイルチェックを実行します：
    
    ```
    pip install pre-commit
    pre-commit install
    ```

    pre-commit checks can be disabled for a particular commit with `git
    commit -n`.
    
    あるコミットに対して事前コミットチェックを無効にするため、`git commit -n`を使用できます。
    

10. Develop the feature on your feature branch on your computer, using
    Git to do the version control. When you\'re done editing, add
    changed files using `git add` and then `git commit`:
    
    Gitを使用してバージョン管理を行い、フィーチャーブランチでフィーチャーを開発します。
    編集が完了したら、`git add`を使用して変更されたファイルを追加してから`git commit`を使用します。

    ```
    git add modified_files
    git commit
    ```

    to record your changes in Git, then push the changes to your GitHub
    account with:
    
    これにより、Gitでの変更が記録され、次に変更コミットをGitHubアカウントにプッシュします：

    ```
    git push -u origin my_feature
    ```

11. Follow
    [these](https://help.github.com/articles/creating-a-pull-request-from-a-fork)
    instructions to create a pull request from your fork. This will send
    an email to the committers. You may want to consider sending an
    email to the mailing list for more visibility.
    
    ここの[アドバイス](https://help.github.com/articles/creating-a-pull-request-from-a-fork)の指示に従って、
    フォークからプルリクエストPRを作成します。これにより、コミッターにメールが送信されます。
    

If you are modifying a Cython module, you have to re-compile after
modifications and before testing them:

Cythonモジュールを変更する場合は、変更後、テストする前に再コンパイルする必要があります：

```
pip install --no-build-isolation -e .
```


Use the `--no-build-isolation` flag to avoid compiling the whole project
each time, only the files you have modified.

`--no-build-isolation`フラグを使用して、変更したファイルのみを毎回プロジェクト全体でコンパイルしないようにします。

It is often helpful to keep your local feature branch synchronized with
the latest changes of the main scikit-learn repository:

定期的にローカルフィーチャーブランチをメインのscikit-learnリポジトリの最新の変更と同期させることを勧めます：

```
git fetch upstream
git merge upstream/main
```

Subsequently, you might need to solve the conflicts. You can refer to
the [Git documentation related to resolving merge conflict using the
command
line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).

その後、コンフリクトを解決する必要があるかもしれません。
[コマンドラインを使用したマージのコンフリクトの解決に関連するGitドキュメント](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)を参照できます。



### Pull request checklist

### プルリクエストのチェックリスト

Before a PR can be merged, it needs to be approved by two core
developers. Please prefix the title of your pull request with `[MRG]` if
the contribution is complete and should be subjected to a detailed
review. An incomplete contribution \-- where you expect to do more work
before receiving a full review \-- should be prefixed `[WIP]` (to
indicate a work in progress) and changed to `[MRG]` when it matures.
WIPs may be useful to: indicate you are working on something to avoid
duplicated work, request broad review of functionality or API, or seek
collaborators. WIPs often benefit from the inclusion of a [task
list](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
in the PR description.

PRをマージする前に、2人のコア開発者による承認が必要です。投稿が完了し、
詳細なレビューを受ける必要がある場合は、プルリクエストのタイトルの前に`[MRG]`を付けてください。
不完全な投稿（完全なレビューを受け取る前にさらに作業を行うことが予想される場合）は、
タイトルに `[WIP]`（進行中の作業を示すため）を付け、成熟したら `[MRG]`に変更する必要があります。
`WIP`は、重複した作業を無効にするために何かに取り組んでいることを示したり、
フィーチャーやAPIの広範なレビューを要求したり、共同作業者を探したりする場合に役立ちます。
`WIP`は、PRの説明に[タスクリスト](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
を含めることで恩恵を受けることがよくあります。

In order to ease the reviewing process, we recommend that your
contribution complies with the following rules before marking a PR as
`[MRG]`. The **bolded** ones are especially important:

レビュープロセスを容易にするために、PRを`[MRG]`としてマークする前に、
投稿が次のルールに準拠することをお勧めします。 **太字**のものは特に重要です：

1.  **Give your pull request a helpful title** that summarises what your
    contribution does. This title will often become the commit message
    once merged so it should summarise your contribution for posterity.
    In some cases "Fix \<ISSUE TITLE\>" is enough. "Fix \#\<ISSUE
    NUMBER\>" is never a good title.
    
    **プルリクエストに役立つタイトル（コントリビューションの要約）を付けます。** 
    このタイトルは、マージされるとコミットメッセージになることが多いため、要約する必要があります。
    場合によっては、`Fix <ISSUE TITLE>`で十分ですが、`Fix ＃<ISSUE NUMBER>`は決して良いタイトルではありません。

2.  **Make sure your code passes the tests**. The whole test suite can
    be run with `pytest`, but it is usually not recommended
    since it takes a long time. It is often enough to only run the test
    related to your changes: for example, if you changed something in
    `sklearn/linear_model/logistic.py`, running the
    following commands will usually be enough:

    **コードがテストに合格していることを確認してください** テストスイート全体を `pytest`で実行できますが、
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

    There may be other failing tests, but they will be caught by the CI
    so you don\'t need to run the whole test suite locally. For
    guidelines on how to use `pytest` efficiently, see the
    [Useful pytest aliases and flags](https://scikit-learn.org/stable/developers/tips.html#pytest-tips).

    他の失敗したテストがあるかもしれませんが、それらはCIによってキャッチされるので、
    テストスイート全体をローカルで実行する必要はありません。`pytest`を効率的に使用するための
    ガイドラインについては、[Useful pytest aliases and flags](https://scikit-learn.org/stable/developers/tips.html#pytest-tips)を参照してください。
    
3.  **Make sure your code is properly commented and documented**, and
    **make sure the documentation renders properly**. To build the
    documentation, please refer to our
    [Documentation](https://scikit-learn.org/stable/developers/contributing.html#contribute-documentation) guidelines.
    The CI will also build the docs: please refer to
    [Generated documentation on CircleCI](https://scikit-learn.org/stable/developers/contributing.html#generated-doc-ci).
    
    **コードが適切にコメント化および文書化されていることを確認してください**そして**文書が適切にレンダリングされていることを確認してください**。ドキュメントを作成するには、
    [Documentation](https://scikit-learn.org/stable/developers/contributing.html#contribute-documentation)
    ガイドラインを参照してください。

4.  **Tests are necessary for enhancements to be accepted**. Bug-fixes
    or new features should be provided with [non-regression
    tests](https://en.wikipedia.org/wiki/Non-regression_testing). These
    tests verify the correct behavior of the fix or feature. In this
    manner, further modifications on the code base are granted to be
    consistent with the desired behavior. In the case of bug fixes, at
    the time of the PR, the non-regression tests should fail for the
    code base in the `main` branch and pass for the PR code.

    **拡張機能が受け入れられるにはテストが必要です** バグ修正または新フィーチャーは、
    [非回帰テスト](https://ja.wikipedia.org/wiki/%E5%9B%9E%E5%B8%B0%E3%83%86%E3%82%B9%E3%83%88)
    で提供する必要があります。これらのテストは、修正またはフィーチャーの正しい動作を検証します。
    このようにして、コードベースのさらなる変更が許可され、目的の動作と一致します。
    バグ修正の場合、PR時に、`main`ブランチのコードベースで非回帰テストが失敗し、
    PRコードに合格する必要があります。
    
    
5.  **Make sure that your PR does not add PEP8 violations**. To check
    the code that you changed, you can run the following command (see
    `above <upstream>` to set up the
    `upstream` remote):
    
    ** PRがPEP8違反を追加しないことを確認してください** 変更したコードを確認するには、
    次のコマンドを実行するか（`upstream`リモートを設定の手続きは上記述べています）、
    ```
    git diff upstream/main -u -- "*.py" | flake8 --diff
    ```

    or `make flake8-diff` which should work on unix-like
    system.

    または`makeflake8-diff`を実行します。これはUnixなシステムで動作します。
    
    
6.  Follow the [coding-guidelines](https://scikit-learn.org/stable/developers/develop.html#coding-guidelines).

    [coding-guidelines](https://scikit-learn.org/stable/developers/develop.html#coding-guidelines)に従います。

7.  When applicable, use the validation tools and scripts in the
    `sklearn.utils` submodule. A list of utility routines available for
    developers can be found in the [developers-utils](https://scikit-learn.org/stable/developers/utilities.html#developers-utils) page.
    
    該当する場合は、`sklearn.utils`サブモジュールの検証ツールとスクリプトを使用します。
    開発者が利用できるユーティリティルーチンのリストは、[developers-utils](https://scikit-learn.org/stable/developers/utilities.html#developers-utils)ページにあります。

8.  Often pull requests resolve one or more other issues (or pull
    requests). If merging your pull request means that some other
    issues/PRs should be closed, you should [use keywords to create link
    to
    them](https://github.com/blog/1506-closing-issues-via-pull-requests/)
    (e.g., `Fixes #1234`; multiple issues/PRs are allowed as long as
    each one is preceded by a keyword). Upon merging, those issues/PRs
    will automatically be closed by GitHub. If your pull request is
    simply related to some other issues/PRs, create a link to them
    without using the keywords (e.g., `See also #1234`).

    多くの場合、プルリクエストは1つ以上の他の問題（またはプルリクエスト）を解決します。
    プルリクエストをマージすることで他の問題/PRを閉じる場合は、[キーワードを使用してそれらへのリンクを作成する](https://github.com/blog/1506-closeing-issues-via-pull-requests/)
    （例： `Fixes ＃1234`; それぞれの前にキーワードが付いている限り、複数の問題/PRが可能）。
    マージすると、これらの問題/PRはGitHubによって自動的に閉じられます。
    プルリクエストが単に他の問題/PRに関連している場合は、キーワードを使用せずにそれらへの
    リンクを作成します（例：`See also ＃1234`）。
    
    
9.  PRs should often substantiate the change, through benchmarks of
    performance and efficiency (see
    [Monitoring Performances](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances)) or through
    examples of usage. Examples also illustrate the features and
    intricacies of the library to users. Have a look at other examples
    in the
    [examples/](https://github.com/scikit-learn/scikit-learn/tree/main/examples)
    directory for reference. Examples should demonstrate why the new
    functionality is useful in practice and, if possible, compare it to
    other methods available in scikit-learn.
    
    PRは、パフォーマンスと効率のベンチマーク
    （[パフォーマンスの監視](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances)を参照）
    または使用例を通じて、変更を実証する必要があります。
    例では、ライブラリの機能と複雑さもユーザーに示しています。
    [examples/](https://github.com/scikit-learn/scikit-learn/tree/main/examples)
    ディレクトリにある他の例を参照してください。
    例では、新しい機能が実際に役立つ理由を示し、可能であれば、
    scikit-learnで利用可能な他の方法と比較する必要があります。
    

10. New features have some maintenance overhead. We expect PR authors to
    take part in the maintenance for the code they submit, at least
    initially. New features need to be illustrated with narrative
    documentation in the user guide, with small code snippets. If
    relevant, please also add references in the literature, with PDF
    links when possible.
    
    新フィーチャーには、メンテナンスのオーバーヘッドがあります。
    PR作成者は、少なくとも最初は、提出するコードの保守に参加することを期待しています。
    新しいフィーチャーは、ユーザーガイドの説明ドキュメントと小さなコードスニペットで説明する必要があります。
    必要に応じて、可能であればPDFリンクを使用して、文献に参照を追加してください。

11. The user guide should also include expected time and space
    complexity of the algorithm and scalability, e.g. `this algorithm
    can scale to a large number of samples > 100000, but does not scale
    in dimensionality: n_features is expected to be lower than 100`.
    
    ユーザーガイドには、アルゴリズムの予想される時間とスペースの複雑さ、
    およびスケーラビリティも含める必要があります。
    「このアルゴリズムは、100000を超える多数のサンプルにスケーリングできますが、次元数はスケーリングしません。
    n_featuresは100未満であると予想されます」。

You can also check our [Code Review Guidelines](https://scikit-learn.org/stable/developers/contributing.html#code-review) to
get an idea of what reviewers will expect.

[Code Review Guidelines](https://scikit-learn.org/stable/developers/contributing.html#code-review)
をチェックして、レビュー担当者が何を期待するかを知ることもできます。

You can check for common programming errors with the following tools:

次のツールを使用して、一般的なプログラミングエラーを確認できます：

-   Code with a good unittest coverage (at least 80%, better 100%),
    check with:
    
    良好な単体テストカバレッジ（少なくとも80％、より良い100％）のコード、以下を確認してください：

    ```
    pip install pytest pytest-cov
    pytest --cov sklearn path/to/tests_for_package
    ```

    see also [Testing and improving test coverage](https://scikit-learn.org/stable/developers/contributing.html#testing-coverage)
    
    [Testing and improving test coverage](https://scikit-learn.org/stable/developers/contributing.html#testing-coverage)を参照してください。

-   Run static analysis with `mypy`:

    `mypy`で静的分析を実行すると、
    
    ```
    mypy sklearn
    ```

    must not produce new errors in your pull request. Using `# type: ignore`
    annotation can be a workaround for a few cases
    that are not supported by mypy, in particular,

    プルリクエストで新しいエラーを生成してはなりません。
    `＃type：ignore`アノテーションを使用すると、
    特にmypyでサポートされていないいくつかのケースの回避策になる可能性があります：
    
    
    -   when importing C or Cython modules
    -   on properties with decorators
    
    - CまたはCythonモジュールをインポートする場合
    - デコレータのあるプロパティについて

Bonus points for contributions that include a performance analysis with
a benchmark script and profiling output (see
[Monitoring performance](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances).

ベンチマークスクリプトとプロファイリング出力を使用したパフォーマンス分析を含むコントリビューションはボーナスポイントになります。
（[Monitoring performance](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances)を参照）。

Also check out the [How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html#performance-howto)
guide for more details on profiling and Cython optimizations.

プロファイリングとCython最適化の詳細については、
[How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html#performance-howto)
ガイドも確認してください。
