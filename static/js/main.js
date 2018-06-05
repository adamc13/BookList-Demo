$(document).on('submit', '#create-book-form', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/create/',
        data: {
            title:$('#title').val(),
            author:$('#author').val(),
            isbn:$('#isbn').val(),
            url:$('#url').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        document.getElementById("create-book-form").reset();
        update();
      },
      
    error:function(){
        alert("This book entry already exists!");
        document.getElementById("create-book-form").reset();
        update();
      }
    });
});


$(document).on('click', '#delete-book', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/delete/',
        data: {
            book_id:$(this).val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        update();
      }
    });
});


function update() {
    $.ajax({
        type: "POST",
        url: '/update/',
        data: {
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }
    })
    .done(function(response) {
        $('#list-body').html(response);
        filter();
    });
}


function sortBy(key) {
    $.ajax({
        type: "POST",
        url: '/sort/',
        data: {
          sort_id: key,
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }
    })
    .done(function(response) {
        $('#list-body').html(response);
        filter();
    });
}

function filter() {

    var input, table, tr, td, i;
    input = document.getElementById('search-input').value.toUpperCase();
    table = document.getElementById("list");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.textContent.toUpperCase().startsWith(input)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
