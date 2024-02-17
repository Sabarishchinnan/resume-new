function addApiDetails(val){
    document.getElementById('clientId').value = ""
    document.getElementById('apiKey').value = ""
    document.getElementById('apiSecret').value = ""
    document.getElementById('requestToken').value = ""
    const URL = '/addUserDetails'
    // const URL = '/settings'
    const xhr = new XMLHttpRequest();
    xhr.open('POST', URL);
    xhr.send(val);
}

function placeOrder(val){
    console.log(val)
    const URL = '/placeOrder'
    const xhr = new XMLHttpRequest();
    xhr.open('POST', URL);
    xhr.send(val);
}


function setTarget(val){
    console.log(val)
    const URL = '/setTarget'
    const xhr = new XMLHttpRequest();
    xhr.open('POST', URL);
    xhr.send(val);
}

function toggle(button) {
    if (button.value == "Algo Disabled") {
      button.value = "Algo Enabled";
    } else {
      button.value = "Algo Disabled";
    }
    console.log(button.value)
    const URL = '/enableAlgo'
    const xhr = new XMLHttpRequest();
    xhr.open('POST', URL);
    xhr.send(button.value);
    // location.reload();
  }


// $(document).ready(function(){
//     $('#myTable').dataTable();
// })


$(document).ready(function() {
    $('#myTable').DataTable();
} );


$(function () {
    $('#myTab li:last-child a').tab('show')
})

// $(function(){
//     $('#myTable').dataTable();
// })