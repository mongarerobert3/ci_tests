import subprocess

def check_unfinished_changes():
    # Check for unstaged changes
    unstaged_changes = subprocess.run(['git', 'diff', '--name-only'], stdout=subprocess.PIPE).stdout.decode().strip()
    
    # Check for uncommitted changes in the staging area
    uncommitted_changes = subprocess.run(['git', 'diff', '--staged', '--name-only'], stdout=subprocess.PIPE).stdout.decode().strip()
    
    # Check for branches with unmerged commits
    branches_with_unmerged_commits = subprocess.run(['git', 'branch', '-r', '--no-merged'], stdout=subprocess.PIPE).stdout.decode().strip()
    
    if unstaged_changes:
        print("There are unstaged changes:")
        print(unstaged_changes)
    else:
        print("No unstaged changes.")
        
    if uncommitted_changes:
        print("There are uncommitted changes:")
        print(uncommitted_changes)
    else:
        print("No uncommitted changes.")
        
    if branches_with_unmerged_commits:
        print("There are branches with unmerged commits:")
        print(branches_with_unmerged_commits)
    else:
        print("No branches with unmerged commits.")

check_unfinished_changes()