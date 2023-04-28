# Gith_Improve 🚧
- [x] **01_Terminal_Makeover** - Pretty CML Skin
- [x] **02_Github_Profile** - Set up a fancy readme
- [ ] 03_Dynamic_Git_Profile
- [ ] 04_Github_Actions

## 01_Terminal_Makeover  
- [x] 1) Theme [[blog]](https://towardsdatascience.com/the-ultimate-guide-to-your-terminal-makeover-e11f9b87ac99) 
  - Homebrew: `https://brew.sh/` installs packages to their own directory and then symlinks their files into /opt/homebrew
  - [starship](https://starship.rs/)
- [x] 2) [ohmyzsh!](https://github.com/ohmyzsh/ohmyzsh)
  - Zsh is a shell designed for interactive use and it is also a powerful scripting language
  - Oh-My-Zsh is an open-source, community-driven framework for managing your ZSH configuration
  - [[themes]](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes) `cloud` `half-life` `jonathan`
  - `vim ~/.zshrc` change theme!
- [x] 3) [bash-it](https://github.com/Bash-it/bash-it)
  - [[themes]](https://bash-it.readthedocs.io/en/latest/themes-list/#list-of-themes) `export BASH_IT_THEME="Metal"`
  - `sudo chown usr ~/.bash_profile`
  
**Anaconda_Path_Fix**
- `source /opt/anaconda3/bin/activate`
- `conda init zsh`

## 02_Github_Profile
Goal: add more personality to my github profile and make it less boring 🤠
- [x] Add a [profile_readme](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
  - A couple of templates I like .. [[Jan]](https://github.com/jborchma) and [[Ian]](https://github.com/ian-whitestone)
- [x] Add bio

<br />

### 03_Dynamic_Git_Profile
- [x] Install npm 
- [x] [mustache](https://www.npmjs.com/package/mustache)
- [x] [Self Updating Readme](https://medium.com/swlh/how-to-create-a-self-updating-readme-md-for-your-github-profile-f8b05744ca91)

**git_workflow** `main.yaml`
1. Checkout current repository to Master branch
2. Setup NodeJs 13.x
3. Cache dependencies and build outputs to improve workflow execution time
4. Install dependencies
5. Generate README file
6. Commit and Push new `README.md` to the repository

<br />

### 04_Github_Actions
[learn-github-actions](https://docs.github.com/en/actions/learn-github-actions)
- Continuous integration and continuous delivery (CI/CD) platform
- Automate build, test, and deployment pipeline

[git-auto-commit](https://michaelheap.com/git-auto-commit/)


