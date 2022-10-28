// Octokit.js
// https://github.com/octokit/core.js#readme

import { Octokit } from "https://cdn.skypack.dev/@octokit/core";

const octokit = new Octokit({
    auth: '${{ secrets.GHAPI }}'
  })
  
const response = await octokit.request('GET /repos/Nicholas-Sidharta12365/tugas-kelompok-pbp/collaborators', {
    owner: 'OWNER',
    repo: 'REPO'
  })

let tags = "";

for(let i = 0 ; i < response.data.length; i++){
  console.log(response.data[i].avatar_url);
  tags += "<img src=" + response.data[i].avatar_url + "alt=pfp class='rounded-full h-12 w-12 mx-1'></img>"
}

document.getElementById("collab_list").innerHTML = tags;