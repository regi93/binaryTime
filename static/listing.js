function loadlist() {
        $.ajax({
            type: "GET",
            url: "/api/v1/timelist",
            data: {},
            success:function(response){
                if (response['result'] == 'success') {
                    alert(response['msg']);
                    let plist = response['plist'];
                    let mlist = response['mlist'];
                    let cnt = 1;
                    plist.forEach(element => {
                        $('#table').append(`<tr>
                        <th scope='row'>${cnt}</th>
                        <td><input type="text" class = "${cnt}"></td>
                        <td>${element.startTime + '~' + element.endTime}</td>
                        </tr>`);
                        cnt += 1;
                    });
                    mlist.forEach(element => {
                        $('#table').append(`<tr>
                        <th scope='row'>${cnt}</th>
                        <td><input type="text" class = "${cnt}"></td>
                        <td>${element.startTime + '~' + element.endTime}</td>
                        </tr>`);
                        cnt += 1;
                    });


                }
            }
        })
    input.addEventListener('submit', article);
    
}
    // 삭제
    // 삭제

    // 삭제

    // 삭제

    // 삭제

    // 삭제

    // 삭제

    // 삭제

    
let input = document.querySelector('input');
function article() {
    let article = input.value
    event.preventDefault();
    console.log(article)
    $.ajax({
        type: "POST",
        url: "/api/v1/timelist",
        data: {},
        success:function(response){
            if (response['result'] == 'success') {
                alert(response['msg']);
            }
        }
    })
}

loadlist();

