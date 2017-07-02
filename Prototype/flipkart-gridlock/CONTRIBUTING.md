# Contributing

We welcome contributions in several forms, e.g.

* Documenting
* Testing
* Coding
* etc.

Please read [14 Ways to Contribute to Open Source without Being a Programming Genius or a Rock Star](http://blog.smartbear.com/programming/14-ways-to-contribute-to-open-source-without-being-a-programming-genius-or-a-rock-star/)

## Git Guidelines

### Workflow

We currently recommend the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).

The mentioned links from Atlassian are the recommended docs to read and understand the git workflows.


### Git Commit

The cardinal rule for creating good commits is to ensure there is only one "logical change" per commit. There are many reasons why this is an important rule:

* The smaller the amount of code being changed, the quicker & easier it is to review & identify potential flaws.
* If a change is found to be flawed later, it may be necessary to revert the broken commit. This is much easier to do if there are not other unrelated code changes entangled with the original commit.
* When troubleshooting problems using Git's bisect capability, small well defined changes will aid in isolating exactly where the code problem was introduced.
* When browsing history using Git annotate/blame, small well defined changes also aid in isolating exactly where & why a piece of code came from.

Things to avoid when creating commits

* Mixing whitespace changes with functional code changes.
* Mixing two unrelated functional changes.
* Sending large new features in a single giant commit.


### Git Commit Conventions

We use git commit as per (Conventional Changelog)[https://github.com/ajoslin/conventional-changelog]:

    <type>(<scope>): <subject>

Example:

    docs(CONTRIBUTING.md): add commit message guidelines

Allowed types:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **refactor**: A code change that neither fixes a bug or adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

For JavaScript/Grunt projects we can use (grunt-conventional-changelog)[https://github.com/btford/grunt-conventional-changelog] to autogenerate CHANGELOG.md.

### Copyright Header

SiMPL is utilizing the [Siemens Inner Source License - 1.1](https://code.siemens.com/siemens/code/blob/master/LICENSE.md)
and tries to do OSS clearing for all of it's components. It is therefore
necessary to have the mandatory copyright header on all source files as following:

```
# Copyright Siemens AG, [YEAR]
# Licensed under the Siemens Inner Source License 1.1
```

Contributions without this header on each new source file won't be accepted.

The meaning of source files covers all files, which allow adding a comment
easily (e.g. `.js` / `.css`) and contribute to the core value of project by
adding originality (e.g. no `.editoconfig` / `.jscsrc`).

### Developer Certificate of Origin (DCO)

All commits with potential upstream code shall contain a Signed-off-by line, also known as the **Developer Certificate of Origin (DCO)** as we know it from the Linux Kernel [Documenation/SubmittingPatches](https://www.kernel.org/doc/Documentation/SubmittingPatches)


    Signed-off-by: Roger Meier <r.meier@siemens.com>

additional tags in addition to Signed-off-by shall be used as long as it makes sence, e.g.

    Reviewed-by:
    Tested-by:
    Reviewed-by:
    Suggested-by:
    Acked-by:

#### External Developers
external developers shall use their Siemens email address, e.g.


    Signed-off-by: Super Hacker <super.hacker.ext@siemens.com>
