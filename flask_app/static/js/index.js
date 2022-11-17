var formLogin = document.getElementById('formLogin'); //obtenemos el formulario

/* vamos a escuchar cuando se realice el evento ON SUBMIT */

formLogin.onsubmit = function (event) {
    event.preventDefault(); /*prevenimos el comportamiento por default de mi formulario*/

    //creamos una variable con todos los datos del formulario
    var formulario = new FormData(formLogin);

    fetch("login", {method: 'POST', body: formulario})
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var mensajeAlerta = document.getElementById('mensajeAlerta');
            mensajeAlerta.innerText = data.message;
            mensajeAlerta.classList.add('alert');
            mensajeAlerta.classList.add('alert-danger');

        });
}