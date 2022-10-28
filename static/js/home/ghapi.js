// Octokit.js
// https://github.com/octokit/core.js#readme
const octokit = new Octokit({
    auth: '${{ secrets.GHAPI }}'
  })
  
  await octokit.request('GET /repos/Nicholas-Sidharta12365/tugas-kelompok-pbp/collaborators', {
    owner: 'OWNER',
    repo: 'REPO'
  })

  