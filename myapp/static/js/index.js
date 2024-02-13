
    // Obtener referencias a los elementos HTML
    const agregarEstudianteBtn = document.getElementById("agregarEstudiante");
    const eliminarEstudianteBtn = document.getElementById("eliminarEstudiante");
    const contenedorEstudiantes = document.getElementById("contenedorEstudiantes");

    // Función para agregar un nuevo estudiante a la lista
    function agregarEstudiante() {
        // Crea un nuevo elemento <li>
        const nuevoEstudiante = document.createElement("li");
        nuevoEstudiante.innerHTML = "<a href='#nuevoEstudiante'>Nuevo Estudiante</a>";

        // Agrega el nuevo estudiante a la lista correspondiente
        const lista1 = document.getElementById("lista1").querySelector("ul");
        lista1.appendChild(nuevoEstudiante);
    }

    // Función para eliminar el último estudiante de la lista
    function eliminarEstudiante() {
        // Obtiene la lista de estudiantes
        const lista1 = document.getElementById("lista1").querySelector("ul");

        // Obtiene el último estudiante de la lista
        const ultimoEstudiante = lista1.lastElementChild;

        // Elimina el último estudiante de la lista
        lista1.removeChild(ultimoEstudiante);
    }

    // Agregar oyentes de eventos a los botones
    agregarEstudianteBtn.addEventListener("click", agregarEstudiante);
    eliminarEstudianteBtn.addEventListener("click", eliminarEstudiante);
