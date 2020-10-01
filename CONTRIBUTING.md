# How to Contribute

We would love your help! and just fun in Hacktoberfest

## Prerequisites
Prepare for contributing by following these beginner-friendly steps.

<p align = "center"><img src = "https://media.giphy.com/media/xUA7aQOxkz00lvCAOQ/giphy.gif" width = 40%></p>

1. Make sure you have created a [GitHub account](https://github.com/join), and are signed in.
2. Fork this repo by clicking the "fork" button in the upper-right corner of this page.
3. Choose a directory on your machine where you plan to store Github Projects. Open your terminal and `cd` to that directory.
4. Clone the project by running `git clone https://github.com/<your-username-here>/Prepration_Code_Repository.git` in your terminal, replacing `<your-username-here>` with your account name.
5. Run `cd Prepration_Code_Repository` to get into the root directory.
6. Run `git remote add upstream https://github.com/ashuprince121/Prepration_Code_Repository.git`.  This is so that you can refer to the original project as the `upstream` version.
7. You cant check your remotes using the command `git remote -v`. Initially you should see this:
```
origin	https://github.com/<your-username-here>/Prepration_Code_Repository.git (fetch)
origin	https://github.com/<your-username-here>/Prepration_Code_Repository.git (push)
upstream	https://github.com/ashuprince121/Prepration_Code_Repository.git (fetch)
upstream	https://github.com/ashuprince121/Prepration_Code_Repository.git (push)

```

## Get started

<p align = "center"><img src = "https://media.giphy.com/media/Ln2dAW9oycjgmTpjX9/giphy.gif" width = 40%></p>

1. Check out for an issue or create another one.
2. Leave a comment that you would like to pick up that issue.
3. Read the description, and make sure to ask questions about anything that is unclear.
5. Make sure you have the latest version of the project with `git pull upstream master` or `git merge upstream/master`.
6. Create a new branch with `git checkout -b <new-branch-name>`. The name should include the issue number and the topic you're working in or simply information about the task you are going to do.  For example, if its about issue #11: resolving a typo in readme, your command could be `git checkout -b 11__resolve-typo-readme`.
7. Make and commit your changes on this new branch, and make a PR when you're ready. [Here are some directions on the process](http://www.dasblinkenlichten.com/how-to-create-a-github-pull-request-pr/).
8. When creating your PR, be sure to make your pull request to the `master` feature branch: 
9. See your pull requests here: https://github.com/ashuprince121/Prepration_Code_Repository/pulls

## Note
If you want that your PR to count as part of a contribution in the Hacktoberfest, remember to join the event in this [link](https://hacktoberfest.digitalocean.com/)