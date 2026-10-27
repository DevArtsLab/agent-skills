# README badge catalog

Replace `OWNER/REPO` with the real GitHub slug (from `git remote -v`). Most examples use shields.io; where a service hosts its own badge, that URL is shown instead.

Contents:

- [GitHub repo metadata](#github-repo-metadata)
- [Build and CI](#build-and-ci)
- [Tests and coverage](#tests-and-coverage)
- [Package registries](#package-registries)
- [Code quality and security](#code-quality-and-security)
- [License](#license)
- [Docs and community](#docs-and-community)
- [Platform and runtime](#platform-and-runtime)
- [Fun and misc](#fun-and-misc)
- [shields.io style parameters](#shieldsio-style-parameters)
- [More badges](#more-badges)

## GitHub repo metadata

Dynamic shields.io badges; public repos only.

<!-- ```markdown -->

[![Stars](https://img.shields.io/github/stars/OWNER/REPO)](https://github.com/OWNER/REPO/stargazers)
[![Forks](https://img.shields.io/github/forks/OWNER/REPO)](https://github.com/OWNER/REPO/forks)
[![Watchers](https://img.shields.io/github/watchers/OWNER/REPO)](https://github.com/OWNER/REPO/watchers)
[![Open issues](https://img.shields.io/github/issues/OWNER/REPO)](https://github.com/OWNER/REPO/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/OWNER/REPO)](https://github.com/OWNER/REPO/pulls)
[![Last commit](https://img.shields.io/github/last-commit/OWNER/REPO)](https://github.com/OWNER/REPO/commits)
[![Commit activity](https://img.shields.io/github/commit-activity/m/OWNER/REPO)](https://github.com/OWNER/REPO/commits)
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![Tag](https://img.shields.io/github/v/tag/OWNER/REPO)](https://github.com/OWNER/REPO/tags)
[![Repo size](https://img.shields.io/github/repo-size/OWNER/REPO)]()
[![Code size](https://img.shields.io/github/languages/code-size/OWNER/REPO)]()
[![Top language](https://img.shields.io/github/languages/top/OWNER/REPO)]()
[![Language count](https://img.shields.io/github/languages/count/OWNER/REPO)]()
[![Contributors](https://img.shields.io/github/contributors/OWNER/REPO)](https://github.com/OWNER/REPO/graphs/contributors)
[![Downloads](https://img.shields.io/github/downloads/OWNER/REPO/total)](https://github.com/OWNER/REPO/releases)
[![Discussions](https://img.shields.io/github/discussions/OWNER/REPO)](https://github.com/OWNER/REPO/discussions)

<!-- ``` -->

Star-history variant (chart link, not a badge): `[![Star History](https://api.star-history.com/svg?repos=OWNER/REPO)]`

## Build and CI

Only use when the corresponding config exists in the repo.

<!-- ```markdown -->

[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Deploy](https://github.com/OWNER/REPO/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/OWNER/REPO/actions/workflows/deploy.yml)
[![GitLab CI](https://gitlab.com/OWNER/REPO/badges/main/pipeline.svg)](https://gitlab.com/OWNER/REPO/-/pipelines)
[![CircleCI](https://circleci.com/gh/OWNER/REPO.svg?style=shield)](https://circleci.com/gh/OWNER/REPO)
[![Travis CI](https://app.travis-ci.com/OWNER/REPO.svg?branch=main)](https://app.travis-ci.com/OWNER/REPO)
[![Buildkite](https://badge.buildkite.com/BUILD_UUID.svg)](https://buildkite.com/ORG/PIPELINE)

<!-- ``` -->

Note: GitHub Actions badges use the workflow file path (`ci.yml`), not the workflow display name. Query params: `?branch=main`, `?event=push`.

## Tests and coverage

Only use when coverage is actually uploaded to the service.

<!-- ```markdown -->

[![Codecov](https://codecov.io/gh/OWNER/REPO/branch/main/graph/badge.svg)](https://codecov.io/gh/OWNER/REPO)
[![Coveralls](https://coveralls.io/repos/github/OWNER/REPO/badge.svg?branch=main)](https://coveralls.io/github/OWNER/REPO?branch=main)
[![CodeFactor](https://www.codefactor.io/repository/github/OWNER/REPO/badge)](https://www.codefactor.io/repository/github/OWNER/REPO)

<!-- ``` -->

## Package registries

Only use when the package is actually published.

<!-- ```markdown -->

[![npm](https://img.shields.io/npm/v/PACKAGE)](https://www.npmjs.com/package/PACKAGE)
[![npm downloads](https://img.shields.io/npm/dm/PACKAGE)](https://www.npmjs.com/package/PACKAGE)
[![PyPI](https://img.shields.io/pypi/v/PACKAGE)](https://pypi.org/project/PACKAGE/)
[![PyPI downloads](https://img.shields.io/pypi/dm/PACKAGE)](https://pypi.org/project/PACKAGE/)
[![Python versions](https://img.shields.io/pypi/pyversions/PACKAGE)](https://pypi.org/project/PACKAGE/)
[![crates.io](https://img.shields.io/crates/v/CRATE)](https://crates.io/crates/CRATE)
[![Go reference](https://pkg.go.dev/badge/MODULE.svg)](https://pkg.go.dev/MODULE)
[![Docker pulls](https://img.shields.io/docker/pulls/OWNER/IMAGE)](https://hub.docker.com/r/OWNER/IMAGE)
[![Docker image size](https://img.shields.io/docker/image-size/OWNER/IMAGE)](https://hub.docker.com/r/OWNER/IMAGE)
[![Homebrew](https://img.shields.io/homebrew/v/FORMULA)](https://formulae.brew.sh/formula/FORMULA)
[![Maven Central](https://img.shields.io/maven-central/v/GROUP/ARTIFACT)](https://central.sonatype.com/artifact/GROUP/ARTIFACT)
[![Gem](https://img.shields.io/gem/v/GEM)](https://rubygems.org/gems/GEM)
[![NuGet](https://img.shields.io/nuget/v/PACKAGE)](https://www.nuget.org/packages/PACKAGE)

<!-- ``` -->

## Code quality and security

<!-- ```markdown -->

[![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=PROJECT_KEY&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=PROJECT_KEY)
[![Codacy](https://app.codacy.com/project/badge/Grade/PROJECT_HASH)](https://app.codacy.com/gh/OWNER/REPO/dashboard)
[![DeepSource](https://app.deepsource.com/gh/OWNER/REPO.svg/?label=active+issues)](https://app.deepsource.com/gh/OWNER/REPO/)
[![Snyk](https://snyk.io/test/github/OWNER/REPO/badge.svg)](https://snyk.io/test/github/OWNER/REPO)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/OWNER/REPO/badge)](https://scorecard.dev/viewer/?uri=github.com/OWNER/REPO)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/PROJECT_ID/badge)](https://www.bestpractices.dev/projects/PROJECT_ID)
[![Dependabot](https://img.shields.io/badge/dependabot-enabled-blue.svg?logo=dependabot)]()

<!-- ``` -->

## License

<!-- ```markdown -->

[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)

<!-- ``` -->

Static alternatives when the repo is private or the dynamic badge lags:

<!-- ```markdown -->

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![License: BSD 3-Clause](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](LICENSE)

<!-- ``` -->

## Docs and community

<!-- ```markdown -->

[![Documentation](https://readthedocs.org/projects/PROJECT/badge/?version=latest)](https://PROJECT.readthedocs.io/)
[![Docs](https://img.shields.io/badge/docs-latest-blue.svg)](https://docs.example.com)
[![Discord](https://img.shields.io/discord/SERVER_ID?logo=discord&label=discord)](https://discord.gg/INVITE)
[![Slack](https://img.shields.io/badge/slack-join-4A154B.svg?logo=slack)](INVITE_URL)
[![Matrix](https://img.shields.io/matrix/ROOM:SERVER?logo=matrix)](https://matrix.to/#/#ROOM:SERVER)
[![Twitter Follow](https://img.shields.io/twitter/follow/HANDLE?style=social)](https://twitter.com/HANDLE)
[![YouTube](https://img.shields.io/youtube/channel/subscribers/CHANNEL_ID?style=social)]()

<!-- ``` -->

## Platform and runtime

Static badges for runtime, platform, and toolchain claims:

<!-- ```markdown -->

[![Python 3](https://img.shields.io/badge/python-3-blue.svg?logo=python&logoColor=white)]()
[![Node](https://img.shields.io/badge/node-%3E%3D18-339933.svg?logo=node.js&logoColor=white)]()
[![Rust](https://img.shields.io/badge/rust-stable-orange.svg?logo=rust&logoColor=white)]()
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg?logo=apple)]()
[![Linux](https://img.shields.io/badge/platform-linux-FCC624.svg?logo=linux&logoColor=black)]()
[![Windows](https://img.shields.io/badge/platform-windows-0078D6.svg?logo=windows&logoColor=white)]()
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&logoColor=white)]()
[![Cloudflare Workers](https://img.shields.io/badge/cloudflare-workers-F38020.svg?logo=cloudflare&logoColor=white)]()
[![Vercel](https://img.shields.io/badge/vercel-deployed-000000.svg?logo=vercel&logoColor=white)]()
[![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)]()

<!-- ``` -->

## Fun and misc

<!-- ```markdown -->

[![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made with love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)]()
[![Ask Me Anything](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)]()
[![Architecture diagram](https://gitdiagram.com/diagram-badge.svg)](https://gitdiagram.com/OWNER/REPO)

<!-- ``` -->

## shields.io style parameters

Append to any shields.io badge URL:

- `?style=flat` (default), `flat-square`, `plastic`, `for-the-badge`, `social`
- `&logo=NAME` - any [simple-icons](https://simpleicons.org) slug (e.g. `python`, `github`, `docker`)
- `&logoColor=white`, `&labelColor=555`, `&color=brightgreen`
- Named colors: `brightgreen`, `green`, `yellowgreen`, `yellow`, `orange`, `red`, `blue`, `lightgrey`, `success`, `important`, `critical`, `informational`, `inactive`, `blueviolet`, `ff69b4` - or any hex without `#`

Static badge anatomy: `https://img.shields.io/badge/LEFT-RIGHT-COLOR` renders `[LEFT | RIGHT]`. Use `%20` or `_` for spaces, `--` for a literal dash.

## More badges

- [https://github.com/Ileriayo/markdown-badges](https://github.com/Ileriayo/markdown-badges)
