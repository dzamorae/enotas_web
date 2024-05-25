(function (){

    const btnEliminacionAlumno = document.querySelectorAll(".btnEliminacionAlumno");

    btnEliminacionAlumno.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro de eliminar el alumno?');

            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

})();