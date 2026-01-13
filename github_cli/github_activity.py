#!/usr/bin/env python3
"""
GitHub Activity CLI
A command-line tool to fetch and display recent GitHub user activity
"""

import sys
import json
import urllib.request
import urllib.error
from datetime import datetime
from typing import Dict, List, Optional, Any


class GitHubActivityCLI:
    """
    Class utama untuk menangani CLI GitHub Activity
    """
    
    
    EVENT_TYPE_MESSAGES = {
        'PushEvent': 'Pushed {payload[commits]} commits to {repo[name]}',
        'IssuesEvent': '{payload[action]} an issue in {repo[name]}',
        'IssueCommentEvent': 'Commented on an issue in {repo[name]}',
        'CreateEvent': 'Created {payload[ref_type]} in {repo[name]}',
        'DeleteEvent': 'Deleted {payload[ref_type]} in {repo[name]}',
        'WatchEvent': 'Starred {repo[name]}',
        'ForkEvent': 'Forked {repo[name]}',
        'PullRequestEvent': '{payload[action]} a pull request in {repo[name]}',
        'PullRequestReviewEvent': 'Reviewed a pull request in {repo[name]}',
        'PullRequestReviewCommentEvent': 'Commented on a pull request review in {repo[name]}',
        'CommitCommentEvent': 'Commented on a commit in {repo[name]}',
        'ReleaseEvent': '{payload[action]} a release in {repo[name]}',
        'GollumEvent': 'Updated wiki pages in {repo[name]}',
        'MemberEvent': '{payload[action]} a member to {repo[name]}',
        'PublicEvent': 'Made {repo[name]} public',
        'SponsorshipEvent': 'Sponsored {repo[name]}',
    }
    
    def __init__(self, username: str):
        """
        Inisialisasi CLI dengan username GitHub
        
        Args:
            username: GitHub username yang akan diambil aktivitasnya
        """
        self.username = username
        self.api_url = f"https://api.github.com/users/{username}/events"
        self.activities = []
    
    def fetch_activities(self) -> bool:
        """
        Mengambil aktivitas dari GitHub API
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        print(f"Fetching activities for {self.username}...")
        
        try:
            # Membuat request ke GitHub API
            request = urllib.request.Request(
                self.api_url,
                headers={
                    'User-Agent': 'GitHub-Activity-CLI/1.0',  # GitHub API memerlukan User-Agent
                    'Accept': 'application/vnd.github.v3+json'
                }
            )
            
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.status == 200:
                    data = response.read()
                    self.activities = json.loads(data.decode('utf-8'))
                    return True
                else:
                    print(f"Error: Received status code {response.status}")
                    return False
                    
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"Error: User '{self.username}' not found")
            elif e.code == 403:
                print("Error: API rate limit exceeded or access forbidden")
                print("Try again later or use GitHub token for authentication")
            else:
                print(f"Error: HTTP {e.code} - {e.reason}")
            return False
            
        except urllib.error.URLError as e:
            print(f"Error: Could not connect to GitHub API - {e.reason}")
            return False
            
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON response - {e}")
            return False
            
        except Exception as e:
            print(f"Error: Unexpected error - {e}")
            return False
    
    def format_activity(self, activity: Dict[str, Any]) -> str:
        """
        Format aktivitas individual menjadi string yang mudah dibaca
        
        Args:
            activity: Data aktivitas dari GitHub API
            
        Returns:
            str: String yang sudah diformat
        """
        event_type = activity.get('type', 'UnknownEvent')
        repo_name = activity.get('repo', {}).get('name', 'Unknown Repository')
        payload = activity.get('payload', {})
        
        # Format timestamp
        created_at = activity.get('created_at', '')
        if created_at:
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                timestamp = dt.strftime('%Y-%m-%d %H:%M')
            except:
                timestamp = created_at
        else:
            timestamp = 'Unknown time'
        
        # Cek apakah event type ada di mapping
        if event_type in self.EVENT_TYPE_MESSAGES:
            try:
                # Gunakan string formatting dengan data dari aktivitas
                message = self.EVENT_TYPE_MESSAGES[event_type]
                
                # Handle kasus khusus untuk beberapa event type
                if event_type == 'PushEvent':
                    # Hitung jumlah commit
                    commits = len(payload.get('commits', []))
                    message = message.replace('{payload[commits]}', str(commits))
                elif event_type == 'IssuesEvent':
                    # Format action (opened, closed, reopened)
                    action = payload.get('action', 'performed action on')
                    message = message.replace('{payload[action]}', action)
                elif event_type == 'PullRequestEvent':
                    action = payload.get('action', 'performed action on')
                    message = message.replace('{payload[action]}', action)
                
                # Ganti placeholder dengan data aktual
                message = message.replace('{repo[name]}', repo_name)
                
            except Exception:
                message = f"{event_type} in {repo_name}"
        else:
            message = f"{event_type} in {repo_name}"
        
        return f"- {message} ({timestamp})"
    
    def display_activities(self, max_activities: int = 10):
        """
        Menampilkan aktivitas di terminal
        
        Args:
            max_activities: Jumlah maksimal aktivitas yang ditampilkan
        """
        if not self.activities:
            print(f"No recent activities found for {self.username}")
            return
        
        print(f"\nRecent GitHub activities for {self.username}:")
        print("=" * 60)
        
        # Tampilkan aktivitas, maksimal max_activities
        for i, activity in enumerate(self.activities[:max_activities]):
            print(self.format_activity(activity))
            
            # Tampilkan informasi tambahan untuk beberapa event type
            self.display_additional_info(activity)
        
        # Tampilkan jumlah total aktivitas
        total = len(self.activities)
        if total > max_activities:
            print(f"\n... and {total - max_activities} more activities")
        else:
            print(f"\nTotal: {total} activities")
    
    def display_additional_info(self, activity: Dict[str, Any]):
        """
        Menampilkan informasi tambahan untuk aktivitas tertentu
        
        Args:
            activity: Data aktivitas dari GitHub API
        """
        event_type = activity.get('type', '')
        payload = activity.get('payload', {})
        
        if event_type == 'PushEvent':
            commits = payload.get('commits', [])
            if commits:
                print("  Commits:")
                for commit in commits[-3:]:  # Tampilkan maksimal 3 commit terakhir
                    message = commit.get('message', '').split('\n')[0]
                    sha = commit.get('sha', '')[:7]
                    print(f"    • {sha}: {message[:50]}{'...' if len(message) > 50 else ''}")
        
        elif event_type == 'IssuesEvent':
            issue = payload.get('issue', {})
            if issue:
                title = issue.get('title', '')
                print(f"  Issue: \"{title[:60]}{'...' if len(title) > 60 else ''}\"")
        
        elif event_type == 'PullRequestEvent':
            pr = payload.get('pull_request', {})
            if pr:
                title = pr.get('title', '')
                print(f"  PR: \"{title[:60]}{'...' if len(title) > 60 else ''}\"")
    
    def get_statistics(self):
        """
        Menampilkan statistik aktivitas
        """
        if not self.activities:
            return
        
        event_counts = {}
        repo_counts = {}
        
        for activity in self.activities:
            event_type = activity.get('type', 'Unknown')
            repo_name = activity.get('repo', {}).get('name', 'Unknown')
            
            event_counts[event_type] = event_counts.get(event_type, 0) + 1
            repo_counts[repo_name] = repo_counts.get(repo_name, 0) + 1
        
        print("\nActivity Statistics:")
        print("-" * 30)
        
        print("Events by type:")
        for event_type, count in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
            event_name = event_type.replace('Event', '')
            print(f"  {event_name}: {count}")
        
        print("\nTop repositories:")
        for repo, count in sorted(repo_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {repo}: {count} events")


def show_help():
    """
    Menampilkan pesan bantuan
    """
    print("GitHub Activity CLI")
    print("=" * 60)
    print("Usage: python github_activity.py <username> [options]")
    print("\nOptions:")
    print("  <username>    GitHub username to fetch activities for")
    print("  --help, -h    Show this help message")
    print("  --stats, -s   Show activity statistics")
    print("  --all, -a     Show all activities (default: 10)")
    print("  --limit N     Show N activities (default: 10)")
    print("\nExamples:")
    print("  python github_activity.py kamranahmedse")
    print("  python github_activity.py kamranahmedse --stats")
    print("  python github_activity.py kamranahmedse --limit 5")
    print("  python github_activity.py kamranahmedse --all")


def main():
    """
    Fungsi utama untuk menjalankan CLI
    """
    # Cek argumen command line
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h']:
        show_help()
        return
    
    username = sys.argv[1]
    show_stats = '--stats' in sys.argv or '-s' in sys.argv
    show_all = '--all' in sys.argv or '-a' in sys.argv
    
    # Cek limit parameter
    limit = None
    for i, arg in enumerate(sys.argv):
        if arg == '--limit' and i + 1 < len(sys.argv):
            try:
                limit = int(sys.argv[i + 1])
            except ValueError:
                print("Error: --limit must be followed by a number")
                return
    
    # Inisialisasi dan jalankan CLI
    cli = GitHubActivityCLI(username)
    
    # Fetch data dari GitHub API
    if not cli.fetch_activities():
        print("\nFailed to fetch activities. Please check the username and try again.")
        return
    
    # Tampilkan aktivitas
    if show_all:
        cli.display_activities(max_activities=len(cli.activities))
    elif limit is not None:
        cli.display_activities(max_activities=limit)
    else:
        cli.display_activities()
    
    # Tampilkan statistik jika diminta
    if show_stats:
        cli.get_statistics()


if __name__ == "__main__":
    main()