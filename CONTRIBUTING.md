## Contributing
This is a new project that's just getting started. If you have any questions or ideas, email me at travis@highlycomposite.com.

1. [Set up](/docs/setup.md) the project.
2. Run the [tests](/docs/testing.md).
3. Run the [server](/docs/running.md).
4. Email travis@highlycomposite.com to get added as a collaborator to this repo (or you can [work from a fork](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/).
4. Find an [issue](https://github.com/highlycomposite/highlycomposite/issues?q=is%3Aopen+is%3Aissue) that looks interesting. The ones labeled [good-first-issue](https://github.com/highlycomposite/highlycomposite/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22+sort%3Acreated-asc) are best for starting.
5. Make the changes locally, test it, push a commit.
6. Open a PR, and I'll get auto assigned as a reviewer.

### Opening PRs
The branch rules are set up to be strict.

1. Changes can only come in through a PR.
2. The branch getting pulled in has to be up-to-date.
3. The CI steps have to pass before it's pulled in.
4. Only [squash commits](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-merges#squash-and-merge-your-pull-request-commits) are allowed, so don't worry too much about your commit messages going into the PR. Just make one good PR message.

#### Review apps
When you open a PR from a branch within this repo (not a fork), a [review app](https://devcenter.heroku.com/articles/github-integration-review-apps) is automatically created. This is a new environment on Heroku that is built from the code on this PR. They're useful for someone else to look at the changes that you've made without having to run the code themselves. They're deleted after one day without getting any new commits, or once the PR is pulled in.
