# Development setup

To avoid duplicating work, it is highly advised that you search through
the [issue tracker](https://github.com/scikit-learn/scikit-learn/issues)
and the [PR list](https://github.com/scikit-learn/scikit-learn/pulls).
If in doubt about duplicated work, or if you want to work on a
non-trivial feature, it\'s recommended to first open an issue in the
[issue tracker](https://github.com/scikit-learn/scikit-learn/issues) to
get some feedbacks from core developers.

One easy way to find an issue to work on is by applying the \"help
wanted\" label in your search. This lists all the issues that have been
unclaimed so far. In order to claim an issue for yourself, please
comment exactly `take` on it for the CI to automatically assign the
issue to you.


## How to contribute

The preferred way to contribute to scikit-learn is to fork the [main
repository](https://github.com/scikit-learn/scikit-learn/) on GitHub,
then submit a \"pull request\" (PR).

In the first few steps, we explain how to locally install scikit-learn,
and how to set up your git repository:

1.  [Create an account](https://github.com/join) on GitHub if you do not
    already have one.

2.  Fork the [project
    repository](https://github.com/scikit-learn/scikit-learn): click on
    the \'Fork\' button near the top of the page. This creates a copy of
    the code under your account on the GitHub user account. For more
    details on how to fork a repository see [this
    guide](https://help.github.com/articles/fork-a-repo/).

3.  Clone your fork of the scikit-learn repo from your GitHub account to
    your local disk:

    ```
    git clone <git@github.com>:YourLogin/scikit-learn.git # add --depth 1 if your connection is slow
    cd scikit-learn
    ```

4.  Install the development dependencies:

    ```
    pip install cython pytest pytest-cov flake8 mypy
    ```

5.  Install scikit-learn in editable mode:

    ```
    pip install --no-build-isolation --editable .
    ```

    If you receive errors in building scikit-learn, see the
    `install_bleeding_edge` section.

6.  Add the `upstream` remote. This saves a reference to the main
    scikit-learn repository, which you can use to keep your repository
    synchronized with the latest changes:

    ```
    git remote add upstream https://github.com/scikit-learn/scikit-learn.git
    ```

You should now have a working installation of scikit-learn, and your git
repository properly configured. The next steps now describe the process
of modifying code and submitting a PR:

7.  Synchronize your `main` branch with the `upstream/main` branch, more
    details on [GitHub
    Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork):

    ```
    git checkout main
    git fetch upstream
    git merge upstream/main
    ```

8.  Create a feature branch to hold your development changes:

    ```
    git checkout -b my_feature
    ```

    and start making changes. Always use a feature branch. It\'s good
    practice to never work on the `main` branch!

9.  (**Optional**) Install [pre-commit](https://pre-commit.com/#install)
    to run code style checks before each commit:

    ```
    pip install pre-commit pre-commit install
    ```

    pre-commit checks can be disabled for a particular commit with `git
    commit -n`.

10. Develop the feature on your feature branch on your computer, using
    Git to do the version control. When you\'re done editing, add
    changed files using `git add` and then `git commit`:

    ```
    git add modified_files
    git commit
    ```

    to record your changes in Git, then push the changes to your GitHub
    account with:

    ```
    git push -u origin my_feature
    ```

11. Follow
    [these](https://help.github.com/articles/creating-a-pull-request-from-a-fork)
    instructions to create a pull request from your fork. This will send
    an email to the committers. You may want to consider sending an
    email to the mailing list for more visibility.

If you are modifying a Cython module, you have to re-compile after
modifications and before testing them:

```
pip install --no-build-isolation -e .
```


Use the `--no-build-isolation` flag to avoid compiling the whole project
each time, only the files you have modified.

It is often helpful to keep your local feature branch synchronized with
the latest changes of the main scikit-learn repository:

```
git fetch upstream
git merge upstream/main
```

Subsequently, you might need to solve the conflicts. You can refer to
the [Git documentation related to resolving merge conflict using the
command
line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).


### Pull request checklist

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

In order to ease the reviewing process, we recommend that your
contribution complies with the following rules before marking a PR as
`[MRG]`. The **bolded** ones are especially important:

1.  **Give your pull request a helpful title** that summarises what your
    contribution does. This title will often become the commit message
    once merged so it should summarise your contribution for posterity.
    In some cases \"Fix \<ISSUE TITLE\>\" is enough. \"Fix \#\<ISSUE
    NUMBER\>\" is never a good title.

2.  **Make sure your code passes the tests**. The whole test suite can
    be run with `pytest`, but it is usually not recommended
    since it takes a long time. It is often enough to only run the test
    related to your changes: for example, if you changed something in
    [sklearn/linear_model/logistic.py]{.title-ref}, running the
    following commands will usually be enough:

    -   `pytest sklearn/linear_model/logistic.py` to make
        sure the doctest examples are correct
    -   `pytest sklearn/linear_model/tests/test_logistic.py`
        to run the tests specific to the file
    -   `pytest sklearn/linear_model` to test the whole
        `~sklearn.linear_model` module
    -   `pytest doc/modules/linear_model.rst` to make sure
        the user guide examples are correct.
    -   `pytest sklearn/tests/test_common.py -k
        LogisticRegression` to run all our estimator checks
        (specifically for `LogisticRegression`, if that\'s
        the estimator you changed).

    There may be other failing tests, but they will be caught by the CI
    so you don\'t need to run the whole test suite locally. For
    guidelines on how to use `pytest` efficiently, see the
    `pytest_tips`.

3.  **Make sure your code is properly commented and documented**, and
    **make sure the documentation renders properly**. To build the
    documentation, please refer to our
    `contribute_documentation` guidelines.
    The CI will also build the docs: please refer to
    `generated_doc_CI`.

4.  **Tests are necessary for enhancements to be accepted**. Bug-fixes
    or new features should be provided with [non-regression
    tests](https://en.wikipedia.org/wiki/Non-regression_testing). These
    tests verify the correct behavior of the fix or feature. In this
    manner, further modifications on the code base are granted to be
    consistent with the desired behavior. In the case of bug fixes, at
    the time of the PR, the non-regression tests should fail for the
    code base in the `main` branch and pass for the PR code.

5.  **Make sure that your PR does not add PEP8 violations**. To check
    the code that you changed, you can run the following command (see
    `above <upstream>` to set up the
    `upstream` remote):

    ```
    bash \$

    git diff upstream/main -u \-- \"\*.py\" \| flake8 \--diff
    ```

    or `make flake8-diff` which should work on unix-like
    system.

6.  Follow the [coding-guidelines](https://scikit-learn.org/stable/developers/develop.html#coding-guidelines).

7.  When applicable, use the validation tools and scripts in the
    `sklearn.utils` submodule. A list of utility routines available for
    developers can be found in the [developers-utils](https://scikit-learn.org/stable/developers/utilities.html#developers-utils) page.

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

10. New features have some maintenance overhead. We expect PR authors to
    take part in the maintenance for the code they submit, at least
    initially. New features need to be illustrated with narrative
    documentation in the user guide, with small code snippets. If
    relevant, please also add references in the literature, with PDF
    links when possible.

11. The user guide should also include expected time and space
    complexity of the algorithm and scalability, e.g. \"this algorithm
    can scale to a large number of samples \> 100000, but does not scale
    in dimensionality: n_features is expected to be lower than 100\".

You can also check our [Code Review Guidelines](https://scikit-learn.org/stable/developers/contributing.html#code-review) to
get an idea of what reviewers will expect.

You can check for common programming errors with the following tools:

-   Code with a good unittest coverage (at least 80%, better 100%),
    check with:

    ```
    bash \$

    pip install pytest pytest-cov pytest \--cov sklearn
    path/to/tests_for_package
    ```

    see also [Testing and improving test coverage](https://scikit-learn.org/stable/developers/contributing.html#testing-coverage)

    Run static analysis with `mypy`:

    ```
    bash \$

    mypy sklearn
    ```

    must not produce new errors in your pull request. Using `# type: ignore`
    annotation can be a workaround for a few cases
    that are not supported by mypy, in particular,

    -   when importing C or Cython modules
    -   on properties with decorators

Bonus points for contributions that include a performance analysis with
a benchmark script and profiling output (see
[Monitoring performance](https://scikit-learn.org/stable/developers/contributing.html#monitoring-performances).

Also check out the [How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html#performance-howto)
guide for more details on profiling and Cython optimizations.

