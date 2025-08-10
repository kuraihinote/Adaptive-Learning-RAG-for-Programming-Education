# How to push this skeleton to a new public GitHub repo

1. Unzip the archive and enter the folder:
   ```bash
   unzip adaptive_rag_repo.zip
   cd adaptive_rag_repo
   ```

2. Initialize git and create a new repo on GitHub:
   - Option A (manual):
     - Create a new repository on GitHub (https://github.com/new) named `adaptive-rag-programming-education` (or your choice) and copy the remote URL.
     - Then run:
       ```bash
       git init
       git add .
       git commit -m "Initial commit - repo skeleton for Adaptive Learning RAG"
       git branch -M main
       git remote add origin https://github.com/<USERNAME>/<REPO>.git
       git push -u origin main
       ```

   - Option B (GitHub CLI):
     ```bash
     gh repo create <USERNAME>/adaptive-rag-programming-education --public --source=. --remote=origin --push
     ```

3. After pushing, your repo will be public. Copy the URL and submit it.

Need me to generate the `gh` command for your GitHub username? Tell me your username and I can give the exact command.
