#!/usr/bin/env python3

import os
from github import Github

g = Github(
    # access_token
    os.environ['GITHUB_PERSONAL_ACCESS_TOKEN_MERGE_TRAIN']
)

repo = g.get_repo("Patbeagan1/Merge-Train")

pulls = [pr
         for pr in repo.get_pulls(state='open', sort='created', base='develop')
         if pr.mergeable]

for pr in pulls:
    print(pr.title)
    print(pr.labels)
    pr.add_to_labels("On The Train")
    pr.remove_from_labels("Ready to Merge")


