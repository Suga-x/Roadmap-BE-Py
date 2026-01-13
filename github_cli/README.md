# GitHub Activity CLI - README

## Deskripsi Proyek
GitHub Activity CLI adalah alat baris perintah sederhana yang dibangun dengan Python untuk mengambil dan menampilkan aktivitas terbaru pengguna GitHub.

## Fitur Utama
- Mengambil aktivitas GitHub pengguna dari API GitHub
- Menampilkan aktivitas dalam format yang mudah dipahami
- Support berbagai jenis event GitHub (Push, Issues, Stars, dll.)
- Statistik aktivitas (opsional)
- Error handling yang baik
- Tidak memerlukan library eksternal

## Persyaratan
- Python 3.x
- Koneksi internet

## Cara Menggunakan

### Instalasi
Tidak ada instalasi khusus. Pastikan Python 3.x sudah terinstal.

### Menjalankan CLI

**Versi Lengkap:**
```
python github_activity.py --help
python github_activity.py Suga-x
python github_activity.py Suga-x --stats
python github_activity.py Suga-x --limit 5
python github_activity.py Suga-x --all
```

**Versi Sederhana:**
```
python github_activity_simple.py Suga-x
```

### Membuat Executable
1. Buat file `github-activity`:
```bash
#!/bin/bash
python3 /path/to/github_activity.py "$@"
```

2. Berikan permission:
```
chmod +x github-activity
```

3. Gunakan langsung:
```
github-activity Suga-x
```

## Contoh Output
```
Fetching activities for Suga-x...

Recent GitHub activities for Suga-x:
============================================================
- Pushed 3 commits to Suga-x/Roadmap-BE-Py (2024-01-15 10:30)
  Commits:
    • abc1234: Update documentation
    • def5678: Fix typo in README
- Starred facebook/react (2024-01-14 16:45)
- Opened an issue in kamranahmedse/developer-roadmap (2024-01-14 14:20)

Total: 15 activities
```

## Event yang Didukung
- PushEvent: Commit ke repository
- IssuesEvent: Issue baru/update
- WatchEvent: Star repository
- ForkEvent: Fork repository
- CreateEvent: Buat repository/branch
- PullRequestEvent: Pull request
- Dan event GitHub lainnya

## Error Handling
- User tidak ditemukan (404)
- Rate limit terlampaui (403)
- Koneksi gagal (network error)
- Response JSON invalid
- Parameter tidak valid

## Teknologi yang Digunakan
- Python 3.x
- urllib (HTTP client bawaan Python)
- JSON
- GitHub REST API

## Catatan Penting
1. Rate Limiting: GitHub API memiliki rate limit 60 request per jam tanpa autentikasi
2. User-Agent: GitHub API memerlukan header User-Agent yang valid
3. Public Data: Hanya aktivitas publik yang bisa diakses

## Pengembangan Lanjutan
1. Autentikasi dengan GitHub Token
2. Caching hasil query
3. Filter berdasarkan jenis event
4. Export data ke format JSON/CSV
5. Pagination untuk data besar

## Referensi
- GitHub REST API Documentation: https://docs.github.com/en/rest
- GitHub Events API: https://docs.github.com/en/rest/activity/events
- Python urllib Documentation: https://docs.python.org/3/library/urllib.html