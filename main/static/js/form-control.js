function updateInputClassName() {
    let inputs = document.querySelectorAll("input");
    let textAreas = document.querySelectorAll("textarea");
    let selectDivs = document.querySelectorAll("select");

    [...inputs, ...textAreas, ...selectDivs].forEach(input => {
        if(!input.classList.contains("form-control")) {
            console.log(input.type);
            if(input.type == "checkbox") {
                input.classList.add("form-check-input");
            }else {
                input.classList.add("form-control");
            }
            

            if(input.rows) {
                console.log(input);
                input.rows = 4;
            }
        }
    })
}

updateInputClassName();