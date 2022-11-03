#!/usr/bin/env python3

from datetime import datetime
import os
from pytz import timezone
from github import Github

g = Github(os.environ['GITHUB_PERSONAL_ACCESS_TOKEN_MERGE_TRAIN'])
repo = g.get_repo("Patbeagan1/Merge-Train")


def get_slush_branch_name():
    curr_datetime = datetime.now(timezone('US/Eastern'))
    formatted_datetime = f"{curr_datetime.year}_{curr_datetime.month}_{curr_datetime.day}__{curr_datetime.hour}_{curr_datetime.minute}_{curr_datetime.second}"
    return f"slush_{formatted_datetime}"


def create_slush_branch():
    train_branch = get_slush_branch_name()
    default_branch = repo.get_branch(repo.default_branch)
    repo.create_git_ref(
        ref=f"refs/heads/{train_branch}",
        sha=default_branch.commit.sha)
    return train_branch


def get_eligible_pr_list():
    pulls = [pr
             for pr in repo.get_pulls(state='open', sort='created', base='develop')
             if pr.mergeable]
    pulls_ready = [pr for pr in pulls
                   if "Ready to Merge" in [
                       label.name for label in pr.labels
                   ]]

    print([(pr.title, pr.head.ref) for pr in pulls])
    print([(pr.title, pr.head.ref) for pr in pulls_ready])
    return pulls_ready


def update_labels_boarded(pr):
    pr.add_to_labels("On the Train")
    pr.remove_from_labels("Ready to Merge")

def update_labels_detrained(pr):
    pr.add_to_labels("Kicked from Train")
    pr.remove_from_labels("On the Train")


def main():
    pulls_ready = get_eligible_pr_list()
    if pulls_ready:
        train_branch = create_slush_branch()
        for pr in pulls_ready:
            try: 
                update_labels_boarded(pr)
                repo.merge(train_branch, pr.head.ref)
            except Exception as e:
                update_labels_detrained(pr)

if __name__ == "__main__":
    main()
