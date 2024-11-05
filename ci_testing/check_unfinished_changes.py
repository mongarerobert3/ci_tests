import subprocess

def git_status():
    # Get the status of the repository
    status_result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True)
    status_output = status_result.stdout.strip()

    if status_output:
        print("There are unstaged changes:")
        print(status_output)
    else:
        print("No unstaged changes found.")

    # Check for uncommitted changes (changes staged for commit)
    commit_result = subprocess.run(['git', 'diff', '--cached', '--name-only'], stdout=subprocess.PIPE, text=True)
    commit_output = commit_result.stdout.strip()

    if commit_output:
        print("There are uncommitted changes:")
        print(commit_output)
    else:
        print("No uncommitted changes found.")

    # Check for unmerged branches
    branches_result = subprocess.run(['git', 'branch', '-r', '--no-merged'], stdout=subprocess.PIPE, text=True)
    branches_output = branches_result.stdout.strip()

    if branches_output:
        print("There are branches with unmerged commits:")
        print(branches_output)
    else:
        print("No branches with unmerged commits found.")

if __name__ == "__main__":
    git_status()