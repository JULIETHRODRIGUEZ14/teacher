// Función para ordenar alfabéticamente la lista de estudiantes
function ordenarAlfabeticamente(listaEstudiantes) {
    var estudiantes = Array.from(listaEstudiantes.children);
    estudiantes.sort(function(a, b) {
        return a.textContent.localeCompare(b.textContent);
    });
    while (listaEstudiantes.firstChild) {
        listaEstudiantes.removeChild(listaEstudiantes.firstChild);
    }
    estudiantes.forEach(function(estudiante) {
        listaEstudiantes.appendChild(estudiante);
    });
}

// Evento para agregar estudiantes globalmente
document.querySelector("button.agregar-global").addEventListener("click", function() {
    var nuevoEstudiante = prompt("Ingrese el nombre del nuevo estudiante:");
    if (nuevoEstudiante) {
        var ficha = prompt("Ingrese el ID de la ficha donde desea agregar al estudiante:");
        var listaEstudiantes = document.getElementById(ficha).querySelector(".lista-estudiantes");
        if (listaEstudiantes) {
            var nuevaFila = document.createElement("li");
            nuevaFila.textContent = nuevoEstudiante;
            listaEstudiantes.appendChild(nuevaFila);
            ordenarAlfabeticamente(listaEstudiantes);
        } else {
            alert("La ficha especificada no existe.");
        }
    }
});

// Evento para eliminar estudiantes globalmente
document.querySelector("button.eliminar-global").addEventListener("click", function() {
    var ficha = prompt("Ingrese el ID de la ficha de la cual desea eliminar al estudiante:");
    var listaEstudiantes = document.getElementById(ficha).querySelector(".lista-estudiantes");
    if (listaEstudiantes) {
        var eliminarPorNombre = confirm("¿Desea eliminar un estudiante por su nombre?");
        if (eliminarPorNombre) {
            var nombreEstudiante = prompt("Ingrese el nombre del estudiante que desea eliminar:");
            var estudiantes = listaEstudiantes.querySelectorAll("li");
            var encontrado = false;
            estudiantes.forEach(function(estudiante) {
                if (estudiante.textContent.trim() === nombreEstudiante.trim()) {
                    listaEstudiantes.removeChild(estudiante);
                    encontrado = true;
                }
            });
            if (!encontrado) {
                alert("El estudiante especificado no existe en la lista de la ficha proporcionada.");
            }
        } else {
            var ultimoItem = listaEstudiantes.lastElementChild;
            if (ultimoItem) {
                listaEstudiantes.removeChild(ultimoItem);
            } else {
                alert("La lista de estudiantes está vacía en la ficha especificada.");
            }
        }
    } else {
        alert("La ficha especificada no existe.");
    }
});
