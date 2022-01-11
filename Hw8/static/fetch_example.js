
function getUsers(){
    console.log('clicked');
    let id = document.getElementById("id").value;
    console.log(id);
    fetch('https://reqres.in/api/users/'+id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data){
    console.log(response_obj_data);
    const curr_main = document.querySelector("main");
    const section = document.createElement('section');
    section.innerHTML = `
    <div>
        <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
        <br>
        <a href="mailto:${response_obj_data.email}">Send Email</a>
    </div>
    `;
    curr_main.appendChild(section);

}

