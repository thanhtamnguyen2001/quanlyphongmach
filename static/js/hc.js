function add_p() {
    event.preventDefault()
    var name =  $('#sel_med :selected').text()
    var id = parseInt($('#sel_med').val())
    var unit = $('#sel_unit').val()
    var quantity = parseInt($('#inpQuantity').val())
    var using = $('#inpUsing').val()
    console.log(quantity)
    if(name != "" && id != "" && unit != "" && $('#inpQuantity').val() != "" && using != ""){
        fetch('/api/add-prescription', {
        method: 'post',
        body: JSON.stringify({
            'name': name,
            'id': id,
            'unit': unit,
            'quantity': quantity,
            'using': using
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        console.info(res)
        return res.json()
    }).then(function(data){
        console.info(data)
        $("#prescription" +data[id].id).remove()
        var htmlStr = '<tr class='+"table-info"+' id="prescription' +data[id].id + '">'
        htmlStr += '<td>' + name + '</td>'
        htmlStr += '<td>' + data[id].unit + '</td>'
        htmlStr += "<td><div class='form-group'> <input class='form-control' type='number' min='1' onblur='update_p("+ data[id].id +", this)' value='"+ data[id].quantity +"'/></div></td>"
        htmlStr += '<td>' + data[id].using + '</td>'
        htmlStr += "<td><input type='button' value='xóa' onclick='delete_prescription("+ data[id].id +")'class='btn btn-danger'/></td></tr>"
        $('#table_detail').append(htmlStr)
    }).catch(function(err){
        console.error(err)
    })
    }
    else{
        alert("Chưa nhập đủ thông tin đơn thuốc")
    }
}
function add_hc(){
    event.preventDefault()
    var symptoms = $('#inpSymptoms').val()
    var disease_prediction = $('#disease_prediction').val()
    var date_of_registration = $('#inpDR')
}
function update_p(id, obj){
    fetch('/api/update-prescription', {
        method: 'put',
        body: JSON.stringify({
            'id': id,
            'quantity': parseInt(obj.value)
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => console.info(data)).catch(err => console.info(err))
}
function delete_prescription(id){
    if(confirm("Bạn có muốn xoá thuốc này khỏi toa thuốc không?") == true){
        fetch('/api/delete-prescription/'+ id, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(data => {
            console.info(data)
            $("#prescription" + id).remove()
        }).catch(err => console.info(err))
    }
}
