import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(['git'] + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command {' '.join(command)}: {e.stderr.decode('utf-8').strip()}")
        return None

# Check for unstaged changes
unstaged_changes = run_git_command(['status', '--porcelain'])
if unstaged_changes:
    print("Unstaged changes found:\n", unstaged_changes)

# Check for uncommitted changes in the staging area
uncommitted_changes = run_git_command(['diff', '--name-only', '--cached'])
if uncommitted_changes:
    print("Uncommitted changes found:\n", uncommitted_changes)

# Check for branches with unmerged commits
local_branches = run_git_command(['branch', '--no-merged']).split('\n')
if local_branches:
    print("Branches with unmerged commits:")
    for branch in local_branches:
        branch = branch.strip()
        if branch:
            print(branch)

if not unstaged_changes and not uncommitted_changes and not local_branches:
    print("No unfinished changes found in the repository.")