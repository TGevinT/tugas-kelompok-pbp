function submitHandler(){
    // const date = $('#date').val();
    var patient_name = $('#patient_name').val();
    var patient_age = $('#patient_age').val();
    var patient_gender = $('#patient_gender').val();
    var medicine = $('#medicine').val();

    $.ajax({
        type: "POST",
        url: "add/",
        async:true,
        data: {
            // date: date,
            patient_name: patient_name,
            patient_age: patient_age,
            patient_gender: patient_gender,
            medicine: medicine,
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),
        },
        success: function (response) {
            document.getElementById("form-create").reset();
            $("#close").click();
            getPrescriptionForm();
        },
        error : function (error) {
            console.log(error)
        }
    });
}


function getPrescriptionForm(){
    $("#rows").empty();
    $.get('json/', function(data) {
        $.each(data, function(index, value) {
            $("#rows").append(
                `<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                ${value.fields.patient_name}
                </th>
                </td>
                <td class="py-4 px-6">
                ${value.fields.patient_age}
                </td>
                <td class="py-4 px-6">
                ${value.fields.patient_gender}
                </td>
                <td class="py-4 px-6">
                ${value.fields.medicine}
                </td>
                </tr>`
            );
        });
    });
}