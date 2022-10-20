# Code behind **Data Analytics at Nesta** Medium Articles :wave:

<img width="520" alt="Screenshot 2022-10-19 at 12 53 30" src="https://user-images.githubusercontent.com/46863334/196672092-d7b07034-4078-473d-9fb3-4992c97b71b4.png">

**A place to store code for [Medium articles written by Nesta's Data Analytics Team.](https://medium.com/data-analytics-at-nesta)**

This repository is to store code for Medium articles written by Nesta's Data Analytics Team. The purpose of our Medium is to share ideas, reflections and tips and tricks for doing data science for social good. Where the code is soley to compliment a given medium article, this is where you should put it. 

## ❓ Is this the right place for my project? 

1. If the original purpose of the code was to serve a medium blog, it should live in the medium repo. The readme of that repo should be a sort of table of contents of code used in blogs.
2. If the blog is referencing code from a project repo, then add a link to that in the medium repo readme
3. If the code you've made also provides material for an internal tutorial then it's arguable that it should live in its own place, as there's a chance it will get updated.

Long story short - if you're not going to update the code and it's simply to compliment an article, this is the repo for you! The idea is that the projects should be self-contained, so think Google Co-lab style code sharing.  

## 📖 Directory

**< Project name (with link to sub-directory) >**
< Short description of project and links to any key resources >

**[spancat tutorial](https://github.com/nestauk/dap_medium_articles/tree/dev/spancat_tutorial)**
A tutorial to train spaCy's spancat component without using config based training. Read the [Medium article here](https://medium.com/p/992024d047c2/edit) and follow along with the [jupyter notebook here](https://github.com/nestauk/dap_medium_articles/blob/dev/spancat_tutorial/spancat_training.ipynb). 

## 🎮 User guidelines

1. Use the directory above to find the code behind an article that you are looking for.
2. Clone this repository.
3. Follow the code behind the article README for any environment set up (if relevant). 

## 📝  Contributor guidelines

To add a new article repo to this repository:

1. Determine whether this is the right place for the work. See [❓ Is this the right place for my project?](https://github.com/nestauk/dap_medium_articles/tree/spancat#-is-this-the-right-place-for-my-project) 
2. Create an issue for the article. For example, _spancat_.
3. Create a new branch from `dev` and check it out with `git checkout -b <issue number>_<article_name>`
4. Create a subdirectory for this article.
5. Write and commit all code, data and documentation inside this sub-directory. Make sure to add a `README.md`.
6. Once development is finished, add the name and description of the article to the Directory above. Don't forget to add a link to the Medium article once it's been published.
7. Create a pull request into `dev`.

When writing your article, the following requirements must be met.

**👍 Development standards**
- Adhere to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
- All requirements to run code behind the article should be independent and defined within the sub-directory (e.g. in a `requirements.txt` or `environment.yml`). Again, you may not want to have a `requirements.txt` and instead contain it all in a notebook.
- Add descriptions of what is happening in each grey cell for readers to follow along.  
- The code must run from start to finish without error.
- Each article should contain its own `README.md` that gives a comprehensive description of the work.

**🔀 Workflow**
- Make pull requests and request code reviews.
- Use the [Nesta Git/GitHub guidelines](https://github.com/nestauk/github_support/blob/dev/guidelines/README.md). Your code is simple and short so you will likely work in one branch and merge into `dev` with one PR. 

**💾 Data**
- Small datasets (~1Mb) can be stored in the repository. 
- Otherwise, if you're using a toy dataset from a data source, simply add steps for a user to download the data locally in your article README.md so they can run the code.

Many of these guidelines require judgement on your part. If in doubt, chat to someone else in the team 🙂