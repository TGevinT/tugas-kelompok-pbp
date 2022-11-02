
function submitHandlerPayment(){
    var id = $('#payment').val()
    var money_paid = $('#moneyPaid').val()

    $.ajax({
        type: "POST",
        url: "payment/" + id,
        async:true,
        data: {
            money_paid: money_paid,
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),
        },
        success: function (data){
            document.getElementById("form-payment").reset();
            $("#form-payment").empty();
            if(data.payment){
                getForm();
                getPaymentSuccess(data.kembalian);
            }else{
                getPaymentFailed();
            }
        },
        error : function (error) {
            console.log(error)
        }
    });
}

function submitHandlerCreate(){
    var patient = $('#id_patient').val()
    var doctor = $('#id_doctor').val()
    var description = $('#id_description').val()
    var bill = $('#id_bill').val()

    $.ajax({
        type: "POST",
        url: "create/",
        async:true,
        data: {
            patient: patient,
            doctor: doctor,
            description: description,
            bill: bill,
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),
        },
        success: function (response) {
            document.getElementById("form-create").reset();
            $("#close").click();
            getForm();
        },
        error : function (error) {
            console.log(error)
        }
    });
}
function getModalPayment(){
    document.getElementById("form-payment").reset();
    $("#form-payment").empty();

    var tag = ""
    $.get('json/', function(data) {
        $.each(data,function(index, value) {

            if (!(value.fields.patient_status_payment)){
                tag += `<option value='${value.pk}'> ${value.fields.patient} with doctor ${value.fields.doctor} : ${value.fields.bill} </option>`
                console.log(value.fields.patient_status_payment)
            }
        }); 
        $("#form-payment").append(
            `<div class="modal-body">
                <div class="grid grid-rows-1 gap-4">
                    <label for = 'payment'>Choose a patient : </label>
                    <select id = 'payment' name = 'payment' class="border border-black" >
                        ${tag}
                    </select>
                    <div class="grid grid-cols-3 place-items-center">
                        <label for="moneyPaid" class="col-span-1">Cash : </label>
                        <input id="moneyPaid" type="number" name="moneyPaid" class="col-span-2 border border-black" autocomplete="off" required />
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" id="close" class="btn btn-secondary border-red-600 text-red-600 hover:bg-red-600 hover:text-white" data-bs-dismiss="modal">Close</button>
                <button type="button" onclick="submitHandlerPayment()" class="btn btn-primary text-blue-600 hover:text-white">Submit</button>
            </div>`
        );
    });

}

function getPaymentSuccess(kembalian){
    $("#form-payment").append(
        `<div class="modal-body flex justify-center flex-col>
            <div class="">
                <img src="/static/images/centang_hijau.png" class="mr-3 h-10 sm:h-20" alt="Centang Hijau">
            </div>
            <div class="text-center">
                <div class="text-green-500 text-2xl"> Payment Successfully</div>
            </div>
            <div class="text-center mt-3 mb-2">
                <p class="my-2">Kembalian : Rp ${kembalian}</p>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" onclick="getModalPayment()" class="btn btn-primary text-blue-600 hover:text-white">Back</button>
            <button type="button" id="close" class="btn btn-secondary border-red-600 text-red-600 hover:bg-red-600 hover:text-white" data-bs-dismiss="modal">Close</button>
        </div>`
    );
}

function getPaymentFailed(){
    $("#form-payment").append(
        `<div class="modal-body flex justify-center flex-col>
            <div class="">
                <img src="/static/images/silang_merah.png" class="mr-3 h-10 sm:h-20" alt="Silang Merah">
            </div>
            <div class="text-center">
                <div class="text-red-500 text-2xl"> Payment Failed</div>
            </div>
            <div class="text-center my-4">
                <p>Your payment was not successfully processed because it is less than the price</p>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" onclick="getModalPayment()" class="btn btn-primary text-blue-600 hover:text-white">Back</button>
            <button type="button" id="close" class="btn btn-secondary border-red-600 text-red-600 hover:bg-red-600 hover:text-white" data-bs-dismiss="modal">Close</button>
        </div>`
    );
}

function getForm(){
    $("#rows").empty();
    $.get('json/', function(data) {
        $.each(data, function(index, value) { 
            var tag = ""
            if(value.fields.patient_status_payment){
                tag = `<div class='text-white text-lg bg-green-500 w-full text-center' >${value.fields.bill}</div>`
            }else{
                tag = `<div class="text-white text-lg bg-red-500 w-full text-center">${value.fields.bill}</div>`
            }
            $("#rows").append(
                `<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                ${value.fields.patient}
                </th>
                <td class="py-4 px-6">
                ${value.fields.date}
                </td>
                <td class="py-4 px-6">
                ${value.fields.doctor}
                </td>
                <td class="py-4 px-6">
                ${value.fields.description}
                </td>
                <td class="py-4 px-6">
                ${tag}
                </td>
                </tr>`
            );
        });
    });
}

function getModalDelete(){
    $("#delete").empty();

    var tag = ""
    $.get('json/', function(data) {
        $.each(data,function(index, value) {
            tag += `<option value='${value.pk}'> ${value.fields.patient} with doctor ${value.fields.doctor} : ${value.fields.bill} </option>`
        }); 
        console.log(tag)
        $("#delete").append(`${tag}`);
    });
}

function submitHandlerDelete(){

    var id = $('#delete').val()

    $.ajax({
        type: "POST",
        url: "delete/" + id,
        async:true,
        data: {
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),
        },
        success: function (response){
            getForm();
            getModalDelete();
        },
        error : function (error) {
            console.log(error)
        }
    });
}

