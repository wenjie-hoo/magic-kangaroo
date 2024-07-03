---
title: How I built this blog site
date: 2022-08-22 23:25:22
updated: 2022-08-23
cover: https://as1.ftcdn.net/v2/jpg/02/94/60/60/1000_F_294606038_g0vKr7gu0t5qUqjNgEnm2GCTXBpgTZ00.jpg
categories: tech
tags: tech
---

💡 **[Hexo](https://hexo.io/)** is a straightforward and fast blog static site framework with various themes you can select from. The following will introduce how I build this blog site with Hexo and **[hexo-theme-cactus](https://github.com/probberechts/hexo-theme-cactus).**

<!-- vscode-markdown-toc -->
* 1. [Prerequisites](#Prerequisites)
* 2. [Quick Start with Hexo](#QuickStartwithHexo)
	* 2.1. [Installing Hexo](#InstallingHexo)
	* 2.2. [Setting up Hexo locally](#SettingupHexolocally)
	* 2.3. [Posting your first blog](#Postingyourfirstblog)
	* 2.4. [Let’s write something](#Letswritesomething)
	* 2.5. [Generating static files](#Generatingstaticfiles)
* 3. [Changing the theme](#Changingthetheme)
	* 3.1. [installing hexo-theme-cactus](#installinghexo-theme-cactus)
	* 3.2. [Setting the Theme](#SettingtheTheme)
	* 3.3. [configuration](#configuration)
* 4. [Deploying Hexo blog on Github Pages](#DeployingHexoblogonGithubPages)
	* 4.1. [creating a repository](#creatingarepository)
	* 4.2. [One-command deployment](#One-commanddeployment)

##  1. <a name='Prerequisites'></a>Prerequisites

- [Node.js](https://nodejs.org/en/)
- [Git](https://git-scm.com/downloads)
-- For MacOs
```
$ brew install node
$ brew install git
```
-- For Linux
```
$ sudo apt update
$ sudo apt install nodejs
$ sudo apt install git
```
<aside>
❗ make sure Node.js and Git are both installed on your machine.
</aside>

##  2. <a name='QuickStartwithHexo'></a>Quick Start with Hexo

###  2.1. <a name='InstallingHexo'></a>Installing Hexo

```bash
$ npm install hexo-cli -g
```

###  2.2. <a name='SettingupHexolocally'></a>Setting up Hexo locally

```bash
$ hexo init ~/blog
$ cd ~/blog
$ hexo server
```

- Now, you can visit your basic Hexo blog at [http://localhost:4000](http://localhost:4000/). Hexo will watch for all file changes and automatically render the site. You can press *`Ctrl+C` to stop the server.*

###  2.3. <a name='Postingyourfirstblog'></a>Posting your first blog

```bash
$ hexo new post "my first post"
```

- Restart the `hexo server`, and you will see your first post!

###  2.4. <a name='Letswritesomething'></a>Let’s write something

- Before writing the first blog, let’s take a look at the Hexo file structure.

```bash
$ tree -L 3

|-- _config.landscape.yml
|-- _config.yml
|-- db.json
|-- node_modules
|-- package-lock.json
|-- package.json
|-- scaffolds
|-- source
|   `-- _posts
|       |-- hello-world.md
|       `-- my-first-post.md
`-- themes
```

- As we can see, the new post "my first post" has been created inside the  `source/_posts` folder, and all of your posts will be stored in this folder if not assigned categories. By default, Hexo has created a  `hello-world.md` tutorial post for us.
- Now, you can add any content to this new post.

```bash
$ vim ~/blog/source/_posts/my-first-post.md

	---
	title: my first post
	date: 2022-08-21 00:50:27
	tags:
	---

	Ciao! This is my first Hexo blog post!
```

- Press `Esc` and then type `:wq` to quit [Vim](https://www.vim.org/). Restart Hexo server and refresh [http://localhost:4000](http://localhost:4000/), you will see the post.

###  2.5. <a name='Generatingstaticfiles'></a>Generating static files

```bash
$ hexo generate 
```

- All static files will be generated under `/blog/public/` folder.

##  3. <a name='Changingthetheme'></a>Changing the theme

<aside>
💡 Changing the theme of Hexo blog is straightforward. There have more than 300 items you can choose from [Hexo Themes](https://hexo.io/themes/), or customized themes from Github repo. Here, I’ll pick the [Cactus](https://github.com/probberechts/hexo-theme-cactus) theme.

</aside>

###  3.1. <a name='installinghexo-theme-cactus'></a>installing hexo-theme-cactus

```bash
$ cd ~/blog
$ git clone https://github.com/probberechts/hexo-theme-cactus.git themes/cactus
```

###  3.2. <a name='SettingtheTheme'></a>Setting the Theme

- Modify the value of `theme:` in `_config.yml` file to `cactus`, and restart Hexo server.

```bash
# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: cactus 
```

```bash
$ hexo server
```

###  3.3. <a name='configuration'></a>configuration

- Most of the site settings can be found in the [`_config.yml`](https://github.com/probberechts/hexo-theme-cactus/blob/master/_config.yml) file.

```bash
# Site
title: Magic Cat
subtitle: 
description: Not done yet, I\'m trying
keywords:
author: Clark
language: en
timezone: ''
```

- More theme detail settings can be found in `~/blog/themes/cactus/_config.yml`

```bash
projects_url: https://github.com/username/username.github.io
direction: ltr
nav:
  home: /
  about: /about/
  articles: /archives/
  Gallery: /gallery
  Archives: /
  Search: /search/
  
social_links:
  github: https://github.com/username
...
# Available color schemes are 'dark', 'light', 'classic' and 'white'.
colorscheme: light
...

```

- For more Features of cactus themes please visit **[`hexo-theme-cactus`](https://github.com/probberechts/hexo-theme-cactus).**

##  4. <a name='DeployingHexoblogonGithubPages'></a>Deploying Hexo blog on Github Pages

<aside>
💡 If you want to deploy the Hexo blog to a server, Github will provide a good way to publish your website.

</aside>

###  4.1. <a name='creatingarepository'></a>creating a repository

- Create [a new public repo](https://github.com/new) named [username.github.io](http://username.github.io) on your Github, make sure to get the username right, if the repo name doesn’t match with your username, it won’t work.

```bash
$ cd ~
$ git clone https://github.com/username/username.github.io
```

- Generating Hexo public files

```bash
$ cd ~/blog
$ hexo clean
$ hexo generate
```

- Copy all the files generated under `~/blog/public` to `~ @/username.github.io`

```bash
$ cp -r ~/blog/public/* ~/username.github.io/
```

- Push it

```bash
$ cd ~/username.github.io/
$ git add .
$ git commit -m "Initial commit"
$ git push -u origin main
```

- Wait for a few minutes, then go to [username.github.io](http://username.github.io) on a browser, you can see your new blog on Github Pages, and you’re done!

###  4.2. <a name='One-commanddeployment'></a>One-command deployment

- Hexo provides a more straightforward way to deploy your site. First, install [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git)

```bash
$ cd ~/blog
$ npm install hexo-deployer-git --save
```

- Next, add configs to the bottom of the `_config.yml` file as follows.

```bash
deploy:
  type: git
  repo: https://github.com/<username>/<project>
  branch: main
```

- Then, run:

```bash
$ hexo clean && hexo deploy
```

- Wait for a few minutes, check your webpage at  [username.github.io](http://username.github.io)