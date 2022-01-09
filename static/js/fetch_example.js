console.log('inside fetch')


function getUsers(){
    console.log('clicked');
    // console.log('https://reqres.in/api/users/'+Math.floor(Math.random() * 12));
    fetch('https://reqres.in/api/users/'+Math.floor(Math.random() * 12)).then(
        response => response.json()

    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    console.log(response_obj_data);
    //add to main section in the html that implement this js
    const curr_main = document.querySelector("front_main");
    // define the usr
        const section = document.createElement('section');

        section.innerHTML = `
        <div id="front">
            <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send Email</a>
        </div>
        
        </div>  
        `;
       // let node= document.getElementById("front");
         curr_main.removeChild(curr_main.firstChild);
        curr_main.appendChild(section);
}