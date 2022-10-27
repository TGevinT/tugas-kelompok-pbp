async function submitHandler(){

    let data = new FormData();
    data.append("csrfmiddlewaretoken", document.getElementsByName("csrfmiddlewaretoken")[0].value)
    data.append("name", document.getElementById("id_name").value)
    data.append("doctor", document.getElementById("id_doctor").value)
    data.append("description", document.getElementById("id_description").value)

    const response = await fetch(
        'add/', {
            method: 'POST',
            header: {
                "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken").value,
            },
            credentials: 'same-origin',
            body: data,
        })

    if(response.status === 200){
        getData();
        document.getElementById("close").click();
    }
}

async function getData() {
    const getResponse = await fetch(
        'json/', {
            method: 'GET',
        }
    )

    let tag = "";

    const data = await getResponse.json()
    data.map((value) => {
        tag += '<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">' +
        '<th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">' +
        value.fields.name +
        '</th>'+
        '<td class="py-4 px-6">' +
        value.fields.date +
        '</td>' +
        '<td class="py-4 px-6">' +
        value.fields.doctor +
        '</td>' +
        '<td class="py-4 px-6">' +
        value.fields.description +
        '</td>' +
        '<td class="py-4 px-6">' +
        '<button id="remove" onClick="remove('+ value.pk +')">Mark Complete</button>' +
        '</td>' +
        '</tr>'
    })

    document.getElementById("rows").innerHTML = tag;
}

async function remove(id){

    let data = new FormData();
    data.append("csrfmiddlewaretoken", document.getElementsByName("csrfmiddlewaretoken")[0].value)

    const remove = await fetch(
        'delete/'+id, {
            method: 'POST',
            header: {
                "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
            },
            credentials: 'same-origin',
            body: data,
        }
    )

    if(remove.status === 200){
        getData()
    }
}