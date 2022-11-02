async function getVaksin() {
    return fetch("/vaksin/json").then((res) => res.json())
}

async function getUserVaksin() {
    return fetch("/vaksin/json1").then((res) => res.json())
}

async function refreshVaksin() {
    document.getElementById("table_header").innerHTML= ""
    let html=`\n
    <tr>
    <th class="px-10 py-2 text-center border border-slate-500">Nama Vaksin</th>
    <th class="px-10 py-2 text-center border border-slate-500">Efek Samping</th>
    <th class="px-10 py-2 text-center border border-slate-500">Dosis Vaksin(mg)</th>
    <th class="px-10 py-2 text-center border border-slate-500">Hapus Vaksin</th>
    </tr>`
    document.getElementById("table_header").innerHTML = html

    document.getElementById("data_vaksin").innerHTML = ""
    const vaksin = await getVaksin()
    let htmlString = ``
    vaksin.forEach((item) => {
    htmlString += `\n
    <tr>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.name}</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.side_effect}</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.dose} mg</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">
      <a class="link no-underline decoration-gray-500 hover:decoration-gray-100" onclick="deleteVaksin(${item.pk})">Delete</a>
    </th>
    </tr>` 
    })
    
    document.getElementById("data_vaksin").innerHTML = htmlString
    document.getElementById("kembali").style.display = "none";
    document.getElementById("user_button").style.display = "block";
}

async function userVaksin() {
    document.getElementById("table_header").innerHTML= ""
    let html=`\n
    <tr>
    <th class="px-10 py-2 text-center border border-slate-500">Nama Vaksin</th>
    <th class="px-10 py-2 text-center border border-slate-500">Tanggal Penambahan</th>
    <th class="px-10 py-2 text-center border border-slate-500">Efek Samping</th>
    <th class="px-10 py-2 text-center border border-slate-500">Dosis Vaksin(mg)</th>
    </tr>`
    document.getElementById("table_header").innerHTML = html

    document.getElementById("data_vaksin").innerHTML = ""
    const userVaksin = await getUserVaksin()
    let htmlString = ``
    userVaksin.forEach((item) => {
    htmlString += `\n
    <tr>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.name}</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.date}</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.side_effect}</th>
    <th class="py-2.5 font-normal text-center border border-slate-500">${item.fields.dose} mg</th>
    </tr>` 
    })
    
    document.getElementById("data_vaksin").innerHTML = htmlString
    document.getElementById("user_button").style.display = "none";
    document.getElementById("kembali").style.display = "block";
}

async function vaksinList() {
  document.getElementById("select_dropdown").innerHTML=""
  const vaksin_list = await getVaksin()
  let htmlString = ''
  vaksin_list.forEach((item) => {
    htmlString+= `\n
    <option value="${item.pk}">${item.fields.name}</option>
    `
  })
  document.getElementById("select_dropdown").innerHTML = htmlString
}

async function vaksinList1() {
  document.getElementById("select_dropdown1").innerHTML=""
  const vaksin_list1 = await getVaksin()
  let htmlString = ''
  vaksin_list1.forEach((item) => {
    htmlString+= `\n
    <option value="${item.pk}">${item.fields.name}</option>
    `
  })
  document.getElementById("select_dropdown1").innerHTML = htmlString
  document.getElementById("text_stock").innerHTML = ""
}

async function addVaksin() {
    fetch("/vaksin/add/", {
        method: "POST",
        body: new FormData(document.querySelector('#form_vaksin'))
    }).then(refreshVaksin)
    return false
}

async function deleteVaksin(id) {
    let url = "/vaksin/delete-vaksin/" + id;
    fetch(url).then(refreshVaksin)
}

async function editDose() {
  fetch("/vaksin/change/", {
    method: "POST",
    body: new FormData(document.querySelector('#edit_dose'))
  }).then(refreshVaksin)
}

async function checkStock() {
  document.getElementById("text_stock").innerHTML=""
  const temp = await getVaksin()
  var e =document.getElementById("select_dropdown1");
  var value = e.value;
  let htmlString = ''
  temp.forEach((item)=> {
    if(item.pk == value){
      htmlString+= `\n
      <h3 class="text-white">Stok Vaksin "${item.fields.name}" adalah ${item.fields.stock}</h3>
      `
    }
  })
  document.getElementById("text_stock").innerHTML = htmlString
}