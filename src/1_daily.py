# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Scrape daily

# %%
from requests_html import HTMLSession
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
import time
import os.path
import git

# %%
url = 'https://www.kath.ch/wp-content/themes/cathkathcatt/ajax.php?esf_showTwocolumns'
list_folder = 'data/list'
article_folder = '/data/article'
path_git = '/data/python/kathch_scraper'


# %%
def download_page(p):
    # Download list
    params = {
        "paged": p,
        "path": "https://www.kath.ch/wp-content/themes/cathkathcatt",
        "posttype": "newsd"
    }

    session1 = HTMLSession()
    r = session1.post(url, data=params)

    # Save to file
    open("%s/%s/%s.html" % (path_git, list_folder, time.time()), 'w', encoding='utf-8').write(r.text)
    
    for el in r.html.find(".esf-content-wrapper .col-lg-6"):
        article_url = el.find(".esf-fullwidth a")[0].attrs['href']
        name = PurePosixPath(unquote(urlparse(article_url).path)).parts[-1]
        print(article_url)

        article_file_name = "%s/%s/%s.html" % (path_git, article_folder, name)
        if os.path.isfile(article_file_name) == False: 
            session_article = HTMLSession()
            r2 = session_article.get(article_url)
            open(article_file_name, 'w', encoding='utf-8').write(r2.text)
        else:
            print("%s already downloaded" % name)


# %%
# Fetch Git
repo = git.Repo(path_git)
repo.git.pull()


# %%
for i in range(1, 3):
    download_page(i)


# %%
repo.git.add(path_git)
if repo.git.diff(None, cached=True) != "":
    repo.git.commit('-m', 'auto-sync', author='webmaster@simonhuwiler.ch')
    repo.git.push()
else:
    print("Nothing changed")


# %%
print("Finito")


# %%



