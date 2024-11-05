import subprocess

def check_unfinished_changes(repo_path):
    try:
        # Change to the repository directory
        subprocess.run(["git", "-C", repo_path, "status"], check=True)

        # Check for unstaged changes
        unstaged = subprocess.run(
            ["git", "-C", repo_path, "diff", "--name-only"],
            stdout=subprocess.PIPE,
            text=True
        )
        if unstaged.stdout:
            print("There are unstaged changes:")
            print(unstaged.stdout)

        # Check for uncommitted changes in the staging area
        uncommitted = subprocess.run(
            ["git", "-C", repo_path, "diff", "--cached", "--name-only"],
            stdout=subprocess.PIPE,
            text=True
        )
        if uncommitted.stdout:
            print("There are uncommitted changes:")
            print(uncommitted.stdout)

        # Check for unmerged branches
        unmerged = subprocess.run(
            ["git", "-C", repo_path, "branch", "--no-merged"],
            stdout=subprocess.PIPE,
            text=True
        )
        if unmerged.stdout:
            print("There are branches with unmerged commits:")
            print(unmerged.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking the repository: {e}")

# Example usage:
# Replace 'path_to_repo' with the actual path to your Git repository
check_unfinished_changes('.')