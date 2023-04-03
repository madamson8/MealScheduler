function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function createFood(current_user) {
    values = {
        "name":$('#food-name').val(),
        "calories":$('#calories').val(),
        "fat":$('#fat').val(),
        "protein":$('#protein').val(),
        "rel_user":current_user
    };
    console.log(values);
    $.ajax({
        url: 'http://127.0.0.1:8000/api/create-food',
        headers: {
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/json'
        },
        method: 'POST',
        dataType: 'json',
        data: JSON.stringify(values),
        success: function(data){
          console.log('success: '+data);
        },
    });
}

function getFood(current_user) {
    $.get("http://127.0.0.1:8000/api/get-food?id=", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      });
}