document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", function(){

            const button = form.querySelector("button");

            button.disabled = true;

            button.innerHTML = `
                <span class="spinner-border spinner-border-sm"></span>
                Registering...
            `;

        });

    }

});