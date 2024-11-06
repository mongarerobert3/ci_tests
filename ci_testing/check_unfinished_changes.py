import subprocess

def get_git_status(repo_path):
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "status", "--porcelain"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while getting git status: {e}")
        return None

def parse_git_status(lines):
    changes = {
        'untracked': [],
        'unstaged': [],
        'staged': []
    }
    for line in lines:
        if line.startswith('??'):
            changes['untracked'].append(line)
        elif line.startswith(' M') or line.startswith('MM') or line.startswith('AM'):
            changes['unstaged'].append(line)
        elif line.startswith(' M') or line.startswith('MM') or line.startswith('AM'):
            changes['staged'].append(line)
    return changes

def summarize_changes(changes):
    summary = []
    if changes['untracked']:
        summary.append('Untracked files:')
        summary.extend(changes['untracked'])
    if changes['unstaged']:
        summary.append('Changes not staged for commit:')
        summary.extend(changes['unstaged'])
    if changes['staged']:
        summary.append('Changes to be committed:')
        summary.extend(changes['staged'])
    return summary

def main(repo_path):
    lines = get_git_status(repo_path)
    if lines:
        changes = parse_git_status(lines)
        summary = summarize_changes(changes)
        for change in summary:
            print(change)
        print('')

        # Highlight unfinished work: unstaged and uncommitted changes
        print("Highlighted unfinished work:")
        for change_type in ['unstaged', 'staged']:
            for change in changes[change_type]:
                print(change)
        print('')

        # Categorize Changes
        print("Categorized changes:")
        for category, ch in changes.items():
            print(f"{category.capitalize()}:")
            for c in ch:
                print(f"  {c}")
        print('')
    else:
        print("No changes detected or unable to retrieve git status.")

# Example usage
# Replace 'path_to_repo' with the actual path to your Git repository
main('.')